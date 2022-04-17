count = 0 ## Initialise the counter

while(True):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from selenium.webdriver.common.by import By

    count += 1 # Add to counter everytime the loop runs

    # # Use the Chrome with the localhost:1991
    # opt = Options()
    # opt.add_experimental_option("debuggerAddress", "localhost:1991")
    # driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options = opt)

    # The location of my ChromeDriver
    chromedriver_path = "C:\Program Files (x86)\chromedriver.exe"

    # Create the ChromeOptions so I can have it always open in Incognito mode
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    # Use the driver to open up the website
    driver = webdriver.Chrome(options=options,executable_path=chromedriver_path)
    driver.get('https://www.premierleague.com/hall-of-fame/nominees')

    # Wait for the page to be done loading
    driver.implicitly_wait(15)
    # time.sleep(10)

    # Find the cookies button and accept it
    cookies = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[5]/button[1]').click()

    driver.implicitly_wait(5)
    # time.sleep(3)

    try:
        driver.implicitly_wait(5)
        # Close advert if any is showing
        advert = driver.find_element(by=By.XPATH, value='//*[@id="advertClose"]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Aguero & Select
        aguero = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[2]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Drogba & Select
        drogba = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[7]').click()
        
        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Scholes & Select
        scholes = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[17]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Yaya & Select
        yaya = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[20]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Ian & Select
        ian = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[25]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Vinny & Select
        vincent = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[12]').click()

        driver.implicitly_wait(5)
        # time.sleep(3)

        # Submit the vote
        submit = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[2]/button').click()

        time.sleep(4)

        # I want to know how many times the bot voted
        print(count)

        driver.quit()

    except:
        # Find Aguero & Select
        aguero = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[2]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Drogba & Select
        drogba = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[7]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Scholes & Select
        scholes = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[17]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Yaya & Select
        yaya = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[20]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Ian & Select
        ian = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[25]').click()

        driver.implicitly_wait(5)
        # time.sleep(5)

        # Find Vinny & Select
        vincent = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[1]/div[12]').click()

        driver.implicitly_wait(5)
        # time.sleep(3)

        # Submit the vote
        submit = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/section/section[3]/div[2]/button').click()

        time.sleep(4)

        # I want to know how many times the bot voted
        print(count)

        driver.quit()