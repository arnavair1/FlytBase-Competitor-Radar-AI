import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # remove scripts/styles
        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        return text.strip()

    except Exception as e:
        print("Scrape error:", e)
        return None
