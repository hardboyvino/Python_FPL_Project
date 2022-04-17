# This is done considering only forwards. Might have to 'copy-pasta' for defs and midfielders. The issue now is sacked managers scrapping. Might have to do it organically (i.e. sliding and searching the club then running the scrapping tool which just makes everything more difficult)

# Also, I can scrap data during the summer months and after learning Python and R, can re-run the analysis of data. See if this can be optimised, MAYBE.

# How to start a new debugger Chrome page in cmd - start chrome.exe --remote-debugging-port=1991 --user-data-dir="C:\Users\Adeniyi Babalola\Desktop\PythonPrograms\chromedata"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait

# Use the Chrome with the localhost:1991
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:1991")
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options = opt)

# Load all players for whatever option/page we are on
# select = Select(driver.find_element_by_id("qty"))
# select.select_by_value("10")

# # Wait for the page to be done loading incase internet is slow
time.sleep(10)

# This is where the data scrapping comes to life. Gather all the other columns and the turn the ones not required to comments

# Get Key Stats Page
stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[1]')
stat_type.click()

time.sleep(20)
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody/tr/td[5]')))

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

# Get Goal Threat Page
stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[2]')
stat_type.click()
time.sleep(20)

# Get all the rows for Goal Threat
playerShotOutBox = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
playerHeadedShots = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
playerNPxG = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
playerGoalsInBox = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[14]')
playerGoalsOutBox = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[15]')
playerHeadedGoals = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[16]')

# # Get Creativity Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[3]')
# stat_type.click()
# time.sleep(10)

# # Get all the rows for Creativity
# playerFinal3rdPass = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerFinal3rdSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerPercentFinal3rdSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerCrosses = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerCrossesSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerPercentCrossesSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')

# # Get Passing Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[4]')
# stat_type.click()
# time.sleep(10)

# # Get all the rows for Passing
# playerPass = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerPassSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerPercentPassSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerOppHalfPass = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerOppHalfPassSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerPercentOppHalfPassSuccess = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
# playerTotThruBall = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[14]')
# playerAccThruBall = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[15]')

# # Get Involvement Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[5]')
# stat_type.click()
# time.sleep(10)

# # Get all the rows for Involvement
# playerTotalTouches = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerBoxTouches = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerFinal3rdEntries = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
# playerBoxEntries = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
# playerFinal3rdFouled = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')
# playerBoxFouled = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[13]')

# # Get Set Pieces Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[6]')
# stat_type.click()
# time.sleep(10)

# # Get all the rows for Set Pieces
# playerTotalCorners = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerCornerIntoBox = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerTotalFKIndirect = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerAccFKIndirect = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerTotalFKDirect = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerAccFKDirect = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
# playerTotalPenalties = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
# playerPenaltyGoals = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')

# # Get the Defending Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[7]')
# stat_type.click()
# time.sleep(10)

# # Get all the rows for Defending
# playerCleanSheet = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerGoalsConceded = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerTotalTackles = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerTacklesWon = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerPercentTackleAcc = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerDefensiveRecovery = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
# playerClearances = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
# playerBlocks = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')
# playerInterceptions = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[13]')
# playerCBI = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[14]')

# # Get the Defensive Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[8]')
# stat_type.click()
# time.sleep(10)

# # Get all the rows for Defensive
# playerShotsConceded = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerShotsConcededInBox = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerShotsConcededOT = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerSP = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[8]')
# playerHeadedShotsConceded = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[9]')
# playerBCConceded = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[10]')
# playerxGC = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
# playerxCS = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')

# # Get the FPL Data Page
# stat_type = driver.find_element(by=By.XPATH, value='//*[@id="stattype"]/option[9]')
# stat_type.click()
# time.sleep(10)

