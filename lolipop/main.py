import requests
from . import display_ascii_art, print_help

def lolipop_get_publicip():
    try:
        local_ip = requests.get("https://api.ipify.org").text
        return local_ip
    except requests.exceptions.RequestException as e:
        print(f"[!] An error occurred while fetching the local IP: {e}")
        return None

def lookup_ip(ip=None):
    if not ip:
        ip = lolipop_get_publicip()
    
    if not ip:
        return

    print(f"[~] Looking up information for IP: {ip}")

    ip_info = {}

    try:
        res1 = requests.get(f"https://ipinfo.io/{ip}/json").json()
        ip_info['ip'] = res1.get('ip', 'N/A')
        ip_info['hostname'] = res1.get('hostname', 'N/A')
        ip_info['city'] = res1.get('city', 'N/A')
        ip_info['region'] = res1.get('region', 'N/A')
        ip_info['country'] = res1.get('country', 'N/A')
    except requests.exceptions.RequestException as e:
        print(f"[!] Failed to connect to ipinfo.io: {e}")

    try:
        res2 = requests.get(f"http://ip-api.com/json/{ip}?fields=66842623").json()
        ip_info['region_code'] = res2.get('region', 'N/A')
        ip_info['country_code'] = res2.get('countryCode', 'N/A')
    except requests.exceptions.RequestException as e:
        print(f"[!] Failed to connect to ip-api.com: {e}")

    print("\nIP Information:")
    for key, value in ip_info.items():
        print(f"{key.capitalize()}: {value}")

def display_menu():
    menu = """
    ------------------------------------
    |       (] LOLIPOP MAIN [)         |
    |----------------------------------|
    | lolipop -l   | View my IP info  |
    | lolipop -i   | Lookup other IP  |
    | lolipop -h   | Show help         |
    ------------------------------------
    """
    print(menu)

def run():
    display_ascii_art()
    display_menu()

    user_input = input("Enter a command: ").strip()

    if user_input == "lolipop -l":
        print("\nFetching information for your local IP...")
        ip = lolipop_get_publicip()
        if ip:
            print(f"Your local IP is: {ip}")
            lookup_ip(ip)
        else:
            print("[!] Unable to retrieve your local IP.")

    elif user_input.startswith("lolipop -i"):
        ip_to_lookup = user_input.split(" ", 1)[-1].strip()
        if ip_to_lookup:
            print(f"\nLooking up information for IP: {ip_to_lookup}...")
            lookup_ip(ip_to_lookup)
        else:
            print("[!] Please specify an IP to lookup after 'lolipop -i'.")

    elif user_input == "lolipop -h":
        print_help()

    else:
        print("[!] Unrecognized command. Try 'lolipop -h' for help.")
