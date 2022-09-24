from bs4 import BeautifulSoup


async def parse_page_with_file():
    with open('/Users/sambhav/Documents/Web-scrapper/scraping-github/github.html') as page:
        parsed_page = BeautifulSoup(page, 'html.parser')
    return parsed_page


async def parse_page(page):
    parsed_page = BeautifulSoup(page, 'html.parser')
    return parsed_page
