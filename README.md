Subdomain Scanner - Python Script

This is a Python-based subdomain scanner tool that allows you to discover active subdomains for a given domain using a wordlist. The script uses multithreading to improve performance and includes useful features such as a progress bar, colored output, duplicate prevention, and timestamped result files.

Features:

Multithreaded scanning with ThreadPoolExecutor

Scans both HTTP and HTTPS versions of each subdomain

Colored terminal output (success in green, failure in red)

Progress bar to visually track scanning progress

Automatically saves found subdomains to a timestamped text file

Prevents duplicate subdomain entries using a Python set

Requirements:

Python 3.x

requests

tqdm

colorama

Install dependencies using pip:
pip install requests colorama tqdm

How to Use:

Make sure you have a file named "subdomainlist.txt" in the same directory. Each line should contain one subdomain prefix (e.g. admin, shop, test).

Run the Python script:
python subdomain_scanner.py

When prompted:

Enter the target domain (e.g. example.com)

Enter the number of threads to use (recommended: 10 to 50)

The script will check each subdomain and print the results in the terminal.

Valid subdomains will be saved to a file named like: found_subdomain_20250731_174512.txt

Example Output:
[FOUND] http://blog.example.com
[FAILED] http://dev.example.com
[FOUND] https://shop.example.com

Notes:

The script will stop checking HTTPS if HTTP is already found for the same subdomain.

Failed requests (e.g. timeout or DNS error) are ignored.

Make sure your wordlist file does not contain empty lines or spaces.

Legal Warning:
This tool is intended for educational and authorized security testing purposes only. Do not use this tool on websites without permission. Unauthorized scanning may be illegal in your jurisdiction.

License:
This script is provided as-is under the MIT License and may be modified or redistributed freely.
