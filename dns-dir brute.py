import sys
import argparse
import requests
import socket
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['dir', 'dns'], help="Choose the mode: 'dir' for directory brute-forcing or 'dns' for DNS enumeration")
parser.add_argument('-w', '--wordlist', type=str, required=True, help="Switch for wordlist")
parser.add_argument('-u', '--url', type=str, help="Switch for URL (for directory brute-forcing)")
parser.add_argument('-d', '--domain', type=str, help="Switch for Domain (for DNS enumeration)")

args = parser.parse_args()

print("[+] Wordlist: ", args.wordlist)
if args.mode == 'dir':
    print("[+] URL: ", args.url)
elif args.mode == 'dns':
    print("[+] Domain: ", args.domain)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

# Read the wordlist
with open(args.wordlist, 'r') as file:
    lines = file.readlines()

def domain_exists(domain):
    """Check if the domain exists."""
    try:
        socket.gethostbyname(domain)  # Attempt to resolve the domain
        return True
    except socket.gaierror:
        return False

def check_subdomain(subdomain):
    """Check the status of a subdomain for DNS enumeration."""
    full_domain = f'{subdomain}.{args.domain}'
    
    # Cache valid domains to avoid repeated DNS lookups
    if domain_exists(full_domain):
        try:
            r = requests.get(f'https://{full_domain}/', headers=headers)
            if r.status_code != 404:
                print(f"{full_domain}")
        except requests.RequestException as e:
            print(f"Request error for {full_domain}: {e}")

if args.mode == 'dns':
    # DNS enumeration mode
    try:
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(check_subdomain, (line.strip() for line in lines))
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    except Exception as e:
        print(f"Error occurred: {e}")

elif args.mode == 'dir':
    # Directory brute-forcing mode
    if args.url is None or ('http' not in args.url and 'https' not in args.url):
        print("Enter a valid URL scheme. (http://example.com or https://example.com)")
        sys.exit()

    try:
        for line in lines:
            line = line.strip("\n")
            r = requests.get(args.url + '/' + line, headers=headers)
            if line.startswith('#'):
                continue
            if r.status_code != 404:
                print(args.url + '/' + line, ":", r.status_code)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    except Exception as e:
        print("Error occurred: ", e)
