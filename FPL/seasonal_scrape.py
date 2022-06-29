import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from final_scrapper import (
    move_sliders_and_scrape, random_sleeps, medium_sleep, scrape_players, scrape_players_predict, short_sleep
)


def main():
    # Page is preopened with OPTA Page loaded
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)

    slider_1 = driver.find_element(By.XPATH, "(//span)[18]")
    slider_2 = driver.find_element(By.XPATH, "(//span)[22]")
    position = "DEF"
    gws_to_consider = 6

    move_sliders_and_scrape(driver, slider_1, slider_2, filename=f"{position} PerApp {gws_to_consider}GWs.csv", gws_to_consider=gws_to_consider)

def move_sliders_and_scrape(driver, slider_1, slider_2, filename, gws_to_consider):
    SLIDER_WIDTH = 569

    pixels_per_gw = 15.37837837837838

   # Reset the sliders. Lower slider and Upper slider to last GW
    ActionChains(driver).drag_and_drop_by_offset(slider_2, SLIDER_WIDTH, 0).perform()
    medium_sleep()
    ActionChains(driver).drag_and_drop_by_offset(slider_1, SLIDER_WIDTH, 0).perform() 
    medium_sleep()

    # Move upper slider to prediction GW
    ActionChains(driver).drag_and_drop_by_offset(slider_1, -((gws_to_consider - 1) * pixels_per_gw), 0).perform() # Then move the upper limit to GW3
    random_sleeps()

    data = scrape_players(driver)
    print("Getting the main player data...")
    
    short_sleep()

    #     # Move the sliders forward for the predict scrapping
    #     # Upper slider by PREDICTION RANGE and lower slider by GWs being considered
    #     ActionChains(driver).drag_and_drop_by_offset(slider_2, (pixels_per_gw * PREDICTION_RANGE), 0).perform()
    #     medium_sleep()
    #     ActionChains(driver).drag_and_drop_by_offset(slider_1, (pixels_per_gw * gws_to_consider), 0).perform()
    #     random_sleeps()

    #     which_gw_are_we_on = int(slider_2.text)
    #     print(f"We are on GW {which_gw_are_we_on}")

    #     prediction = scrape_players_predict(driver)
    #     print("Getting prediction data...")

    #     # Merge all the dataFrames using the Name column to match the data across dataFrames 
    #     data_all = data.merge(prediction, how='left', on='Names')

    # # Fill empty cells with NaN
    # data.replace("", np.nan, inplace=True)

    # # Remove all rows that contain NaN
    # data.dropna(subset=["Points_y"], inplace=True)

    #     print("Merged all the data...")

    #     # data_all.to_excel(f"Players with Predicted Points Scrape - {strftime('%a %d %b %Y %H %M %S %p')}.xlsx", index=False)

    #     short_sleep()

    # append_df_to_excel('202122 FWD Per App 2 GW.xlsx', data_all, index=False, header = None)
    data.to_csv(filename, mode="a", index=False, header=True)

    #     short_sleep()

    #     # Return sliders to position before prediction moved the slider
    #     ActionChains(driver).drag_and_drop_by_offset(slider_1, -(pixels_per_gw * gws_to_consider), 0).perform()
    #     medium_sleep()
    #     ActionChains(driver).drag_and_drop_by_offset(slider_2, -(pixels_per_gw * PREDICTION_RANGE), 0).perform()
    #     medium_sleep()

    #     # Move the sliders by 1 GW each so the scraping process can be rinsed and repeated
    #     ActionChains(driver).drag_and_drop_by_offset(slider_2, (pixels_per_gw), 0).perform()
    #     medium_sleep()
    #     ActionChains(driver).drag_and_drop_by_offset(slider_1, (pixels_per_gw), 0).perform()
    #     random_sleeps()


if __name__ == "__main__":
    main()