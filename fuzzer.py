import requests

def show_banner():
    print(r'''
    =========================================================================
      ____  ___ ____      ____  _   _ ____ _____ _____ ____  
     |  _ \|_ _|  _ \    | __ )| | | / ___|_   _| ____|  _ \ 
     | | | || || |_) |   |  _ \| | | \___ \ | | |  _| | |_) |
     | |_| || ||  _ <    | |_) | |_| |___) || | | |___|  _ < 
     |____/|___|_| \_\   |____/ \___/|____/ |_| |_____|_| \_\
                                                               
     [ Cyb-Weapons Lab | Directory Enumerator ]
     [ Created by White20devilera ]
    =========================================================================
    ''')

def dir_buster(target_url, directory_list_path):
    # if url does not contain "http" or "https" it is being added
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
        print(f"[*] Protocol missing! Using default: {target_url}")

    print(f"[*] Target URL: {target_url}")
    print(f"[*] Wordlist: {directory_list_path}")
    print("-" * 50)

    try:
        with open(directory_list_path, 'r') as file:
            for line in file:
                directory_name = line.strip()
                
                # skips lines where it begins with spaces or with a '#'
                if not directory_name or directory_name.startswith('#'):
                    continue
                
                test_url = f"{target_url}/{directory_name}"
                
                try:
                    response = requests.get(test_url, timeout=3)
                    if response.status_code == 200:
                        print(f"[+] Found: {test_url} (Status: 200 OK)")
                    elif response.status_code == 403:
                        print(f"[!] Forbidden: {test_url} (Status: 403)")
                        
                except requests.exceptions.RequestException:
                    # skips if any network error occur
                    pass

    except FileNotFoundError:
        print(f"[!] Error: File '{directory_list_path}' not found.")

show_banner()

target = input("Enter target URL: ").strip()
wordlist = input("Enter the path to your directory list (e.g., directories.txt): ").strip()


dir_buster(target, wordlist)