from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Add_product_to_cart():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)
        self.username_el = (By.ID,"user-name")
        self.password_el = (By.ID,"password")
        self.login_btn_el = (By.ID,"login-button")
        self.product_el_vrification = (By.XPATH,"//span[contains(@data-test,'title')]")
        self.all_product_add_to_cart_el = (By.XPATH,"//button[contains(text(),'Add to cart')]")
        self.click_cart_page_link_el = (By.XPATH,"//a[contains(@data-test,'shopping-cart-link')]")
        self.verifing_remove_el = (By.XPATH,"(//button[contains(text(),'Remove')])[1]")

    def login_page(self,username:str, password:str):
        user = self.wait.until(EC.visibility_of_element_located(self.username_el))
        user.clear()
        user.send_keys(username)

        pwd = self.wait.until(EC.visibility_of_element_located(self.password_el))
        pwd.clear()
        pwd.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.login_btn_el)).click()
    
    def verify_product_page_is_visiable(self):
        product_text = self.wait.until(EC.visibility_of_element_located(self.product_el_vrification))
        return product_text

    def add_all_product_to_cart(self):
        products_el = self.wait.until(EC.visibility_of_all_elements_located(self.all_product_add_to_cart_el))
        for product in products_el:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",product)
            product.click()
    

    def verify_product_added_sucessfully(self):
        # self.wait.until(EC.element_to_be_clickable(self.click_cart_page_link_el)).click()
        remove_el = self.wait.until(EC.visibility_of_element_located(self.verifing_remove_el))
        return remove_el


