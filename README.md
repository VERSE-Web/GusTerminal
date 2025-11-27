# GusTerminal (Still under making)
A custom Windows-style terminal written in Python, featuring a green hacker-themed prompt, built-in commands, and a custom ping tool (`ECTping`). Fully supports custom icons when compiled with PyInstaller.

## 🚀 Features

### Custom Prompt
- Displays as: `C:\Users\user\$~` in neon green.
- Always starts in the user's home directory.

### Built-in Commands
- `cd <path>` — Change directory
- `cls` — Clear screen
- `lsdir` — List directory contents (uses dir)
- `ipconfig` — Windows IP info
- `nano <file>` — Simple built-in text editor
- `ECTping <target>` — Advanced ping tool with:
  - IP resolver
  - HTTPS status code check
  - 4-packet ping
  - Animated loading bar
  - Average latency extraction
- `help` — Shows command list
- `exit` — Close GusTerminal

### Animated Loading Bar
Runs during ECTping while Windows ping command executes.

### Terminal Title
Automatically sets the CMD window title to:
GusTerminal

## 🔧 How to Run (Python)

Install required modules:
pip install requests colorama

Run the terminal:
python gus_terminal.py

## 🛠️ Building the .exe (PyInstaller)

Install PyInstaller:
pip install pyinstaller

Build the executable with your custom icon:
pyinstaller --onefile --console --icon="gus_icon.ico" gus_terminal.py

Your EXE will be created in:
dist/gus_terminal.exe

## 🎨 Icon
The repo includes a custom neon-green `$~` hacker-style icon.
Use it when building with PyInstaller to theme your terminal.

## 📄 License
CIL Cert V1.2 — Custom Internal License, Version 1.2.
