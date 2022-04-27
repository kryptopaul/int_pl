from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

chromedriver = Service('chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=chromedriver, options=chrome_options)

class tools:
    def create_account(login, password, recovery):
        #Generates and appends a random number
        random_append = random.randint(0, 999999)
        login = login + str(random_append)
        browser.get("https://int.pl/#/register")
        print(f"Creating account with {login}@int.pl, {password}, {recovery}")

        #Fill in Login (email)
        login_field = browser.find_element_by_id('loginId')
        login_field.send_keys(login)

        #Fill in Password
        password_field = browser.find_element_by_xpath('//*[@id="passwordId"]')
        password_confirm_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[3]/input')
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)

        #Fill in Recovery
        recovery_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[4]/input')
        recovery_field.send_keys(recovery)

        #Fill in Date
        day_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[5]/div[1]/input[1]')
        month_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[5]/div[1]/input[2]')
        year_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[5]/div[1]/input[3]')
        day_field.send_keys("01")
        month_field.send_keys("01")
        year_field.send_keys("2000")

        #Select Gender
        gender_button = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[6]/label[2]')
        gender_button.click()
        
        # Accept Terms of Service
        browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="portalRulesId"]'))))
            
        # Submit the form (time.sleep used since the script behind the button doesn't load on time despite the button being visible)
        time.sleep(2)
        submit_button = browser.find_element_by_xpath('//*[@id="ng-app"]/body/section[1]/div[2]/div/div/div[1]/form[2]/button[1]')
        submit_button.click()
        
        #Checks if success
        try:
            success_msg = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div[2]/div/div/div[1]/form[2]/div[1]/div/label')))
            if success_msg.get_attribute('textContent') == "Twoje konto pocztowe zostało założone":
                print(f"Successfully created {login}@int.pl:{password}")
                browser.delete_all_cookies()
                browser.refresh()
        except:
            print("Error")        

        # while True:
        #     continue
        
        