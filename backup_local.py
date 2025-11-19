import os
import subprocess
import datetime

# MySQL connection details
MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Secret123"
MYSQL_DB = "prog8850"

# Local “Azure Storage” folder
BACKUP_DIR = "azure_backup_storage"

def main():
    # Ensure backup folder exists
    os.makedirs(BACKUP_DIR, exist_ok=True)

    # Create timestamped filename
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    backup_filename = f"mysql-{MYSQL_DB}-{ts}.sql"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    print(f"Creating backup: {backup_path}")

    # Run mysqldump command
    cmd = [
        "mysqldump",
        f"-h{MYSQL_HOST}",
        f"-u{MYSQL_USER}",
        f"-p{MYSQL_PASSWORD}",
        MYSQL_DB
    ]

    # Write dump to file
    with open(backup_path, "w") as f:
        subprocess.run(cmd, stdout=f, check=True)

    print(f"Backup completed successfully: {backup_path}")

if __name__ == "__main__":
    main()
