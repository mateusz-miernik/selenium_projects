"""
    Script for testing downloading ebooks from page https://www.salesmanago.com
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from argparse import ArgumentParser, Namespace
from time import sleep


class TestEbookDownloading:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        del driver

    @pytest.fixture(scope="function")
    def wait(self, driver):
        wait = WebDriverWait(driver, 10)
        yield wait
        del wait

    @staticmethod
    def driver_without_pytest():
        return webdriver.Chrome()

    @staticmethod
    def wait_without_pytest(driver):
        return WebDriverWait(driver, 10)

    @staticmethod
    def parse_args() -> Namespace:
        parser = ArgumentParser("Script for testing downloading ebooks from page https://www.salesmanago.com")
        parser.add_argument("ebook_name", help="Name of ebook for downloading")
        args = parser.parse_args()
        return args

    def test_ebook_downloading(self, driver, wait, stringinput):
        driver.maximize_window()
        driver.get("https://www.salesmanago.com/")
        cookies_permission = wait.until(EC.element_to_be_clickable((By.ID, 'close-cookies')))   # close cookies message
        cookies_permission.click()
        # driver.find_element_by_id("close-cookies").click()
        # sleep(60)
        # resources_page = \
        #     wait.until(EC.element_to_be_clickable((By.XPATH,
        #                                            "/html/body/nav/section/nav/div/div/ul/li[5]/a")))
        resources_page = \
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   'body > nav > section > nav > div > div > ul > li:nth-child(5)')))
        resources_page.click()
        # sleep(60)
        # ebooks_page = \
        #     wait.until(EC.element_to_be_clickable((By.XPATH,
        #                                            "/html/body/nav/section/nav/div/div/ul/li[5]/"
        #                                            "div/div/div/div[2]/div/div[1]/ul/li[2]")))
        ebooks_page = \
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   'body > nav > section > nav > div > div > ul > li:nth-child(5) '
                                                   '> div > div > div > div.col-md-6 > div > div:nth-child(1) > ul '
                                                   '> li:nth-child(2) > a')))
        ebooks_page.click()

        assert stringinput == "ebook"


def main() -> None:
    args = TestEbookDownloading.parse_args()
    ebook_name = args.ebook_name
    driver = TestEbookDownloading.driver_without_pytest()
    wait = TestEbookDownloading.wait_without_pytest(driver)
    test = TestEbookDownloading()
    test.test_ebook_downloading(driver, wait, ebook_name)


if __name__ == "__main__":
    main()
