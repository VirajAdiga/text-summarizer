from goose3 import Goose
from loguru import logger

from base.scraper import Scraper


class GooseScraper(Scraper):
    """
    Concrete scraper using goose
    """

    def scrape_get_text_from_page(self, url):
        g = Goose()
        g.config.browser_user_agent = "Mozilla 5.0"
        logger.info(f"Sending request to page '{url}'")
        article = g.extract(url=url)
        logger.info(f"Extracting the response")
        g.close()
        logger.info(f"Article cleaned data is available")
        return article.cleaned_text.lstrip().rstrip().strip().replace("\n", " ")
