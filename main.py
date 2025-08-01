```python
import requests
import json

def check_ip_geolocation(ip_address):
    """
    Check the geolocation of a given IP address using the IPinfo API.
    
    Parameters:
    ip_address (str): The IP address to check.

    Returns:
    dict: A dictionary containing geolocation information.
    """
    url = f"https://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response as a dictionary
    except requests.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None

def display_geolocation_info(ip_info):
    """
    Display the geolocation information in a readable format.
    
    Parameters:
    ip_info (dict): The geolocation information to display.
    """
    if ip_info:
        print("IP Address Information:")
        print(f"IP: {ip_info.get('ip')}")
        print(f"City: {ip_info.get('city')}")
        print(f"Region: {ip_info.get('region')}")
        print(f"Country: {ip_info.get('country')}")
        print(f"Location: {ip_info.get('loc')}")
        print(f"Organization: {ip_info.get('org')}")
    else:
        print("No information to display.")

def main():
    """
    The main function to execute the OSINT IP geolocation script.
    """
    ip_address = input("Enter an IP address to lookup: ")
    ip_info = check_ip_geolocation(ip_address)
    display_geolocation_info(ip_info)

if __name__ == "__main__":
    main()
```
