from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import random


class Invalid_login():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)
        self.username_el = (By.ID,"user-name")
        self.password_el = (By.ID,"password")
        self.click_login_btn_el = (By.ID,"login-button")
        self.error_massage_el = (By.XPATH,"//h3[contains(@data-test,'error')]")

    def generate_rendom_username(self):
        lenth = 8
        username = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase,k=lenth))
        return username



    def invalid_login_email(self):
        user = self.wait.until(EC.visibility_of_element_located(self.username_el))
        user.clear()
        user.send_keys(self.generate_rendom_username())

    def generate_random_password(self):
        lenth = 8
        password = "".join(random.choices(string.punctuation + string.ascii_lowercase + string.digits,k=lenth))
        return password
    
    def invalid_login_password(self):
        pwd = self.wait.until(EC.visibility_of_element_located(self.password_el))
        pwd.clear()
        pwd.send_keys(self.generate_random_password())

    def click_login_btn_for_invalid_login(self):
        self.wait.until(EC.element_to_be_clickable(self.click_login_btn_el)).click()

    def error_massage(self):
        error_msg = self.wait.until(EC.visibility_of_element_located(self.error_massage_el))
        return error_msg