from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains

# Use the Chrome with the localhost:1991
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:1991")
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options = opt)

def main():
    # Get the pixels of the slider per GW
    slider_width = int(input("What is the width of the slider: "))
    total_gw = int(input("How many GWs so far: "))
    pixels_per_gw = slider_width / (total_gw - 1)
    gws_to_consider = 2

    # Identify the sliders
    slider_1 = driver.find_element(by=By.XPATH, value='//*[@id="__next"]//div[2]/div[2]/span/span[3]/span')
    slider_2 = driver.find_element(by=By.XPATH, value='//*[@id="__next"]//div[2]/div[2]/span/span[4]/span')

    # Get the current GW
    current_gw = driver.find_element(by=By.XPATH, value='//*[@id="__next"]//div[2]/div[2]/span/span[4]/span/span/span').text

    # Reset the sliders. Lower limit to GW1 and Upper slider to last GW
    ActionChains(driver).drag_and_drop_by_offset(slider_1, -500, 0).perform()
    time.sleep(5) # Because FFHub website is slow as balls for both sliders to move together
    ActionChains(driver).drag_and_drop_by_offset(slider_2, -500, 0).perform() # First reset upper limit to GW1
    time.sleep(5) # Because FFHub website is slow as balls for both sliders to move together
    ActionChains(driver).drag_and_drop_by_offset(slider_2, (gws_to_consider * pixels_per_gw), 0).perform() # Then move the upper limit to GW3
    time.sleep(5) # Because FFHub website is slow as balls for both sliders to move together
    move_slider(slider_1, slider_2, pixels_per_gw, gws_to_consider)

def move_slider(slide1, slide2, pixels, gw):
    current_gw = "1" # Initialise to 1

    while current_gw < "5":
        # Move lower slider to appropraite GW for the scrapping
        ActionChains(driver).drag_and_drop_by_offset(slide1, pixels, 0).perform()
        time.sleep(5)
        ActionChains(driver).drag_and_drop_by_offset(slide2, pixels, 0).perform()
        time.sleep(5)

        # Get the current GW
        current_gw = driver.find_element(by=By.XPATH, value='//*[@id="__next"]//div[2]/div[2]/span/span[4]/span/span/span').text


main()
