from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def test_screenshot():
    #   Initialize webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    #   get to website url
    driver.get("http:\\www.google.pl")

    #   Make a click for google permissions window
    agree_for_google = driver.find_element_by_id("L2AGLb")
    agree_for_google.click()

    #   Insert name for president of Poland into searching form
    input_form = driver.find_element_by_class_name("gLFyf")
    input_form.click()
    input_form.send_keys("Andrzej Duda")

    #   Click search button to execute searching
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,
                                                               "btnK"))).click()

    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').click()
    driver.save_screenshot("andrzej_duda_portret.png")


def main() -> None:
    test_screenshot()


if __name__ == "__main__":
    main()
