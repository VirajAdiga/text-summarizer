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
        article.download()
        article.parse()
        logger.info(f"Extracting the response")
        article = article.text
        logger.info(f"Article cleaned data is available")
        return article.lstrip().rstrip().strip().replace("\n", " ")
