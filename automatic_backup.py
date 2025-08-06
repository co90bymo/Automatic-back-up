import psutil
import time
import shutil
from datetime import datetime
from pathlib import Path
import sys


# --- Configuration parameters ---
# Name of the process to monitor for triggering backups#
PROCESS_NAME = 'cherrytree'
# Source and Backup paths
SOURCE_DIR = Path.home() / "Documents" / "Cherry Tree"
BACKUP_DIR = Path.home() / "Documents" / "Backups" / "Cherry Tree"
# Time between back ups
BACKUP_INTERVAL = 300
# Maximum number of back ups
MAX_BACKUPS = 50

# --- Initial folder checks ---
try:
    if not SOURCE_DIR.exists():
        raise FileNotFoundError(f"Source directory does not exist: {SOURCE_DIR}")
    
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

except Exception as e:
    print(f"Startup error: {e}")
    sys.exit(1)

# This method is extracted for easier debugging
def delete_oldest_backup():
    backups = [f for f in BACKUP_DIR.iterdir()]

    if (len(backups) > MAX_BACKUPS):
        backups_sorted = sorted(backups)
        shutil.rmtree(backups_sorted[0])

    
def save_backup():
    # Delete old back-ups
    delete_oldest_backup()

    # Create a timestamped subdirectory for this backup
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_subdir = BACKUP_DIR / f"backup_{timestamp}"
    backup_subdir.mkdir()

    # Copy all .ctb and .ctd files (or everything, if preferred)
    for file in SOURCE_DIR.iterdir():
        if file.suffix in (".ctb", ".ctd"):  # or remove this check to copy all files
            shutil.copy2(file, backup_subdir)

    print(f"Backup saved to: {backup_subdir}")

# --- Main logic loop ---
while True:
    for proc in psutil.process_iter(['name']):
        if (proc.info['name'] == PROCESS_NAME):
            save_backup()
    time.sleep(BACKUP_INTERVAL)
    
