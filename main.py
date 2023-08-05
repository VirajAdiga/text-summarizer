from driver import Driver


def main(page_url):
    driver = Driver()
    driver.get_summary_of_page(page_url, scraper_type="newspaper")


if __name__ == "__main__":
    # url = "https://jamesclear.com/saying-no"
    url = "https://blog.var.so/intro"
    main(url)
