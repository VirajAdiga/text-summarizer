from newspaper import Article
from loguru import logger

from base.scraper import Scraper


class NewspaperScraper(Scraper):
    """
    Concrete scraper using newspaper library
    """

    def scrape_get_text_from_page(self, url):
        logger.info(f"Sending request to page '{url}'")
        article = Article(url)
        logger.info(f"Extracting the response")
        article.download()
        article.parse()
        return self._clean_data(article.text)
