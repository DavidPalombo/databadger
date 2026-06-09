import random
import requests
import time

from bs4 import BeautifulSoup
from src.utils.user_agents import USER_AGENTS

class SimpleScraper:
    def __init__(self):
        self.session = requests.Session()

    def _build_headers(self):
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
        }
    
    def _delay(self):
        time.sleep(random.uniform(1,3))

    def fetch_page(self, url):
        self._delay()

        response = self.session.get(
            url,
            headers = self._build_headers(),
            timeout = 10,
        )

        response.raise_for_status()

        return response
    
    def scrape(self, url):
        response = self.fetch_page(url)

        soup = BeautifulSoup(response.text, "html.parser")

        title = (
            soup.title.text.strip()
            if soup.title
            else ""
        )

        meta_description = ""

        meta_tag = soup.find("meta", attrs = {"name": "description"}, )

        if meta_tag:
            meta_description = meta_tag.get("content", "")

        links = []

        for tag in soup.find_all("a", href=True):
            links.append(tag["href"])

        forms = []

        for form in soup.find_all("form"):
            form_data = {
                "action": form.get("action"),
                "method": form.get("method", "GET"),
                "inputs": [],
            }

            for input_tag in form.find_all("input"):
                form_data["inputs"].append({
                    "name": input_tag.get("name"),
                    "type": input_tag.get("type"),
                })
            
            forms.append(form_data)

        return {
            "target": url,
            "status_code": response.status_code,
            "title": title,
            "meta_description": meta_description,
            "links": links,
            "forms": forms,
        }