from .main import run, lookup_ip
import requests

def lolipop_get_publicip(ip=None):
    if not ip:
        ip = requests.get("https://api.ipify.org").text
    return lookup_ip(ip)

def lolipop_get_publicip():
    return requests.get("https://api.ipify.org").text

def display_ascii_art():
    ascii_art = r"""
    _    ___  _    _  ___  ___  ___
   | |  | . || |  <_>| . \| . || . \ 
   | |_ | | || |_ | ||  _/| | ||  _/ 
   |___|`___'|___||_||_|  `___'|_|  
    """
    print(ascii_art)

def print_help():
    help_text = """
    ------------------------------------
    |       (] LOLIPOP MAIN [)         |
    |----------------------------------|
    | lolipop -l   | View my IP info  |
    | lolipop -i   | Lookup other IP  |
    | lolipop -h   | Show help         |
    ------------------------------------
    """
    print(help_text)
