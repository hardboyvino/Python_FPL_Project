# How to start a new debugger Chrome browser in cmd - start chrome.exe --remote-debugging-port=1991 --user-data-dir="C:\Users\Adeniyi Babalola\Desktop\PythonPrograms\chromedata"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains


def main():
    # Use the Chrome with the localhost:1991
    opt = Options()
    opt.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options = opt)
    driver.get('https://www.flydanaair.com/')

    # Wait for the page to be done loading
    time.sleep(5)

    # # If Newsletter popup shows
    # driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/main/div/section[3]/div[2]/button/div').click()

    # Close the Fraud Alert popup
    # driver.find_element(By.XPATH, value='//*[@id="enquirypopup"]/div/div/div[3]/button').click()

    # Wait for the page to be done loading
    # time.sleep(10)

    # Click on the Departure form so the options can show up
    driver.find_element(By.ID, "bookFrom").click()
    
    # Wait for the page to be done loading
    time.sleep(2)

    # Click on Lagos
    driver.find_element(By.XPATH, value='//*[@id="__layout"]//div/section[1]/ul/li[3]/a').click()

    # If Newsletter popup shows
    # driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/main/div/section[3]/div[2]/button/div').click()

    # Click on the Arrival form so the options can show up
    driver.find_element(By.ID, "bookTo").click()
    
    # Wait for the page to be done loading
    time.sleep(2)

    # Click on Lagos
    driver.find_element(By.XPATH, value='//*[@id="__layout"]//div/section[2]/ul/li[1]/a').click()

    # If Newsletter popup shows
    # driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/main/div/section[3]/div[2]/button/div').click()

    # Select DepartureDate Selector Form
    driver.find_element(By.ID, 'bookDepartureDate').click()

    # Select tomorrow
    driver.find_element(By.XPATH, value='//div/div[2]/div/span[27]').click()

    # Search for flight
    driver.find_element(By.XPATH, value='//form/div[3]/div[3]/div/button').click()


if __name__ == "__main__":
    main()