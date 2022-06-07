import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from final_scrapper import (
    click_per90,
    click_per_start,
    click_perapp,
    season_201819,
    season_201920,
    season_202021,
    season_202122,
    move_sliders_and_scrape,
)


def main():
    start_time = time.time()
    # Page is preopened with OPTA Page loaded
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    slider_1 = driver.find_element(By.XPATH, "(//span)[18]")
    slider_2 = driver.find_element(By.XPATH, "(//span)[22]")

    position = "GK"

    # 1
    click_perapp(driver)
    season_201819(driver, wait)
    for_loop_scrape_perapp(driver, slider_1, slider_2, position)

    # 2
    click_perapp(driver)
    season_201920(driver, wait)
    for_loop_scrape_perapp(driver, slider_1, slider_2, position)

    # 3
    click_perapp(driver)
    season_202021(driver, wait)
    for_loop_scrape_perapp(driver, slider_1, slider_2, position)

    # 4
    click_perapp(driver)
    season_202122(driver, wait)
    for_loop_scrape_perapp(driver, slider_1, slider_2, position)

    # 5
    click_per_start(driver)
    season_201819(driver, wait)
    for_loop_scrape_perstart(driver, slider_1, slider_2, position)

    # 6
    click_per_start(driver)
    season_201920(driver, wait)
    for_loop_scrape_perstart(driver, slider_1, slider_2, position)

    # 7
    click_per_start(driver)
    season_202021(driver, wait)
    for_loop_scrape_perstart(driver, slider_1, slider_2, position)

    # 8
    click_per_start(driver)
    season_202122(driver, wait)
    for_loop_scrape_perstart(driver, slider_1, slider_2, position)

    # 9
    click_per90(driver)
    season_201819(driver, wait)
    for_loop_scrape_per90(driver, slider_1, slider_2, position)

    # 10
    click_per90(driver)
    season_201920(driver, wait)
    for_loop_scrape_per90(driver, slider_1, slider_2, position)

    # 11
    click_per90(driver)
    season_202021(driver, wait)
    for_loop_scrape_per90(driver, slider_1, slider_2, position)

    # 12
    click_per90(driver)
    season_202122(driver, wait)
    for_loop_scrape_per90(driver, slider_1, slider_2, position)

    print(f"Time taken - {(time.time() - start_time)}")


def for_loop_scrape_perapp(driver, slider_1, slider_2, position):
    for i in range(2, 7):
        move_sliders_and_scrape(
            driver, slider_1, slider_2, filename=f"{position} PerApp {i}GWs.csv", gws_to_consider=i
        )


def for_loop_scrape_perstart(driver, slider_1, slider_2, position):
    for i in range(2, 7):
        move_sliders_and_scrape(
            driver, slider_1, slider_2, filename=f"{position} PerStart {i}GWs.csv", gws_to_consider=i
        )


def for_loop_scrape_per90(driver, slider_1, slider_2, position):
    for i in range(2, 7):
        move_sliders_and_scrape(
            driver, slider_1, slider_2, filename=f"{position} Per90 {i}GWs.csv", gws_to_consider=i
        )


if __name__ == "__main__":
    main()
