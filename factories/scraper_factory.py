from scrapers.goose_scraper import GooseScraper


class ScraperFactory:
    """
    Factory class to create required concrete scrapers
    """

    @staticmethod
    def get_scraper(scraper_type):
        scraper_map = {
            "goose": GooseScraper
        }

        if scraper_type not in scraper_map:
            return None
        return scraper_map[scraper_type]()
