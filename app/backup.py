import os
import shutil
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "cartorio.db")
BACKUP_DIR = os.path.join(BASE_DIR, "backups")

os.makedirs(BACKUP_DIR, exist_ok=True)

data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_file = os.path.join(BACKUP_DIR, f"cartorio_{data_atual}.db")

if os.path.exists(DB_PATH):
    shutil.copy2(DB_PATH, backup_file)
    print(f"✅ Backup criado com sucesso: {backup_file}")
else:
    print("⚠️ Banco de dados não encontrado. Verifique o caminho.")
