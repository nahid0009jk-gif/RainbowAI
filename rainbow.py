cat << 'EOF' > rainbow.py
import os
import sys
import time
import webbrowser

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
{CYAN}============================================================={RESET}
{MAGENTA}{BOLD}
   ___ _____  ___ _  _______  ______  _  _   ___ 
  / _ \\/ _ \\ / _ \\ |/ / __/ |/ / __ \\/ /| | / _ \\
 / , _/ __ // // / ' /\\ \\/    / /_/ / /_| |/ __ /
/_/|_/_/ |_/____/_/\\_/__/_/|_/\\____/____/|_/_/ |_|
{RESET}
{YELLOW}{BOLD}              ✨ RainbowAI - by Yusuf haydar ✨           {RESET}
{CYAN}============================================================={RESET}
    """)
    print(f"
 {GREEN}[01]{RESET} {WHITE}Open LimeWire Download Link (Auto-Redirect){RESET}")
    print(f" {RED}[00]{RESET} {WHITE}Exit Program{RESET}\n")

    user_choice = input(f"{YELLOW}👉 Enter Your Choice >> {RESET}").strip()

    if user_choice in ["01", "1"]:
        print(f"\n{GREEN}[+] Opening browser and redirecting...{RESET}")
        time.sleep(1)
        webbrowser.open("https://limewire.com/d/o7y92#82fUqyp")
        print(f"{CYAN}[✔] Redirected successfully to LimeWire!{RESET}\n")
    else:
        print(f"\n{RED}[!] Exiting... Goodbye! 👋{RESET}\n")
        sys.exit()

if __name__ == "__main__":
    main()
EOF
python rainbow.py