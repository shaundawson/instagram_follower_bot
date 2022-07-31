import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from keys import CHROME_BINARY_LOC, CHROME_DRIVER_PATH, CHROME_PROFILE_PATH
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random


def pause():
    time_break = random.randint(4,9)
    return time.sleep(time_break)

class InstagramtFollowrBot:
    def __init__(self, CHROME_DRIVER_PATH):
        self.s=Service(executable_path=CHROME_DRIVER_PATH)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
        self.chrome_options.binary_location=(CHROME_BINARY_LOC)
        self.driver = webdriver.Chrome(service=self.s, options=self.chrome_options)
        
    def sign_in(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        pause()
        logged_in = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div/div/div[2]/div[2]/button")
        logged_in.click()
        
    def search(self):
        pass
            

bot = InstagramtFollowrBot(CHROME_DRIVER_PATH)
bot.sign_in()
bot.search()