from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

def openRozvrh(driver):

    elem = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/input")) #pole pro semestr
    elem.clear()
    elem.send_keys("léto 2022/2023")
    elem.send_keys(Keys.RETURN)

    time.sleep(25)      #moznost elegantnejsiho reseni?

    elem = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[2]/div[2]/button[3]").click()       #tlacitko dole na export CSV souboru

    time.sleep(15)
