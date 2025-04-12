
import datetime
import os
import requests
from pystyle import Colors, Colorate, Center, Write

os.system("title LOLIPOP TERMINAL")

ascii_art = r"""
                  _    ___  _    _  ___  ___  ___               
                 | |  | . || |  <_>| . \| . || . \           
                 | |_ | | || |_ | ||  _/| | ||  _/            
                 |___|`___'|___||_||_|  `___'|_|              
"""

menu = """
------------------------------------
|       (] LOLIPOP MAIN [)         |
|----------------------------------|
| lolipop -l   | view my ip info   |
|------------- |-------------------|
| lolipop -i   | lookup other ip   |
|--------------|-------------------|
"""

def fancy_display(info_dict):
    print()
    for key, value in info_dict.items():
        if value:  
            key_cap = key.replace("_", " ").title()
            Write.Print(f"[~] {key_cap:<20}: {value}\n", Colors.red_to_blue, interval=0.002)
    print()

def section(title):
    bar = f"╔{'═' * (len(title) + 4)}╗\n║  {title}  ║\n╚{'═' * (len(title) + 4)}╝"
    Write.Print(f"\n{bar}\n", Colors.green_to_white, interval=0.005)

def lookup_ip(ip=None):
    target = ip if ip else ""

    section("IPINFO.IO")
    try:
        res1 = requests.get(f"https://ipinfo.io/{target}/json").json()
        subset1 = {
            "ip": res1.get("ip"),
            "hostname": res1.get("hostname"),
            "city": res1.get("city"),
            "region": res1.get("region"),
            "country": res1.get("country"),
            "location (lat, lon)": res1.get("loc"),
            "postal": res1.get("postal"),
            "timezone": res1.get("timezone"),
            "org": res1.get("org"),
            "asn": res1.get("asn"),
            "asn_org": res1.get("asn", {}).get("name") if "asn" in res1 else None,
            "ip_type": res1.get("ip_type"),
            "network": res1.get("network"),
            "company": res1.get("company"),
            "carrier": res1.get("carrier"),
            "region_code": res1.get("region_code"),
            "country_code": res1.get("country_code")
        }
        fancy_display(subset1)
    except:
        Write.Print("[!] Failed to connect to ipinfo.io\n", Colors.red, interval=0.01)

    section("IP-API.COM")
    try:
        res2 = requests.get(f"http://ip-api.com/json/{target}?fields=66842623").json()
        fancy_display(res2)
    except:
        Write.Print("[!] Failed to connect to ip-api.com\n", Colors.red, interval=0.01)

    section("IPWHO.IS")
    try:
        res3 = requests.get(f"https://ipwho.is/{target}").json()
        subset3 = {
            "ip": res3.get("ip"),
            "continent": res3.get("continent"),
            "country": res3.get("country"),
            "region": res3.get("region"),
            "city": res3.get("city"),
            "latitude": res3.get("latitude"),
            "longitude": res3.get("longitude"),
            "postal": res3.get("postal"),
            "timezone": res3.get("timezone", {}).get("id"),
            "utc_offset": res3.get("timezone", {}).get("offset"),
            "country_flag": res3.get("flag", {}).get("emoji"),
            "connection_type": res3.get("connection", {}).get("type"),
            "asn": res3.get("connection", {}).get("asn"),
            "isp": res3.get("connection", {}).get("isp"),
            "domain": res3.get("connection", {}).get("domain"),
            "proxy": res3.get("proxy"),
            "vpn": res3.get("security", {}).get("vpn"),
            "tor": res3.get("security", {}).get("tor"),
            "threat_level": res3.get("security", {}).get("threat_level")
        }
        fancy_display(subset3)
    except:
        Write.Print("[!] Failed to connect to ipwho.is\n", Colors.red, interval=0.01)

    section("IPAPI.CO")
    try:
        res4 = requests.get(f"https://ipapi.co/{target}/json/").json()
        subset4 = {
            "ip": res4.get("ip"),
            "network": res4.get("network"),
            "version": res4.get("version"),
            "city": res4.get("city"),
            "region": res4.get("region"),
            "country_name": res4.get("country_name"),
            "country_code": res4.get("country"),
            "latitude": res4.get("latitude"),
            "longitude": res4.get("longitude"),
            "timezone": res4.get("timezone"),
            "utc_offset": res4.get("utc_offset"),
            "asn": res4.get("asn"),
            "org": res4.get("org"),
            "languages": res4.get("languages"),
            "currency": res4.get("currency"),
        }
        fancy_display(subset4)
    except:
        Write.Print("[!] Failed to connect to ipapi.co\n", Colors.red, interval=0.01)

    section("GEOLOCATION-DB")
    try:
        res6 = requests.get(f"https://geolocation-db.com/json/{target}&position=true").json()
        subset6 = {
            "ip": res6.get("IPv4"),
            "city": res6.get("city"),
            "state": res6.get("state"),
            "country": res6.get("country_name"),
            "country_code": res6.get("country_code"),
            "latitude": res6.get("latitude"),
            "longitude": res6.get("longitude"),
        }
        fancy_display(subset6)
    except:
        Write.Print("[!] Failed to connect to geolocation-db.com\n", Colors.red, interval=0.01)

def save_log(action, additional_info=None):
    log_message = f"{datetime.datetime.now()} - ACTION: {action}"
    
    if additional_info:
        log_message += f" - INFO: {additional_info}"
    
    with open("logs.txt", "a") as log_file:
        log_file.write(log_message + "\n")

def tool_started():
    save_log("Tool started", additional_info="Initialization complete.")

def tool_closed():
    save_log("Tool closed", additional_info="Process terminated normally.")

def action_performed(action_name):
    save_log(f"Action performed: {action_name}", additional_info="Action completed successfully.")

tool_started()  
action_performed("Performing task A")  
tool_closed()

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(ascii_art)))
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(menu)))

    Write.Print("\n[~] Enter command: ", Colors.blue_to_white, interval=0.02)
    cmd = input().strip()

    if cmd == "lolipop -l":
        os.system("cls" if os.name == "nt" else "clear")
        Write.Print("[~] Grabbing your IP info...\n", Colors.cyan_to_blue, interval=0.01)
        lookup_ip()

    elif cmd.startswith("lolipop -i "):
        ip = cmd.replace("lolipop -i ", "").strip()
        if ip:
            os.system("cls" if os.name == "nt" else "clear")
            Write.Print(f"[~] Looking up IP: {ip}...\n", Colors.yellow_to_red, interval=0.01)
            lookup_ip(ip)
        else:
            Write.Print("[!] Usage: lolipop -i <ip>\n", Colors.red, interval=0.01)

    else:
        Write.Print("[!] Unknown command.\n", Colors.red, interval=0.01)

if __name__ == "__main__":
    main()
    input("")
