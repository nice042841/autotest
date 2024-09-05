# utils.py
import allure
import random
import os
import uuid
import pytest, time, json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(scope="class")
def browser(request):
    mobile_emulation = {"deviceName": "iPhone 14 Pro Max"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
   
    service = Service(r"C:\H5_With Json\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    url = request.param
    driver.get(url)
    driver.implicitly_wait(5)
    
    # Handle 403 Forbidden status
    max_attempts = 5
    for attempt in range(max_attempts):
        if "403 Forbidden" in driver.page_source:
            print(f"檢測到 403 Forbidden，正在刷新頁面... 嘗試 {attempt + 1}")
            driver.refresh()
            time.sleep(6)  # 等待頁面刷新
        else:
            break
    else:
        raise Exception("達到最大刷新嘗試次數，仍然遇到 403 Forbidden 狀態。")

    yield driver
    driver.quit()




@pytest.fixture(scope="class")
def LoginBrowser(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatest01")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser



@pytest.fixture(scope="class")
def LoginBrowser_MY(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "nice042841")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "jay02714")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser
    
@pytest.fixture(scope="class")
def LoginBrowser_TH(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatest02")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_ID(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatest03")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_HI(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatestinr")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_VN(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatestvvnd")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_USD(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatestusd")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_BD(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "qatestbdt")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_CS(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "rqatestcny")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1q2w3e4r")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_KH(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "aitestkhusd01")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "1qaz2wsx")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_BR(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "ricktestbr01")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "jay02714")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

@pytest.fixture(scope="class")
def LoginBrowser_KR(browser):
    interactions = Interactions(browser)
    interactions.enter_text(By.CSS_SELECTOR, CS["login_username"], "ricktestkr")
    interactions.enter_text(By.CSS_SELECTOR, CS["login_password"], "jay02714")
    interactions.click_button(By.XPATH, xpaths["login_btn"])
    return browser

def load_json(json_file_path):
    json_file_path = os.path.join(os.path.dirname(__file__), 'element_json', 'Nova88_H5.json')
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

CS = load_json("Nova88_H5.json")["css_selectors"]
urls = load_json("Nova88_H5.json")["urls"]
xpaths =load_json("Nova88_H5.json")["XPaths"]

def load_json_header(json_file_path):
    json_file_path = os.path.join(os.path.dirname(__file__), 'element_json', 'N88 Header data.json')
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data



class Interactions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        

    def refresh(self, max_refresh_attempts = 10):
        refresh_attempts = 0
        while self.browser.title == "403 Forbidden" and refresh_attempts < max_refresh_attempts:
            print(f"403 Forbidden detected, refreshing the page... Attempt {refresh_attempts + 1}")
            self.browser.refresh()
            time.sleep(10)
            refresh_attempts += 1
        
    def wait_for_page_load(self, driver, timeout=10):
        WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    def click_button(self, by, locator):
        btn = self.wait.until(EC.element_to_be_clickable((by, locator)))
        btn.click()
        time.sleep(0.2)

    def page_down(self):
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    def page_end(self):
        body = self.browser.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.END)
        time.sleep(1)

    def page_close(self):
        self.browser.close()
        time.sleep(1)

    def page_switch(self, num):
        handles = self.browser.window_handles
        if num < len(handles):
            self.browser.switch_to.window(handles[num])
            time.sleep(1)
        else:
            raise IndexError(f"Window handle index {num} is out of range. There are only {len(handles)} handles available.")


    def element_display(self, by, locator):
        element = self.browser.find_element(by, locator)
        return element.is_displayed()

    def get_msg(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element.text
        except TimeoutException:
            print(f"Element not found: {by}, {locator}")
            self.driver.save_screenshot(f"timeout_{locator}.png")
            raise

    def switch_handle(self):
        current_handle = self.browser.current_window_handle
        self.wait.until(EC.number_of_windows_to_be(2))
        all_handles = self.browser.window_handles
        new_window_handle = next(iter(set(all_handles) - set([current_handle])))
        self.browser.switch_to.window(new_window_handle)

    def switch_iframe(self, by, locator):
        iframe = self.browser.find_element(By.TAG_NAME, "iframe")
        self.browser.switch_to.frame(iframe)
        element  = self.wait.until(EC.presence_of_element_located((by, locator)))
        return element

    def select_option_by_click(self, by, locator, option_text):
        dropdown_button = self.driver.find_element(by, locator)
        dropdown_button.click()
        option_locator = (By.XPATH, f"//button[contains(text(), '{option_text}')]")
        option = self.driver.find_element(*option_locator)
        option.click()

    def enter_text(self, by, locator, text):
        element = self.wait.until(EC.presence_of_element_located((by, locator)))
        element.clear()
        time.sleep(3)
        element.send_keys(text)
    
    def generate_phone_number_my(self):
        return ''.join(random.choices('0123456789', k=9))
    
    def generate_phone_number_th(self):
        return ''.join(random.choices('0123456789', k=9))
    
    def generate_phone_number_id(self):
        return ''.join(random.choices('0123456789', k=13))
    
    def generate_phone_number_hi(self):
        return ''.join(random.choices('0123456789', k=10))
    
    def generate_phone_number_vn(self):
        return ''.join(random.choices('0123456789', k=9))
    
    def generate_phone_number_bd(self):
        return ''.join(random.choices('0123456789', k=11))
    
    def generate_phone_number_kh(self):
        return ''.join(random.choices('0123456789', k=8))
    
    def generate_phone_number_ch(self):
        return ''.join(random.choices('0123456789', k=10))
    
    def generate_phone_number_kr(self):
        return ''.join(random.choices('0123456789', k=9))
    
    def generate_phone_number_br(self):
        return ''.join(random.choices('0123456789', k=11))
    

    
    # 流水號 
    def generate_unique_username(self, base_name="rickauto"):
        counter = self._read_counter()
        username = f"{base_name}{counter:03d}"
        self._increment_counter()
        return username

    def _read_counter(self):
        try:
            with open("username_counter.txt", "r") as file:
                counter = int(file.read().strip())
        except FileNotFoundError:
            counter = 1
        return counter

    def _increment_counter(self):
        counter = self._read_counter() + 1
        with open("username_counter.txt", "w") as file:
            file.write(str(counter))

    def element_display_h5(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value))).is_displayed()
    
    
    def generate_unique_username_only(self, base_name="qaautotest"):
        counter = self._read_counter()
        username = f"{base_name}{counter:03d}"
        self._increment_counter()
        return username

    def _read_counter(self):
        try:
            with open("username_counter_only.txt", "r") as file:
                counter = int(file.read().strip())
        except FileNotFoundError:
            counter = 1
        return counter

    def _increment_counter(self):
        counter = self._read_counter() + 1
        with open("username_counter_only.txt", "w") as file:
            file.write(str(counter))
            
    def get_elements(self, by, selector):
        return self.driver.find_elements(by, selector)
    
