import scraper
import summarizer


class Driver:
    scraper = scraper.Scraper()
    summarizer = summarizer.Summarizer()

    def _get_text_from_page(self, page_url):
        return self.scraper.scrape_get_text_from_page(page_url)

    def _summarize_text(self, text):
        return self.summarizer.get_summarized_text(text)

    def scrape_and_summarize(self, page_url):
        text = self._get_text_from_page(page_url)
        return self._summarize_text(text)


def main(page_url):
    driver = Driver()
    print(driver.scrape_and_summarize(page_url))


if __name__ == "__main__":
    url = "https://www.nytimes.com/2023/02/03/technology/chatgpt-openai-artificial-intelligence.html"
    main(url)
