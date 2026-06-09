import click

from rich import print
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

if __name__ == "__main__":
    cli()