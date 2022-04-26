from calendar import month
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import json
import time

chromedriver = Service('chromedriver.exe')
browser = webdriver.Chrome(service=chromedriver)


class tools:
    def create_account(login, password, recovery):
        browser.get("https://int.pl/#/register")
        print(f"Creating account with {login}, {password}, {recovery}")

        login_field = browser.find_element_by_xpath('//*[@id="loginId"]')
        login_field.send_keys(login)

        #error_field = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/section/div[2]/div/div/div[1]/form[2]/div[1]/div[1]/div[3]/div/span[3]')))
        #print(error_field.get_attribute('textContent'))
        #if error_field.get_attribute('textContent') == "Zajęty":
        #    print("Zajęty")
        #else:
        #     print("Wyglada na wolne")

        password_field = browser.find_element_by_xpath('//*[@id="passwordId"]')
        password_confirm_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[3]/input')
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)

        recovery_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[4]/input')
        recovery_field.send_keys(recovery)

        day_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[5]/div[1]/input[1]')
        month_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[5]/div[1]/input[2]')
        year_field = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[5]/div[1]/input[3]')
        day_field.send_keys("01")
        month_field.send_keys("01")
        year_field.send_keys("2000")

        gender_button = browser.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[1]/form[2]/div[6]/label[2]')
        gender_button.click()

        terms_checkbox = browser.find_element_by_xpath('//*[@id="ng-app"]/body/section[1]/div[2]/div/div/div[1]/form[2]/div[7]/div[1]/label')
        terms_checkbox.click()
        
        