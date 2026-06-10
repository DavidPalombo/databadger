import click

from rich import print
from src.scraper.advanced_scraper import AdvancedScraper
from src.scraper.simple_scraper import SimpleScraper
from src.scraper.exporters import export_csv, export_json

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

    scraper = AdvancedScraper(max_depth = depth)

    data = scraper.crawl(url)

    export_csv(data, "output/crawl_results.csv")
    export_json(data, "output/crawl_results.json")

    print(f"[green]Finished. Found {data['summary']['pages_discovered']} pages[/green]")

if __name__ == "__main__":
    cli()