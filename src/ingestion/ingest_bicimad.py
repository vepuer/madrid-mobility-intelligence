import os
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import re

# --- CONFIGURATION ---
BASE_URL = "https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=54e76af6a185a910VgnVCM200000f921e388RCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default&idValorado=54e76af6a185a910VgnVCM200000f921e388RCRD&action=addValoracion&puntuacion=4"
DOMAIN = "https://datos.madrid.es"
RAW_DATA_PATH = "data/bronze"

# Fake User-Agent to avoid being blocked
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_zip_links():
    """
    Parses the specific HTML structure of datos.madrid.es to find Years and ZIPs.
    """
    print(f"🔎 Scanning {BASE_URL}...")
    
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        zip_links = {}

        # LOGIC BASED ON YOUR HTML SNIPPET:
        # 1. Find all <p class="info-title"> (e.g., "Datos bicimad 2023")
        titles = soup.find_all('p', class_='info-title')
        
        print(f"👀 Found {len(titles)} data groups. Analyzing...")

        for title in titles:
            text = title.get_text().strip()
            
            # Check if this title is about Bicimad and has a Year
            if "bicimad" in text.lower():
                # Extract year using Regex (find 4 digits starting with 20)
                year_match = re.search(r'20\d{2}', text)
                
                if year_match:
                    year = int(year_match.group(0))
                    
                    # 2. The link is in the NEXT element after the title
                    # We look for the next <a> tag with class "ico-zip"
                    link_tag = title.find_next('a', class_='ico-zip')
                    
                    if link_tag and 'href' in link_tag.attrs:
                        clean_link = urljoin(DOMAIN, link_tag['href'])
                        zip_links[year] = clean_link
                        print(f"   👉 Found Year {year}")

        return zip_links

    except Exception as e:
        print(f"❌ Error scraping URL: {e}")
        return {}

def download_file(url, year):
    filename = f"bicimad_{year}.zip"
    filepath = os.path.join(RAW_DATA_PATH, filename)

    if os.path.exists(filepath):
        print(f"✅ [SKIP] Year {year} already exists.")
        return

    print(f"⬇️  [DOWNLOADING] Year {year}...")
    try:
        response = requests.get(url, headers=HEADERS, stream=True)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"🎉 [SUCCESS] Saved {filename}")
        time.sleep(1)
    except Exception as e:
        print(f"❌ [ERROR] Failed to download {year}: {e}")

if __name__ == "__main__":
    print("🚀 Starting Automated BiciMAD Ingestion (Scraper v2)...")
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    links = get_zip_links()
    
    if not links:
        print("⚠️ No links found! The HTML structure might have changed.")
    else:
        print(f"🔎 Found {len(links)} valid datasets.")
        # Sort years descending (2023 first)
        for year in sorted(links.keys(), reverse=True):
            download_file(links[year], year)

    print("🏁 Ingestion Finished.")