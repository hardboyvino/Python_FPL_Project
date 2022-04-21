from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains


def main():
    # The location of my ChromeDriver
    chromedriver_path = "C:\Program Files (x86)\chromedriver.exe"

    # Create the ChromeOptions so I can have it always open in Incognito mode
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    # Use the driver to open up the website
    driver = webdriver.Chrome(options=options,executable_path=chromedriver_path)
    driver.get('https://www.flyairpeace.com/')

    # Wait for the page to be done loading
    time.sleep(15)

    # Close the Fraud Alert popup
    driver.find_element(By.XPATH, value='//*[@id="enquirypopup"]/div/div/div[3]/button').click()

    # Wait for the page to be done loading
    time.sleep(5)

    # Select Abuja as Depature Location
    select = Select(driver.find_element(By.ID, "Origin")).select_by_value("ABV")
    
    # Wait for the page to be done loading
    time.sleep(5)

    # Select Arrival Location
    Select(driver.find_element(By.ID, "Destination")).select_by_value("LOS")

if __name__ == "__main__":
    main()