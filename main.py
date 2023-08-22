from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import json
from Modules.login import *
from Modules.open_rozvrh import *
from Modules.open_page import *
from Modules.convert import *


driver = webdriver.Edge()
openPage(driver)
login(driver)
driver.maximize_window()
openRozvrh(driver)
driver.close()

csv_to_json(csvFile, jsonFile)