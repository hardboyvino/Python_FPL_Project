# This is done considering only forwards. Might have to 'copy-pasta' for defs and midfielders. The issue now is sacked managers scrapping. Might have to do it organically (i.e. sliding and searching the club then running the scrapping tool which just makes everything more difficult)

# Also, I can scrap data during the summer months and after learning Python and R, can re-run the analysis of data. See if this can be optimised, MAYBE.

# How to start a new debugger Chrome page in cmd - start chrome.exe --remote-debugging-port=1991 --user-data-dir="C:\Users\Adeniyi Babalola\Desktop\PythonPrograms\chromedata"

import re
from re import T, search
import click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pandas as pd
import openpyxl
from openpyxl import Workbook
import time
import csv

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:1991")

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",chrome_options=opt)
# driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

# Maximise the window once it opens before loading the page
# driver.maximize_window()

# Go to the login page of FFHub and immediately reload to OPTA page if login is successful
# driver.get("https://www.fantasyfootballhub.co.uk/login?r=/opta")

# Wait for the page to be done loading incase internet is slow
# time.sleep(5)

# Click on the cookie button if it is popping up
# i = driver.find_element_by_id("rcc-confirm-button").click()

# Enter email and password to login and automatically press enter
# search = driver.find_element_by_id("email")
# search.send_keys("hardboyvino")
# search = driver.find_element_by_id("password")
# search.send_keys("uAzux$DUO6X7(%c2")
# search.send_keys(Keys.RETURN)

# Wait for the page to be done loading incase internet is slow or CAPTA shows up to solve
# time.sleep(20)

#Change to PerApp Selection for Data Gathering
# perapp = driver.find_element_by_xpath("//input[@id='perapp']").click()

# Unclick the GK, Def and Mid Positions for Analysis
# gk_position = driver.find_element_by_xpath("//input[@id='gkp']").click()
# def_position = driver.find_element_by_xpath("//input[@id='def']").click()
# mid_position = driver.find_element_by_xpath("//input[@id='mid']").click()

# So that I can change the sliders to the right GW
# time.sleep(20)

# Load all players for whatever option/page we are on
# select = Select(driver.find_element_by_id("qty"))
# select.select_by_value("99999")

# Wait for the page to be done loading incase internet is slow
# time.sleep(10)

# ##############################################################
# ####### Move the sliders for 3GWs - MAYVBE DELETE #############
# ##############################################################
# # slider1 = driver.find_element_by_xpath('//div/div[2]/div[2]/div[2]/div/div/div[2]/section/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/span/span[3]/span/span/span')
# # slider2 = driver.find_element_by_xpath('//div/div[2]/div[2]/div[2]/div/div/div[2]/section/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/span/span[4]')
# # ActionChains(driver).click_and_hold(slider1).drag_and_drop(270, 0).release(slider1).perform()


stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[1]')
stat_type.click()
time.sleep(5)

# # This is where the data scrapping comes to life. Gather all the other columns and the turn the ones not required to comments
# playerNames = driver.find_elements(by=By.XPATH, value='//tbody/tr/td/div/a')
playerNames = driver.find_elements(by=By.XPATH, value='//tbody/tr')
# playerTeams = driver.find_elements(by=By.XPATH, value='//tbody/tr/td/div/div/span')
# playerPrice = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[2]')
# playerAppearances = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[3]')
# playerMinutes = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[4]')
# playerShot = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerOT = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerIn = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerBC = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerxG = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerG = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
# playerPercentxGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
# playerPercentGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')
# playerxGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[13]')
# playerGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[14]')
# playerKP = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[15]')
# playerBCC = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[16]')
# playerxAssist = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[17]')
# playerAssists = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[18]')
# playerxPts = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[19]')
# playerBPS = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[20]')
# playerB = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[21]')
# playerPts = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[22]')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[2]')
stat_type.click()
time.sleep(5)
playerNames2 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[3]')
stat_type.click()
time.sleep(5)
playerNames3 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[4]')
stat_type.click()
time.sleep(5)
playerNames4 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[5]')
stat_type.click()
time.sleep(5)
playerNames5 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[6]')
stat_type.click()
time.sleep(5)
playerNames6 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[7]')
stat_type.click()
time.sleep(5)
playerNames7 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[8]')
stat_type.click()
time.sleep(5)
playerNames8 = driver.find_elements(by=By.XPATH, value='//tbody/tr')

stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[9]')
stat_type.click()
time.sleep(5)
playerNames9 = driver.find_elements(by=By.XPATH, value='//tbody/tr')
# appearances = driver.find_elements_by_xpath('//tbody/tr/td[3]')

# Create the fpl_data dictionary
fpl_data = []

# For the length of all the players available, put them in the fpl_data dictionary. But I have realised you can run calculations straight from here as well which is AMAZING!!!
for i in range(len(playerNames)):
    temp_data = {
            'Name': re.split(' |\n',playerNames[i].text),
            'Name2': re.split(' |\n',playerNames2[i].text),
            'Name3': re.split(' |\n',playerNames3[i].text),
            'Name4': re.split(' |\n',playerNames4[i].text),
            'Name5': re.split(' |\n',playerNames5[i].text),
            'Name6': re.split(' |\n',playerNames6[i].text),
            'Name7': re.split(' |\n',playerNames7[i].text),
            'Name8': re.split(' |\n',playerNames8[i].text),
            'Name9': re.split(' |\n',playerNames9[i].text)
            # 'Team Name': playerTeams[i].text,
            # 'Price': float(playerPrice[i].text.replace("£","")),
            # 'Minutes': float(playerMinutes[i].text),
            # 'Appearances': playerAppearances[i].text,
            # 'Shots': float(playerShot[i].text),
            # 'On Target': float(playerOT[i].text),
            # 'Shots in Box': float(playerIn[i].text),
            # 'Big Chances': float(playerBC[i].text),
            # 'Expected Goals': float(playerxG[i].text),
            # 'Goals': float(playerG[i].text),
            # '%%xGI': (float(playerPercentxGI[i].text.replace("%",'')) / 100),
            # '%%GI': (float(playerPercentGI[i].text.replace("%",'')) / 100),
            # 'xGI': float(playerxGI[i].text),
            # 'Goal Involvement': float(playerGI[i].text),
            # 'Key Passes': float(playerKP[i].text),
            # 'Big Chances Created': float(playerBCC[i].text),
            # 'Expected Assists': float(playerxAssist[i].text),
            # 'Assists': float(playerAssists[i].text),
            # 'Expected Points': float(playerxPts[i].text),
            # 'BPS': float(playerBPS[i].text),
            # 'Bonus Points': float(playerB[i].text),
            # 'Points': float(playerPts[i].text),
            # 'Predicted Points': (float(playerPrice[i].text.replace("£","")) * 1000) + (float(playerxG[i].text) * 3)
    }
    fpl_data.append(temp_data)

# #Print out only the columns Names and Points and 'drops' all columns named
data = pd.DataFrame(fpl_data)
# df = data.drop(columns=['Team Name', 'Minutes'])
# df = data.drop(columns=['Team Name', 'Minutes'])
# print(df)
# print(data)

# # Turn the panda into an excel file
data.to_csv('fpl.csv', index = False)

read_file = pd.read_csv('fpl.csv')
read_file.to_excel('fpl_new.xlsx', index = False)