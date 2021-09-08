from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def test_multiple_tabs():
    # Start the driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open URL
    driver.get("https://onet.pl")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    #   Process cookies permissions statement
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[1]/div[2]/div/div[4]/button[2]'))).click()

    # Store the ID of the original window
    original_window = driver.current_window_handle
    print(original_window)

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Open several new tabs
    number_of_new_tabs = 5
    for _ in range(number_of_new_tabs):
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div[2]'))).click()
        sleep(0.2)
        driver.switch_to.window(original_window)

    print(driver.window_handles)

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(number_of_new_tabs + 1))

    # Loop through until we find a new window handle
    last_window = driver.window_handles[1]
    print(f"Last window ID is: {last_window}")
    driver.switch_to.window(last_window)
    sleep(3)

    for window_handle in driver.window_handles:
        if window_handle == original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("Onet – Jesteś na bieżąco"))
    print(driver.title)


def main() -> None:
    test_multiple_tabs()


if __name__ == "__main__":
    main()
