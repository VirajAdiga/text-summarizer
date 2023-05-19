import requests
from bs4 import BeautifulSoup


class Scraper:
    page_parser = 'html.parser'

    def scrape_get_text_from_page(self, url):
        return self._scrape_get_text_from_page(url)

    def _scrape_get_text_from_page(self, url):
        response = requests.get(url)

        # Get the HTML content
        html = response.text

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html, self.page_parser)

        # Remove unwanted elements based on CSS selectors or tags
        unwanted_tags = ['header', 'footer', 'nav', 'figure']
        for tag in soup(unwanted_tags):
            tag.extract()

        # Extract the main content based on specific tags or classes
        content_tags = ['div', 'article', 'section']
        main_content = soup.find_all(content_tags)

        # Extract the text from the main content
        main_text = ' '.join([tag.get_text() for tag in main_content]).strip().lstrip().rstrip()

        # print(main_text)
        return main_text
