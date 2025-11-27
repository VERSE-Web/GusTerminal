import os
import socket
import subprocess
import requests
import re
import threading
import time
import colorama
from colorama import Fore, Style

colorama.init()

# ==========================
#        PROMPT
# ==========================

def prompt():
    path = os.getcwd()
    return f"{Fore.GREEN}{path}\\$~ {Style.RESET_ALL}"

# ==========================
#       LOADING BAR
# ==========================

def loading_bar(stop_event):
    frames = ["[■_________]", "[■■________]", "[■■■_______]", "[■■■■______]",
              "[■■■■■_____]", "[■■■■■■____]", "[■■■■■■■___]", "[■■■■■■■■__]",
              "[■■■■■■■■■_]", "[■■■■■■■■■■]"]

    i = 0
    while not stop_event.is_set():
        print(f"\r{Fore.YELLOW}Loading {frames[i]}{Style.RESET_ALL}", end="")
        i = (i + 1) % len(frames)
        time.sleep(0.1)

    print("\r", end="")  # clear line

# ==========================
#          ECTping
# ==========================

def ectping(target):
    print(f"\n[+] Target: {target}")

    # Resolve IP
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] IP Address: {ip}")
    except:
        print(f"{Fore.RED}[!] Could not resolve domain.{Style.RESET_ALL}")
        return

    # HTTPS status
    try:
        r = requests.get(f"https://{target}", timeout=3)
        print(f"[+] HTTPS Status: {r.status_code}")
    except:
        print(f"{Fore.RED}[!] HTTPS check failed or no SSL.{Style.RESET_ALL}")

    print("\n[+] Pinging (4 packets):")

    # Start animated loader
    stop_event = threading.Event()
    loader = threading.Thread(target=loading_bar, args=(stop_event,))
    loader.start()

    # Run ping
    ping_cmd = ["ping", "-n", "4", target]
    out = subprocess.check_output(ping_cmd, text=True, errors="ignore")

    # Stop the loading bar
    stop_event.set()
    loader.join()

    print(out)

    # Parse average ping
    match = re.search(r"Average = (\d+ms)", out)
    if match:
        print(f"[+] Average Latency: {match.group(1)}\n")
    else:
        print(f"{Fore.RED}[!] Could not read average.{Style.RESET_ALL}\n")

# ==========================
#            nano
# ==========================

def nano(filename):
    print(f"\n--- nano: editing {filename} ---")
    print("Type your text below. Press ENTER on an empty line to save & exit.\n")

    if os.path.exists(filename):
        with open(filename, "r") as f:
            existing = f.read().strip()
        if existing:
            print("--- Existing Content ---")
            print(existing)
            print("------------------------\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)

    with open(filename, "w") as f:
        f.write(text)

    print(f"\n[+] Saved {filename}\n")

# ==========================
#         MAIN SHELL
# ==========================

def main():
    os.system('title GusTerminal')

    # Always start in C:\Users\user
    try:
        os.chdir(r"C:\Users\user")
    except:
        pass

    while True:
        cmd = input(prompt()).strip()

        if cmd.startswith("cd "):
            try:
                path = cmd.split(" ", 1)[1]
                os.chdir(path)
            except Exception as e:
                print(f"{Fore.RED}[!] cd error: {e}{Style.RESET_ALL}")

        elif cmd == "cls":
            os.system("cls")

        elif cmd == "help":
            print("""
Available Commands:
  cd <path>        - Change directory
  cls              - Clear screen
  nano <file>      - Edit file inside the shell
  ECTping <target> - Custom ping tool
  help             - Show this list
  exit             - Quit shell
  lsdir            - List directory contents
  ipconfig         - Windows IP information
""")

        elif cmd.startswith("nano "):
            filename = cmd.split(" ", 1)[1]
            nano(filename)

        elif cmd.lower().startswith("ectping "):
            target = cmd.split(" ", 1)[1]
            ectping(target)

        elif cmd in ("exit", "quit"):
            break

        elif cmd == "ipconfig":
            try:
                out = subprocess.check_output(["ipconfig"], text=True, errors="ignore")
                print(out)
            except Exception as e:
                print(f"{Fore.RED}[!] ipconfig error: {e}{Style.RESET_ALL}")

        elif cmd == "lsdir":
            os.system("dir")

        elif cmd:
            print(f"{Fore.RED}[!] Unknown command{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
