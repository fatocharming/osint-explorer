```python
import requests
from bs4 import BeautifulSoup

def fetch_ip_info(ip_address):
    """
    Fetches geolocation and ISP information of the given IP address.
    
    Args:
        ip_address (str): The IP address to query.
    
    Returns:
        dict: A dictionary containing geolocation and ISP information.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the IP information in a readable format.

    Args:
        ip_info (dict): The IP information dictionary.
    """
    if ip_info:
        print(f"IP Address: {ip_info.get('ip')}")
        print(f"Hostname: {ip_info.get('hostname')}")
        print(f"City: {ip_info.get('city')}")
        print(f"Region: {ip_info.get('region')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Location: {ip_info.get('loc')}")
        print(f"Postal: {ip_info.get('postal')}")
        print(f"Organization: {ip_info.get('org')}")
    else:
        print("No information available.")

def main():
    """
    Main function to execute the script.
    """
    ip_address = input("Enter an IP address to analyze: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