# # Gte all the rows for FPL Data
# playerSaves = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[5]')
# playerYellowCards = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[6]')
# playerRedCard = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[7]')
# playerThreat = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[11]')
# playerCreativity = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[12]')
# playerInfluence = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[13]')
# playerxAtt = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[14]')
# playerbBPS = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[16]')
# playeraPts = driver.find_elements(by=By.XPATH, value='//tbody/tr/td[19]')

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
                '%%xGI': (float(playerPercentxGI[i].text.replace("%",'')) / 100),
                '%%GI': (float(playerPercentGI[i].text.replace("%",'')) / 100),
                'xGI': float(playerxGI[i].text),
                'Goal Involvement': float(playerGI[i].text),
                'Key Passes': float(playerKP[i].text),
                'Big Chances Created': float(playerBCC[i].text),
                'Expected Assists': float(playerxAssist[i].text),
                'Assists': float(playerAssists[i].text),
                'Expected Points': float(playerxPts[i].text),
                'BPS': float(playerBPS[i].text),
                'Bonus Points': float(playerB[i].text),
                'Shots Outside Box':float(playerShotOutBox[i].text),
                'Headed Shots': float(playerHeadedShots[i].text),
                'NPxG': float(playerNPxG[i].text),
                'Goals In Box': float(playerGoalsInBox[i].text),
                'Goals from Outside Box': float(playerGoalsOutBox[i].text),
                'Headed Goals': float(playerHeadedGoals[i].text),
                # 'Final 3rd Passes': float(playerFinal3rdPass[i].text),
                # 'Final 3rd Successesful Passes': float(playerFinal3rdSuccess[i].text),
                # '%% Final 3rd Successful': (float(playerPercentFinal3rdSuccess[i].text.replace("%",'')) / 100),
                # 'Total Crosses': float(playerCrosses[i].text),
                # 'Successful Crosses': float(playerCrossesSuccess[i].text),
                # '%% Successful Crosses': (float(playerPercentCrossesSuccess[i].text.replace("%",'')) / 100),
                # 'Total Passes': float(playerPass[i].text),
                # 'Successful Passes': float(playerPassSuccess[i].text),
                # '%% Successful Passes': (float(playerPercentPassSuccess[i].text.replace("%",'')) / 100),
                # 'Opposition Half Passes': float(playerOppHalfPass[i].text),
                # 'Successful Opposition Half Passes': float(playerOppHalfPassSuccess[i].text),
                # '%% Successful Opposition Half Passes': (float(playerPercentOppHalfPassSuccess[i].text.replace("%",'')) / 100),
                # 'Total Throughballs': float(playerTotThruBall[i].text),
                # 'Accurate Throughballs': float(playerAccThruBall[i].text),
                # 'Total Touches': float(playerTotalTouches[i].text),
                # 'Touches in Box': float(playerBoxTouches[i].text),
                # 'Entries into Final 3rd': float(playerFinal3rdEntries[i].text),
                # 'Entries into Box': float(playerBoxEntries[i].text),
                # 'Fouled in Final 3rd': float(playerFinal3rdFouled[i].text),
                # 'Fouled in Box': float(playerBoxFouled[i].text),
                # 'Total Corners': float(playerTotalCorners[i].text),
                # 'Corners into Box': float(playerCornerIntoBox[i].text),
                # 'Total Indirect FK': float(playerTotalFKIndirect[i].text),
                # 'Accurate Indirect FK': float(playerAccFKIndirect[i].text),
                # 'Total Direct FK': float(playerTotalFKDirect[i].text),
                # 'Accurate Direct FK': float(playerAccFKDirect[i].text),
                # 'Total Penalties': float(playerTotalPenalties[i].text),
                # 'Penalty Goals': float(playerPenaltyGoals[i].text),
                # 'Cleansheet': float(playerCleanSheet[i].text),
                # 'Goals Conceded': float(playerGoalsConceded[i].text),
                # 'Total Tackles': float(playerTotalTackles[i].text),
                # 'Tackles Won': float(playerTacklesWon[i].text),
                # '%% Accurate Tackles': float(playerPercentTackleAcc[i].text),
                # 'Recovery': float(playerDefensiveRecovery[i].text),
                # 'Clearances': float(playerClearances[i].text),
                # 'Blocks': float(playerBlocks[i].text),
                # 'Interceptions': float(playerInterceptions[i].text),
                # 'CBI': float(playerCBI[i].text),
                # 'Shots Conceded': float(playerShotsConceded[i].text),
                # 'Shots Conceded In Box': float(playerShotsConcededInBox[i].text),
                # 'Shots Conceded OT': float(playerShotsConcededOT[i].text),
                # 'SP': float(playerSP[i].text),
                # 'Headed Shots Conceded': float(playerHeadedShotsConceded[i].text),
                # 'BC Conceded': float(playerBCConceded[i].text),
                # 'xGC': float(playerxGC[i].text),
                # 'xCS': float(playerxCS[i].text),
                # 'Saves': float(playerSaves[i].text),
                # 'Yellow Card': float(playerYellowCards[i].text),
                # 'Red Card': float(playerRedCard[i].text),
                # 'Threat': float(playerThreat[i].text),
                # 'Creativity': float(playerCreativity[i].text),
                # 'Influence': float(playerInfluence[i].text),
                # 'xAtt': float(playerxAtt[i].text),
                # 'bBPS': float(playerbBPS[i].text),
                # 'aPts': float(playeraPts[i].text),
                'Points': float(playerPts[i].text),
    }
    fpl_data.append(temp_data)

# Turn the fpl_data into Panda DataFrame
data = pd.DataFrame(fpl_data)

# print(data)

# Turn the panda into an excel file
data.to_excel('fpl.xlsx', index = False)