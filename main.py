from driver import Driver


def main():
    # url = "https://jamesclear.com/saying-no"
    # url = "https://blog.var.so/intro"
    url = "https://www.youtube.com/watch?v=-vSWtmEfkmA"
    driver = Driver()
    driver.get_summary(url)


if __name__ == "__main__":
    main()
