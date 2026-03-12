from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class valid_login():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)
        self.username_el = (By.ID,"user-name")
        self.password_el = (By.ID,"password")
        self.login_btn_el = (By.ID,"login-button")
        self.product_el_vrification = (By.XPATH,"//span[contains(@data-test,'title')]")


    def fill_username_input_fild(self,username:str):
        user = self.wait.until(EC.visibility_of_element_located(self.username_el))
        user.clear()
        user.send_keys(username)

    def fill_password_input_fild(self,Password:str):
        pwd = self.wait.until(EC.visibility_of_element_located(self.password_el))
        pwd.clear()
        pwd.send_keys(Password)

    def click_login_btn(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_btn_el))
        login_btn.click()


    def verifing_product_el_is_present(self):
        product_text = self.wait.until(EC.visibility_of_element_located(self.product_el_vrification))
        return product_text
