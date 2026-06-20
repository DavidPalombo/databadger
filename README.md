# DataBadger

A configurable website and data collection platform built with Python.

DataBadger can scrape individual pages, crawl entire websites, extract structured data, analyze site structure, and generate professional reports. It supports both traditional HTML websites and JavaScript-rendered applications through Playwright.

## Features

### Static Website Scraping

* Extract page titles and metadata
* Discover internal and external links
* Collect forms and input fields
* Export results to JSON and CSV

### Site Mapping & Crawling

* Recursive multi-page crawling
* Configurable crawl depth
* Internal link discovery
* Endpoint inventory generation
* Duplicate URL prevention

### JavaScript Rendering

* Playwright browser automation
* Dynamic content extraction
* Screenshot capture
* Headless and visible browser modes

### Reporting

* JSON exports
* CSV exports
* HTML executive reports

## Example Use Cases

### Business Intelligence

* Competitor price monitoring
* Content monitoring
* Product catalog collection
* Market research

### Website Analysis

* Site inventory generation
* Content audits
* Link analysis
* Form discovery

### Security Research

* Application mapping
* Endpoint discovery
* Input surface identification
* Technology fingerprinting

## Architecture

SimpleScraper

* Fast single-page analysis

AdvancedScraper

* Multi-page crawling and site mapping

PlaywrightScraper

* JavaScript-rendered application support

## Example Commands

Scrape a single page:

python main.py scrape https://quotes.toscrape.com

Crawl an entire website:

python main.py crawl https://quotes.toscrape.com --depth 3

Scrape a JavaScript-rendered site:

python main.py playwright-scrape https://quotes.toscrape.com/js

## Output Formats

* JSON
* CSV
* HTML Reports

## Future Enhancements

* Technology fingerprinting
* Robots.txt support
* Crawl resume checkpoints
* Change detection
* Scheduled monitoring
* Recon pipeline integration