"""
    Script for testing downloading ebooks from page https://www.salesmanago.com
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from argparse import ArgumentParser, Namespace
from time import sleep
from pathlib import Path


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
        cookies_permission = wait.until(EC.element_to_be_clickable((By.ID, 'close-cookies')))  # close cookies message
        cookies_permission.click()

        resources_section = \
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   'body > nav > section > nav > div > div > ul > li:nth-child(5)')))
        resources_section.click()

        ebooks_page = \
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   'body > nav > section > nav > div > div > ul > li:nth-child(5) '
                                                   '> div > div > div > div.col-md-6 > div > div:nth-child(1) > ul '
                                                   '> li:nth-child(2) > a')))
        ebooks_page.click()

        ebook_elements = driver.find_elements_by_class_name("ebook__img--container")
        ebook_names = [Path(element.get_attribute('href')).stem
                       for element in driver.find_elements_by_css_selector('div.ebook__img--container a')]

        all_ebooks = {ebook_name: ebook_element for (ebook_name, ebook_element) in zip(ebook_names, ebook_elements)}

        for idx, ebook in enumerate(all_ebooks.items(), start=1):
            print(f"{idx}: {ebook}")

        declared_ebook = all_ebooks[stringinput]
        declared_ebook.click()

        print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[1])

        name_and_surname = wait.until(EC.element_to_be_clickable((By.NAME, 'name')))
        name_and_surname.click()
        name_and_surname.send_keys("Mateusz Miernik")

        email = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
        email.click()
        email.send_keys("mateusz.miernik.benhauer+testrekrutacja@salesmanago.com")

        company = wait.until(EC.element_to_be_clickable((By.NAME, 'company')))
        company.click()
        company.send_keys("The Best Company")

        website = wait.until(EC.element_to_be_clickable((By.NAME, 'url')))
        website.click()
        website.send_keys("https://www.google.com")

        phone_number = wait.until(EC.element_to_be_clickable((By.NAME, 'phoneNumber')))
        phone_number.click()
        phone_number.send_keys("501401301")

        try:
            button = driver.find_element_by_css_selector('.btn.center-block.form-btn.form-btn')
        except NoSuchElementException:
            button = driver.find_element_by_css_selector('.btn.btn-success')

        button.click()
        sleep(3)


def main() -> None:
    args = TestEbookDownloading.parse_args()
    ebook_name = args.ebook_name
    driver = TestEbookDownloading.driver_without_pytest()
    wait = TestEbookDownloading.wait_without_pytest(driver)
    test = TestEbookDownloading()
    test.test_ebook_downloading(driver, wait, ebook_name)


if __name__ == "__main__":
    main()
