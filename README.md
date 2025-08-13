# 📄 CherryTree Auto Backup Service using Systemd

This script automatically backs up your CherryTree notes at regular intervals while CherryTree is running. It uses a **systemd user service** so it runs in the background after you log in.

You can use this to store backups of anything — you just need to find the process name of the software and specify the location of the files you want to back up.
For example, you could have a dedicated LibreOffice backup folder, and every time you open LibreOffice, the service will create a backup automatically.

---

## 🚀 Set-up

From the folder where your script is stored, run:

### 1️⃣ Make the script executable
```bash
chmod +x cherrytree_backup.py
```

### 2️⃣ Create the systemd user service file, I use vim
```bash
sudo vim ~/.config/systemd/user/cherrytree_backup.service
```

### 3️⃣ Add the following content
```ini
[Unit]
Description=CherryTree Auto Backup Service

[Service]
# Find your Python path with: which python3
# Replace /path/to/python3 below with that output
# Also replace /path/to/cherrytree_backup.py with the full path to your script
ExecStart=/path/to/python3 -u /path/to/cherrytree_backup.py
Restart=always
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=default.target
```

---

## ⚙️ Enable the service

Reload systemd and enable the service so it starts automatically after login:
```bash
systemctl --user daemon-reload
systemctl --user enable cherrytree_backup.service
```

---

## ▶️ Start the service manually
```bash
systemctl --user start cherrytree_backup.service
```

Check if it’s running:
```bash
systemctl --user status cherrytree_backup.service
```

---

## 📡 View live logs
```bash
journalctl --user -u cherrytree_backup.service -f
```


```