# 直接抓 dropdonw 所有遊戲
    def check_game_list_print(self, category_xpath, expected_games):
        game_list_div = self.wait.until(
            EC.presence_of_element_located((By.XPATH, category_xpath))
        )
        
        game_buttons = game_list_div.find_elements(By.CSS_SELECTOR, '.gamelist-item')
        game_titles = [button.find_element(By.CSS_SELECTOR, '.gamelist-title').text for button in game_buttons]

        print("Game Titles:", game_titles)

        for game in expected_games:
            assert game in game_titles, f"Game '{game}' not found but got: {game_titles}"

    
    def check_game_list_img(self, category_xpath, expected_games,expected_url):
        try:
            game_list_div = self.wait.until(
            EC.presence_of_element_located((By.XPATH, category_xpath))
        )
        
            game_buttons = game_list_div.find_elements(By.CSS_SELECTOR, '.gamelist-item')
            game_titles = [button.find_element(By.CSS_SELECTOR, '.gamelist-title').text for button in game_buttons]
            game_imgs = [button.find_element(By.CSS_SELECTOR, '.gamelist-img img').get_attribute('src') for button in game_buttons]

            print("Game Titles:", game_titles)
            print("Game Image URLs:", game_imgs)

        # 驗證遊戲標題
            for game in expected_games:
                assert game in game_titles, f"Game '{game}' not found"

            # 構建預期的圖片 URL 後綴列表
            expected_suffixes = [f"{game.lower().replace(' ', '-')}.png" for game in expected_games]
            
            # 驗證圖片 URL 後綴
            for img_url in expected_url:
                if not any(img_url.endswith(suffix) for suffix in expected_suffixes):
                    raise AssertionError(f"URL {img_url} does not match any of the expected suffixes.")
            for url in game_imgs:
                image_displayed = self.check_image_displayed(url)
                assert image_displayed, f"Image '{url}' not displayed"
                
        except TimeoutException:
            print(f"TimeoutException: The element with XPath '{category_xpath}' was not found.")
    
    def check_image_displayed(self, image_url):
        current_window = self.driver.current_window_handle
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(image_url)

        status = False
        try:
            status = self.driver.execute_script("return document.readyState") == "complete"
        except Exception as e:
            print(f"Error checking image: {e}")

        self.driver.close()
        self.driver.switch_to.window(current_window)
        return status

        
        
# 驗證圖片
    def check_game_list_img1(self, category_xpath, expected_games):
        try:
            game_list_div = self.wait.until(
                EC.presence_of_element_located((By.XPATH, category_xpath))
            )
            time.sleep(2)  # 等待元素完全加载

            game_buttons = game_list_div.find_elements(By.CSS_SELECTOR, '.gamelist-item')
            game_titles = [button.find_element(By.CSS_SELECTOR, '.gamelist-title').text for button in game_buttons]
            game_image_urls = [button.find_element(By.CSS_SELECTOR, '.gamelist-img img').get_attribute('src') for button in game_buttons]
            expected_suffixes = [f"{game.lower().replace(' ', '-')}.png" for game in expected_games]

            print("Game Titles:", game_titles)
            print("Game Image URLs:", expected_suffixes)

            for game in expected_games:
                assert game in game_titles, f"Game '{game}' not found"

            for url in game_image_urls:
                image_displayed = self.check_image_displayed(url)
                assert image_displayed, f"Image '{url}' not displayed"
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="TimeoutException", attachment_type=allure.attachment_type.PNG)
            assert False, f"TimeoutException: Could not find element by XPath: {category_xpath}"

    def check_image_displayed(self, image_url):
        current_window = self.driver.current_window_handle
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(image_url)

        status = False
        try:
            status = self.driver.execute_script("return document.readyState") == "complete"
        except Exception as e:
            print(f"Error checking image: {e}")

        self.driver.close()
        self.driver.switch_to.window(current_window)
        return status
    
    def go_back(self):
        self.driver.back()

    def refresh_page(self):
        self.driver.refresh()
        
    
   
   
    
    
    