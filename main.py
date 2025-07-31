import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
from tqdm import tqdm
from datetime import datetime

# Initialize colorama with auto-reset for clean output
init(autoreset=True)

# Get user input for target domain and number of threads
target_input = input("Enter the target domain: ").strip()
max_threads = int(input("Max threads (default 20): ") or 20)

# Generate timestamped output file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f"found_subdomain_{timestamp}.txt"

# Set to avoid duplicate subdomain entries
found_subdomains = set()

# Subdomain scanning function
def scan_subdomain(word):
    word = word.strip()
    for protocol in ["http", "https"]:
        url = f"{protocol}://{word}.{target_input}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code < 400:
                if url not in found_subdomains:
                    found_subdomains.add(url)
                    print(Fore.GREEN + f"[FOUND]  {url}")
                    with open(output_file, "a") as f:
                        f.write(url + "\n")
                break  # No need to test both protocols if one works
        except requests.RequestException:
            print(Fore.RED + f"[FAILED] {url}")
            pass

# Load subdomain wordlist from file
with open("subdomainlist.txt", "r") as file:
    words = file.readlines()

# Perform multithreaded scanning with progress bar
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    list(tqdm(executor.map(scan_subdomain, words), total=len(words)))

# Final message
print(Style.BRIGHT + Fore.CYAN + f"\nScan complete. Results saved to: {output_file}")
