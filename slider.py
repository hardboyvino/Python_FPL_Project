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
    position = input("Which position to scrape(gk, def, mid or fwd): ")


    if position == "gk":
        goalkeeper_scrape()

    elif position == "def":
        defender_scrape()

    elif position == "mid":
        midfielder_scrape()

    elif position == "fwd":
        forward_scrape()

    else:
        print("Pick a valid option")

def goalkeeper_scrape():
    # Get the pixels of the slider per GW
    slider_width = int(input("What is the width of the slider: "))
    total_gw = int(input("How many GWs so far: "))
    pixels_per_gw = slider_width / (total_gw - 1)
    gws_to_consider = 2
    predict_lookahead = 3 # How many GWs to use in prediction points scrapping
    position = "gk"

    # Click on the perApp button
    driver.find_element(By.ID, "perapp").click()

    # Load all players for whatever option/page we are on
    Select(driver.find_element(By.ID, "qty")).select_by_value("99999")

    # # Wait for the page to be done loading incase internet is slow
    time.sleep(10)

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
    move_slider(slider_1, slider_2, pixels_per_gw, predict_lookahead, position)

def defender_scrape():
    # Get the pixels of the slider per GW
    slider_width = int(input("What is the width of the slider: "))
    total_gw = int(input("How many GWs so far: "))
    pixels_per_gw = slider_width / (total_gw - 1)
    gws_to_consider = 2
    predict_lookahead = 3 # How many GWs to use in prediction points scrapping
    position = "def"

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
    move_slider(slider_1, slider_2, pixels_per_gw, predict_lookahead, position)

def midfielder_scrape():
    # Get the pixels of the slider per GW
    slider_width = int(input("What is the width of the slider: "))
    total_gw = int(input("How many GWs so far: "))
    pixels_per_gw = slider_width / (total_gw - 1)
    gws_to_consider = 2
    predict_lookahead = 3 # How many GWs to use in prediction points scrapping
    position = "mid"

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
    move_slider(slider_1, slider_2, pixels_per_gw, predict_lookahead, position)

def forward_scrape():
    # Get the pixels of the slider per GW
    slider_width = int(input("What is the width of the slider: "))
    total_gw = int(input("How many GWs so far: "))
    pixels_per_gw = slider_width / (total_gw - 1)
    gws_to_consider = 2
    predict_lookahead = 3 # How many GWs to use in prediction points scrapping
    position = "fwd"

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
    move_slider(slider_1, slider_2, pixels_per_gw, predict_lookahead, position)


def move_slider(slide1, slide2, pixels, predict, position):
    current_gw = "1" # Initialise to 1

    while current_gw < "33":
        # Get Key Stats Page
        stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[1]').click()

        time.sleep(10)

        # Get all the rows for Key Stats
        playerNames = driver.find_elements(by=By.XPATH, value='//tbody/tr/td/div/a')
        playerTeams = driver.find_elements(by=By.XPATH, value='//tbody/tr/td/div/div/span')
        playerPrice = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[2]')
        playerAppearances = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[3]')
        playerMinutes = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[4]')
        playerShot = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
        playerOT = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
        playerIn = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
        playerBC = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
        playerxG = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
        playerG = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
        playerPercentxGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
        playerPercentGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')
        playerxGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[13]')
        playerGI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[14]')
        playerKP = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[15]')
        playerBCC = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[16]')
        playerxAssist = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[17]')
        playerAssists = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[18]')
        playerxPts = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[19]')
        playerBPS = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[20]')
        playerB = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[21]')
        playerPts = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[22]')

        # Create the fpl_data dictionary
        fpl_data = []

        # For the length of all the players available, put them in the fpl_data dictionary. But I have realised you can run calculations straight from here as well which is AMAZING!!!
        for i in range(len(playerNames)):
            temp_data = {
                        'Name': playerNames[i].text,
                        'Team Name': playerTeams[i].text,
                        'Price': float(playerPrice[i].text.replace("£","")),
                        'Minutes': float(playerMinutes[i].text),
                        'Appearances': playerAppearances[i].text,
                        'Shots': float(playerShot[i].text),
                        'On Target': float(playerOT[i].text),
                        'Shots in Box': float(playerIn[i].text),
                        'Big Chances': float(playerBC[i].text),
                        'Expected Goals': float(playerxG[i].text),
                        'Goals': float(playerG[i].text),
                        '%%xGI': (float(playerPercentxGI[i].text.replace("%",''))) / 100,
                        '%%GI': (float(playerPercentGI[i].text.replace("%",''))) / 100,
                        'xGI': float(playerxGI[i].text),
                        'Goal Involvement': float(playerGI[i].text),
                        'Key Passes': float(playerKP[i].text),
                        'Big Chances Created': float(playerBCC[i].text),
                        'Expected Assists': float(playerxAssist[i].text),
                        'Assists': float(playerAssists[i].text),
                        'Expected Points': float(playerxPts[i].text),
                        'BPS': float(playerBPS[i].text),
                        'Bonus Points': float(playerB[i].text),
                        'Points': float(playerPts[i].text)
            }
            fpl_data.append(temp_data)

        time.sleep(10)

        # Move the sliders forward for the predict scrapping
        ActionChains(driver).drag_and_drop_by_offset(slide2, (pixels * predict), 0).perform()
        time.sleep(5)
        ActionChains(driver).drag_and_drop_by_offset(slide1, (pixels * predict), 0).perform()
        time.sleep(5)



        # Get the future points
        playerNames = driver.find_elements(by=By.XPATH, value='//tbody/tr/td/div/a')
        playerPtsPredict = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[22]')

        # Create the fpl_data dictionary
        fpl_data2 = []

        # For the length of all the players available, put them in the fpl_data dictionary. But I have realised you can run calculations straight from here as well which is AMAZING!!!
        for i in range(len(playerNames)):
            temp_data2 = {
                        'Name': playerNames[i].text,
                        'PointsPredict': float(playerPtsPredict[i].text)
            }
            fpl_data2.append(temp_data2)        
        time.sleep(10)

        # Move sliders back to original positon
        ActionChains(driver).drag_and_drop_by_offset(slide1, -(pixels * predict), 0).perform()
        time.sleep(5)
        ActionChains(driver).drag_and_drop_by_offset(slide2, -(pixels * predict), 0).perform()
        time.sleep(5)

        # Turn the fpl_data into Panda DataFrame
        data = pd.DataFrame(fpl_data)
        data2 = pd.DataFrame(fpl_data2)

        # Merge all the dataFrames using the Name column to match the data across dataFrames 
        dataAll = data.merge(data2, how='left', on='Name')

        # Fill all blanks in the dataframe with zeros so the results don't return NaN
        dataAll.fillna(0, inplace=True)

        # Turn the panda into an excel file
        if position == "gk":
            dataAll.to_excel('fpl_goalkeeper.xlsx', index = False)

        elif position == "def":
            dataAll.to_excel('fpl_defenders.xlsx', index = False)

        elif position == "mid":
            dataAll.to_excel('fpl_midfielders.xlsx', index = False)

        elif position == "fwd":
            dataAll.to_excel('fpl_forward.xlsx', index = False)


        # Get the current GW for while loop
        current_gw = driver.find_element(by=By.XPATH, value='//*[@id="__next"]//div[2]/div[2]/span/span[4]/span/span/span').text
        time.sleep(5)

        # Move lower slider to appropraite GW for the scrapping
        ActionChains(driver).drag_and_drop_by_offset(slide2, pixels, 0).perform()
        time.sleep(5)
        ActionChains(driver).drag_and_drop_by_offset(slide1, pixels, 0).perform()
        time.sleep(5)


main()