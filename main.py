```python
import requests

def fetch_ip_info(ip_address):
    """
    Fetches geolocation and ISP information for a given IP address using the ip-api.com service.
    
    Args:
        ip_address (str): The IP address to look up.
    
    Returns:
        dict: A dictionary containing IP information or an error message.
    """
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def display_ip_info(ip_info):
    """
    Displays the information retrieved for an IP address in a readable format.
    
    Args:
        ip_info (dict): The dictionary containing the IP information.
    """
    if "error" in ip_info:
        print(f"Error: {ip_info['error']}")
        return

    print(f"IP Address: {ip_info.get('query')}")
    print(f"Country: {ip_info.get('country')}")
    print(f"Region: {ip_info.get('regionName')}")
    print(f"City: {ip_info.get('city')}")
    print(f"ISP: {ip_info.get('isp')}")
    print(f"Latitude: {ip_info.get('lat')}")
    print(f"Longitude: {ip_info.get('lon')}")

def main():
    """
    Main function to execute the OSINT project. 
    It prompts the user for an IP address and fetches its information.
    """
    ip_address = input("Enter an IP address to look up: ")
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```