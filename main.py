```python
import requests
from bs4 import BeautifulSoup
import argparse

def fetch_ip_info(ip_address):
    """
    Fetches IP address information from an online API.

    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing IP information.
    """
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the information of an IP address in a readable format.

    Args:
        ip_info (dict): Dictionary containing IP information.
    """
    if ip_info:
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
    else:
        print("No information available for this IP address.")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="OSINT IP Address Lookup Tool")
    parser.add_argument('ip', type=str, help='IP address to look up')
    args = parser.parse_args()

    # Fetch and display IP address information
    ip_info = fetch_ip_info(args.ip)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
