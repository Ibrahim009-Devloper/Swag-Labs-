from selenium import webdriver
import pytest
from base_page.add_product_to_cart_page import Add_product_to_cart
from utilities.read_propertice import read_config
from utilities.custom_logger import log_maker

class Test_product_page():
    def test_add_to_cart(self,setup):
        self.driver = setup
        self.driver.get(read_config.get_url())
        self.add_to_cart = Add_product_to_cart(self.driver)
        self.add_to_cart.login_page(read_config.get_username(),read_config.get_password())
        assert self.add_to_cart.verify_product_page_is_visiable().is_displayed,"product page is not displayed"

        self.add_to_cart.add_all_product_to_cart()
        assert self.add_to_cart.verify_product_added_sucessfully().is_displayed(),"Added product number is not matching"
