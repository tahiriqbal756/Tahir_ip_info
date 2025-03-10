import requests
import pyfiglet
import webbrowser
from termcolor import colored

def banner():
    print(colored(pyfiglet.figlet_format("Tahir IP Info"), 'cyan'))

def get_ip_info(ip=""):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    
    if response['status'] == 'success':
        print(colored(f"📌 IP Info for: {response['query']}", 'yellow'))
        print(colored(f"🌍 Country: {response['country']}", 'green'))
        print(colored(f"🏙 City: {response['city']}", 'cyan'))
        print(colored(f"🗺 Region: {response['regionName']}", 'magenta'))
        print(colored(f"📍 Latitude: {response['lat']}, Longitude: {response['lon']}", 'blue'))
        print(colored(f"📡 ISP: {response['isp']}", 'red'))
        
        maps_link = f"https://www.google.com/maps?q={response['lat']},{response['lon']}"
        print(colored(f"🗺 Live Location: {maps_link}", 'yellow'))
        open_map = input(colored("📌 Open in Google Maps? (y/n): ", "cyan")).lower()
        if open_map == "y":
            webbrowser.open(maps_link)
    else:
        print(colored("❌ Invalid IP Address!", 'red'))

def menu():
    while True:
        banner()
        print(colored("1️⃣ Your Own IP Info", "green"))
        print(colored("2️⃣ Enter IP to Lookup", "cyan"))
        print(colored("3️⃣ Exit", "red"))
        choice = input(colored("🔹 Select an option: ", "yellow"))

        if choice == "1":
            get_ip_info("")
        elif choice == "2":
            ip = input(colored("🔍 Enter IP Address: ", 'yellow'))
            get_ip_info(ip)
        elif choice == "3":
            print(colored("👋 Exiting... Bye!", 'red'))
            break
        else:
            print(colored("❌ Invalid Option! Try Again.", "red"))

if __name__ == "__main__":
    menu()
          
