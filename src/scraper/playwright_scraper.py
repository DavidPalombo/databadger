from bs4 import BeautifulSoup
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright

class PlaywrightScraper:

    def __init__(self, headless = True):
        # headless is set to True for no browser window to appear
        self.headless = headless

    def get_page_html(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless = self.headless)

            page = browser.new_page()

            page.goto(url, wait_until = "networkidle", timeout = 10000)

            html = page.content()

            browser.close()

            return html
        
    def scrape(self, url):
        html = self.get_page_html(url)

        soup = BeautifulSoup(html, "html.parser")

        # Extract page title
        title = (
            soup.title.text.strip()
            if soup.title
            else ""
        )

        # Extract meta description
        meta_description = ""

        meta_tag = soup.find("meta", attrs = {"name": "description"})

        if meta_tag:
            meta_description = meta_tag.get("content", "")

        # Extract Links
        links = []

        for tag in soup.find_all("a", href = True):
            links.append(tag["href"])

        # Extract forms
        forms = []

        for form in soup.find_all("form"):
            form_data = {
                "action": form.get("action"),
                "method": form.get("method", "GET"),
                "inputs": []
            }

            for input_tag  in form.find_all("input"):
                form_data["inputs"].append({
                    "name": input_tag.get("name"),
                    "type": input_tag.get("type"),
                })

            forms.append(form_data)

        """
        TODO: defaulting the status code to 200 for now. Future improvement will be
        to capture:
            - Actual HTTP status code
            - Response headers
            - Redirect chains
            - Network requests
        """
        page_data = {
            "url": url,
            "status_code": 200,
            "title": title,
            "meta_description": meta_description,
            "links": links,
            "forms": forms,
            "response_headers": {
                "source": "playwright_browser"
            },
            "content_length": len(html),
        }

        return {
            "target": url,
            "scan_time": datetime.now(timezone.utc).isoformat(),
            "summary": {
                "pages_discovered": 1,
                "links_found": len(links),
                "forms_found": len(forms),
            },
            "pages": [page_data]
        }
