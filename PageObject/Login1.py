import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Login2:
    def __init__(self, driver):
        self.driver = driver
        self.textbox_email = "formBasicEmail"
        self.textbox_pwd = "formBasicPassword"
        self.btn = "mt-4.btn.btn-primary"


    def input_email(self, email):
        self.driver.find_element(self.textbox_email).send_keys(email)

    def input_pwd(self, pwd):
        self.driver.find_element(self.textbox_pwd).send_keys(pwd)

    def click_btn(self):
        self.driver.find_element(By.CLASS_NAME, value="mt-4.btn.btn-primary").click()
        time.sleep(5)