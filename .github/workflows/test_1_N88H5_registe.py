import pytest
import json
import uuid
import random
import os
import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from utils_stage import Interactions,time
from selenium.common.exceptions import TimeoutException

# Load JSON data
json_file_path = os.path.join(os.path.dirname(__file__), 'element_json', 'Nova88_H5.json')
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

CS = data["css_selectors"]
urls = data["urls"]
xpaths = data["XPaths"]

@pytest.fixture(scope="class")
def browser():
    mobile_emulation = {"deviceName": "iPhone 14 Pro Max"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
   
    service = Service(r"C:\H5_With Json\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("browser")

@allure.feature("Register Feature")
class TestRegister:
      
    @allure.story("Register Sucess Cases - Basic Info")
    def test_register_Success(self,browser):
        register =Interactions(browser)
        browser.get(urls["register_page"])
        time.sleep(15)
        unique_username = register.generate_unique_username()
        register.enter_text(By.CSS_SELECTOR, CS["register_username"], unique_username)
        register.enter_text(By.CSS_SELECTOR, CS["register_password"], "jay02714")
        register.enter_text(By.CSS_SELECTOR, CS["register_confirm"], "jay02714")
        register.enter_text(By.CSS_SELECTOR, CS["register_realname"], "rick")
        register.click_button(By.CSS_SELECTOR, CS["register_submit"])



    @allure.story("Register Sucess Cases - register done")
    def test_register_done(self,browser):
        register = Interactions(browser)
        time.sleep(15)
        register.click_button(By.XPATH, xpaths["register_currency"])  
        country_xpath = f'//div[contains(@class,"Join")]/form/div[2]/div/div[1]'
        register.click_button(By.XPATH, country_xpath)
        unique_phonenumber = register.generate_phone_number_my()
        register.enter_text(By.CSS_SELECTOR, CS["register_phone"], unique_phonenumber)
        submit_button = browser.find_element(By.XPATH, xpaths["register_submit_btn"])
        browser.execute_script("arguments[0].click();", submit_button)
        time.sleep(5)
            

if __name__ == "__main__":
    pytest.main(["--alluredir=./allure-results"])
    
    
