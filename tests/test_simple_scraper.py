from src.scraper.simple_scraper import SimpleScraper

def test_scrape_returns_dict():
    scraper = SimpleScraper()

    data = scraper.scrape("https://quotes.toscrape.com")

    assert isinstance(data, dict)
    assert "links" in data
    assert "forms" in data