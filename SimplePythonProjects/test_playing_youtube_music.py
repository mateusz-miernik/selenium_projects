from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_playing_youtube_music():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.youtube.com")

    #   Process intro about cookies
    process_cookies = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             '/html/body/ytd-app/ytd-consent-bump-v2-lightbox'
                                                             '/tp-yt-paper-dialog/div[2]/div[2]/div[5]/div[2]/'
                                                             'ytd-button-renderer[2]/a')))
    process_cookies.click()

    #   Type specific text into search bar and execute searching
    search_bar = driver.find_element_by_id("search")
    search_bar.click()
    search_bar.send_keys("Krzysztof Krawczyk Parostatek")
    execute_search = driver.find_element_by_id("search-icon-legacy")
    execute_search.click()

    #   Find and click first video of searching results

    play_music = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            '/html/body/ytd-app/div/ytd-page-manager/'
                                                            'ytd-search/div[1]/'
                                                            'ytd-two-column-search-results-renderer/div/'
                                                            'ytd-section-list-renderer/div[2]/'
                                                            'ytd-item-section-renderer/div[3]/'
                                                            'ytd-video-renderer[1]/div[1]')))
    play_music.click()
    sleep(240)


def main() -> None:
    test_playing_youtube_music()


if __name__ == "__main__":
    main()
