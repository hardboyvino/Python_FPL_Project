from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Use the Chrome with the localhost:1991
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:1991")
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe",options = opt)