# 🔐 WiFi Password Recovery Tool

<p align="center">
⠀⠀⠀⠀⠀⢀⣤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⢤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡼⠋⠀⣀⠄⡂⠍⣀⣒⣒⠂⠀⠬⠤⠤⠬⠍⠉⠝⠲⣄⡀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⠊⢔⠕⠈⣀⣀⡀⠈⠆⠀⠀⠀⡍⠁⠀⠁⢂⠀⠈⣷⠀⠀
⠀⠀⣠⣾⠥⠀⠀⣠⢠⣞⣿⣿⣿⣉⠳⣄⠀⠀⣀⣤⣶⣶⣶⡄⠀⠀⣘⢦⡀
⢀⡞⡍⣠⠞⢋⡛⠶⠤⣤⠴⠚⠀⠈⠙⠁⠀⠀⢹⡏⠁⠀⣀⣠⠤⢤⡕⠱⣷
⠘⡇⠇⣯⠤⢾⡙⠲⢤⣀⡀⠤⠀⢲⡖⣂⣀⠀⠀⢙⣶⣄⠈⠉⣸⡄⠠⣠⡿
⠀⠹⣜⡪⠀⠈⢷⣦⣬⣏⠉⠛⠲⣮⣧⣁⣀⣀⠶⠞⢁⣀⣨⢶⢿⣧⠉⡼⠁
⠀⠀⠈⢷⡀⠀⠀⠳⣌⡟⠻⠷⣶⣧⣀⣀⣹⣉⣉⣿⣉⣉⣇⣼⣾⣿⠀⡇⠀
⠀⠀⠀⠈⢳⡄⠀⠀⠘⠳⣄⡀⡼⠈⠉⠛⡿⠿⠿⡿⠿⣿⢿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠀⠙⢦⣕⠠⣒⠌⡙⠓⠶⠤⣤⣧⣀⣸⣇⣴⣧⠾⠾⠋⠀⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣭⣒⠩⠖⢠⣤⠄⠀⠀⠀⠀⠀⠠⠔⠁⡰⠀⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⢤⣀⣀⠉⠉⠀⠀⠀⠀⠀⠁⠀⣠⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠒⠲⠶⠤⠴⠒⠚⠁
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-green.svg" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.6+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg" alt="Platform">
</p>

<p align="center">
  <b>A cross-platform tool to recover saved WiFi passwords</b>
</p>

---

## ✨ Features

| Feature | Linux | Windows | macOS |
|---------|:-----:|:-------:|:-----:|
| List all saved WiFi networks | ✅ | ✅ | ✅ |
| Retrieve single network password | ✅ | ✅ | ✅ |
| Retrieve all passwords at once | ✅ | ✅ | ✅ |
| Save results to file | ✅ | ✅ | ✅ |
| Auto-detect operating system | ✅ | ✅ | ✅ |

---

## 📥 Installation

```bash
git clone https://github.com/tishan-nilusha/wifresti.git
cd wifresti

🚀 Usage

🐧 Linux
Bash
sudo python3 wifresti.py

🪟 Windows
Bash
python wifresti.py
Run as Administrator

🍎 macOS
Bash
sudo python3 wifresti.py

📦 Requirements
Python 3.6+
No external dependencies


🍎 Mac OS Notes
Keychain Access: Mac stores WiFi passwords in the Keychain. The script uses the security command to retrieve them.
Popup Dialog: When running, Mac may show a popup asking for permission to access the Keychain. Click Allow or enter your password.
Wireless Interface: The script tries en0 first, then en1. If neither works, check your interface with:
Bash
networksetup -listallhardwareports
Alternative Method: If the script doesn't work, you can manually check passwords in:
Open Keychain Access app
Search for your WiFi network name
Double-click and check "Show password"

⚠️ Disclaimer
This tool is for educational purposes and legitimate password recovery only.
Use it only on systems you own. The author is not responsible for any misuse.

👤 Author
Tishan Nilusha

