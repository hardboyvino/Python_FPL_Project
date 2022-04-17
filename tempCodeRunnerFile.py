while():
    from tkinter.tix import Select
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from selenium.webdriver.common.by import By

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

    time.sleep(5)

    driver.quit()