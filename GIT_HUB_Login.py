# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pyautogui

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)

def user_login(user_id,user_pw) :
    try :
        driver.get("https://github.com/")
        time.sleep(5)
    except :
        time.sleep(1)
        try :
            driver.get("https://github.com/")
        except :
            pyautogui.press('f5')
            time.sleep(1)
            try :
                driver.get("https://github.com/")
            except:
                print("Visit Git Hub WEB site Fail !!")
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/button').click()
    except :
        print("Click menu button fail")
    try :
        driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
    except :
        pyautogui.press('f5')
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/button/').click()
        except :
            print("Click menu button fail")
        try :
            driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        except :
            print("Can't Click Sign in button")
    try :
        driver.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(user_id)
    except :
        print("Can't find user id text field")
    try :
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(user_pw)
    except :
        print("Can't find user PW text field") 
    try :
        driver.find_element(By.XPATH, '//*[@id="login"]/form/div[3]/input[7]').click()
    except :
        print("Click Login button Fail")

user_id = "please change user id"
user_pw = "please change user pw"
user_login(user_id,user_pw)

