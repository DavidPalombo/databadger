from src.scraper.simple_scraper import SimpleScraper
from urllib.parse import urljoin, urlparse

class AdvancedScraper(SimpleScraper):

    def __init__(self, max_depth = 3):
        super().__init__()

        self.max_depth = max_depth
        self.visited = set()
        self.pages = []

    def is_internal_link(self, base_url, target_url):
        return (urlparse(base_url).netloc == urlparse(target_url).netloc)
    
    def _crawl_page(self, url, depth):
        if depth > self.max_depth:
            return
        
        if url in self.visited:
            return
        
        self.visited.add(url)

        print(f"Scraping: {url}")

        try:
            page_result = self.scrape(url)
            page_data = page_result["pages"][0]
            self.pages.append(page_data)

            for link in page_data["links"]:
                absolute_url = urljoin(url, link)

                if not self.is_internal_link(url, absolute_url):
                    continue

                self._crawl_page(absolute_url, depth + 1)
        
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return