import os

import requests
from colorama import Fore,init
os.system("clear")

import os
import time

# Clear screen
os.system("clear")

# Logo & Header
print("""\033[1;32m
  ____  ___    ____  ______  __
 / __ \/   |  / __ )/ __ ) \/ /
/ /_/ / /| | / __  / __  |\  / 
/ _, _/ ___ |/ /_/ / /_/ / / /  
/_/ |_/_/  |_/_____/_____/ /_/   

\033[0m\033[1;36m""" + "-"*50)

# Profile Info
print("\033[0m\033[1;33m👑 Owner   : \033[1;37mRabby")
print("\033[0m\033[1;33m💻 Github  : \033[1;37mRABBY_VAI152")
print("\033[0m\033[1;33m📘 Facebook: \033[1;37mMd Rabby")
print("\033[0m\033[1;36m" + "-"*50)

# Facebook follow prompt
print("\033[0m\033[1;35m📢 FOLLOW MY FACEBOOK:")
time.sleep(2)

# Horizontal line
print("\033[0m\033[1;36m" + "-"*50)

# Wait for user input
input("\033[1;33m[•] PRESS ENTER TO CONTINUE...\033[0m")

# Open Facebook profile
os.system("xdg-open https://www.facebook.com/md.rabby.598002")

# Initialize colorama
init(autoreset=True)

def track_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        res = requests.get(url)
        data = res.json()

        print(f"\n{Fore.CYAN}🔍 IP Tracking Information:\n")
        print(f"{Fore.GREEN}🔹 IP Address: {Fore.YELLOW}{data.get('ip', 'N/A')}")
        print(f"{Fore.GREEN}🌍 Country: {Fore.YELLOW}{data.get('country', 'N/A')}")
        print(f"{Fore.GREEN}🏙️ Region: {Fore.YELLOW}{data.get('region', 'N/A')}")
        print(f"{Fore.GREEN}📍 City: {Fore.YELLOW}{data.get('city', 'N/A')}")
        print(f"{Fore.GREEN}📡 ISP: {Fore.YELLOW}{data.get('org', 'N/A')}")
        print(f"{Fore.GREEN}🛰️ Coordinates: {Fore.YELLOW}{data.get('loc', 'N/A')}")
        print(f"{Fore.GREEN}⏰ Timezone: {Fore.YELLOW}{data.get('timezone', 'N/A')}")
        print(f"\n{Fore.CYAN}✅ Tracking completed.\n")

    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}{'='*40}")
    print(f"{Fore.YELLOW}📌 Rabby's IP Tracker Tool")
    print(f"{Fore.MAGENTA}{'='*40}")
    ip = input(f"{Fore.CYAN}🔎 Enter IP address to track: {Fore.WHITE}")
    track_ip(ip)

