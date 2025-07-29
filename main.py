import requests
from bs4 import BeautifulSoup
import sys

def fetch_page(url):
    """Fetch the content of a web page."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        sys.exit(1)

def extract_emails(html):
    """Extract email addresses from HTML content."""
    emails = set()
    for line in html.split('\n'):
        if '@' in line:
            # Simple regex to find emails
            emails.update(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', line))
    return emails

def main(url):
    """Main function to perform OSINT on a given URL."""
    print(f"Fetching content from {url}...")
    html_content = fetch_page(url)
    
    print("Extracting email addresses...")
    emails = extract_emails(html_content)
    
    if emails:
        print("Found the following email addresses:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python osint_script.py <url>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    main(target_url)