from scrapers.goose_scraper import GooseScraper
from scrapers.newspaper_scraper import NewspaperScraper
from scrapers.trafilatura_scraper import TrafilaturaScraper


class ScraperFactory:
    """
    Factory class to create required concrete scrapers
    """

    @staticmethod
    def get_scraper(scraper_type):
        scraper_map = {
            "goose": GooseScraper,
            "trafilatura": TrafilaturaScraper,
            "newspaper": NewspaperScraper
        }

        if scraper_type not in scraper_map:
            return None
        return scraper_map[scraper_type]()
