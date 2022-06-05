from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep, strftime
from random import randint
import datetime


def main():
    # Page is preopened with OPTA Page loaded
    chrome_options = ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:1991")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    url = "https://www.fantasyfootballhub.co.uk/opta"


def scrape_players_and_teams(driver, wait):

    # Read the page source
    html = driver.page_source

    # Create panda DataFrames for all possible tables on the HTML page
    df = pd.read_html(html)

    # For easy selection of the 1st table (In my case the only table)
    data = df[0]

    # Split the Name column into Name, Position and Team.
    # Has to be done in 2 different batches
    data[["Names", "Position"]] = data["Name"].str.split("(", expand=True)
    data[["Position", "Team"]] = data["Position"].str.split(")", expand=True)

    # Do not show the first column when print the DataFrame on VSCode, although the column still exists when exported to Excel or CSV
    # data = data.iloc[:, 1:]

    # Instead of just hiding the column, totally drop it so it is not even in the CSV or Excel
    # data = data.drop(columns=data.columns[0], axis=1, inplace=True)

    # Remove all instances of % and £ in the DataFrame
    data = data.replace(regex=["%"], value=[""])
    data = data.replace(regex=["£"], value=[""])

    random_sleeps()

    team_data_type(driver, wait)

    """Converts a team's long name to their short name."""
    team_name_conversion = {
        "Arsenal": "ARS",
        "Aston Villa": "AVL",
        "Brentford": "BRE",
        "Brighton": "BHA",
        "Burnley": "BUR",
        "Bournemouth": "BOU",
        "Cardiff": "CAR",
        "Chelsea": "CHE",
        "Crystal Palace": "CRY",
        "Everton": "EVE",
        "Fulham": "FUL",
        "Huddersfield": "HUD",
        "Leicester": "LEI",
        "Leeds": "LEE",
        "Liverpool": "LIV",
        "Man City": "MCI",
        "Man Utd": "MUN",
        "Newcastle": "NEW",
        "Norwich": "NOR",
        "Sheffield Utd": "SHU",
        "Southampton": "SOU",
        "Spurs": "TOT",
        "Watford": "WAT",
        "West Brom": "WBA",
        "West Ham": "WHU",
        "Wolves": "WOL",
        None: None,
    }

    team_html = driver.page_source

    dp = pd.read_html(team_html)

    teams = dp[0]

    teams.rename(columns={"Name": "Team"}, inplace=True)

    # Replace all the team names so they match up
    for word, replacement in team_name_conversion.items():
        teams = teams.replace(regex=[word], value=[replacement])

    combined = data.merge(teams, how="left", on="Team")

    print(combined)

    combined.to_excel(f"Players & Teams Combined Scrape - {strftime('%a %d %b %Y %H %M %S %p')}.xlsx", index=False)


def scrape_players(driver):
    # Read the page source 
    html = driver.page_source

    # Create panda DataFrames for all possible tables on the HTML page
    df = pd.read_html(html)

    # For easy selection of the 1st table (In my case the only table)
    data = df[0]

    # Split the Name column into Name, Position and Team.
    # Has to be done in 2 different batches
    data[["Names", "Position"]] = data["Name"].str.split("(", expand=True)
    data[["Position", "Team"]] = data["Position"].str.split(")", expand=True)

    # Do not show the first column when print the DataFrame on VSCode, although the column still exists when exported to Excel or CSV
    # data = data.iloc[:, 1:]

    # Instead of just hiding the column, totally drop it so it is not even in the CSV or Excel
    # data = data.drop(columns=data.columns[0], axis=1, inplace=True)

    # Remove all instances of % and £ in the DataFrame
    data = data.replace(regex=["%"], value=[""])
    data = data.replace(regex=["£"], value=[""])

    print(data)

    data.to_excel(f"Players Only Scrape - {strftime('%a %d %b %Y %H %M %S %p')}.xlsx", index=False)


def maximize_window(driver):
    driver.maximize_window()

    random_sleeps()

def load_all_players(driver, wait):
    driver.find_element(By.CSS_SELECTOR, "div[class='my-4'] div[class=' css-r71ql9-singleValue']").click()

    # Load all possible players
    load_all = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'All (slow)')]")
        )
    )

    load_all.click()

    sleep(20)

def click_per90(driver):
    driver.find_element(By.CSS_SELECTOR, "#per90").click()

def click_per_start(driver):
    driver.find_element(By.CSS_SELECTOR, "#perstart").click()

def click_perapp(driver):
    driver.find_element(By.CSS_SELECTOR, "#perapp").click()

def team_data_type(driver, wait):
    # this will click dropdown for data type
    try: 
        driver.find_element(
            By.XPATH, value="//div[contains(text(),'Players')]"
        ).click()

    except:
        driver.find_element(By.XPATH, value="//div[contains(text(),'Teams')]").click()  

    # Click on Player option
    teams = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Teams')]"))
    )

    teams.click()

    random_sleeps()

def player_data_type(driver, wait):
    # this will click dropdown for data type
    driver.find_element(
        By.XPATH, value="(//div)[132]"
    ).click()

    # Click on Player option
    player = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[contains(text(),'Players')]")
        )
    )

    player.click()

    random_sleeps()


def stat_type_custom(driver, wait):
    """
    This function goes into the Stat Type option and selects Custom
    """
    # this will click dropdown for stat types
    driver.find_element(
        By.XPATH, value="(//div[contains(@class,'css-seq4h5-control')])[3]"
    ).click()

    random_sleeps()

    # Click on Custom option
    custom = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Custom')]"))
    )

    custom.click()

    random_sleeps()

    # Click Save button for the custom selections
    driver.find_element(By.XPATH, value="//button[normalize-space()='Save']").click()

    random_sleeps()

def random_sleeps():
    sleep(randint(5, 7))


if __name__ == "__main__":
    main()
