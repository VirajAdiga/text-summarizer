from driver import Driver


def main():
    # page_url = "https://jamesclear.com/saying-no"
    page_url = "https://blog.var.so/intro"
    driver = Driver()
    driver.get_summary_of_page(page_url)


if __name__ == "__main__":
    main()
