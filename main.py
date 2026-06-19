import click

from rich import print
from src.scraper.advanced_scraper import AdvancedScraper
from src.scraper.config import ScraperConfig
from src.scraper.exporters import export_csv, export_json
from src.scraper.playwright_scraper import PlaywrightScraper
from src.scraper.simple_scraper import SimpleScraper

@click.group()
def cli():
    pass

@cli.command()
@click.argument("url")
def scrape(url):
    print(f"[cyan]Scraping[/cyan] {url}")

    scraper = SimpleScraper()

    data = scraper.scrape(url)

    export_csv(data, "output/results.csv")
    export_json(data, "output/results.json")

    print("[green]Finished[/green]")


@cli.command()
@click.argument("url")
@click.option("--depth", default = 3, help = "Maximum crawl depth")
def crawl(url, depth):
    print(f"[cyan]Crawling[/cyan] {url}")

    config = ScraperConfig(max_depth = depth)

    scraper = AdvancedScraper(config = config)

    data = scraper.crawl(url)

    export_csv(data, "output/crawl_results.csv")
    export_json(data, "output/crawl_results.json")

    print(f"[green]Finished. Found {data['summary']['pages_discovered']} pages[/green]")

@cli.command()
@click.argument("url")
@click.option("--headless", is_flag = True, default = False, help = "Run browser in headless mode")
def playwright_scrape(url, headless):
    print(f"[cyan]Paywright scraping[/cyan] {url}")

    scraper = PlaywrightScraper(headless = headless)

    data = scraper.scrape(url)

    export_json(data, "output/playwright_results.json")

    export_csv(data, "output/playwright_results.csv")

    print(f"[green]Finished. Found {data['summary']['links_found']} links[/green]")

if __name__ == "__main__":
    cli()