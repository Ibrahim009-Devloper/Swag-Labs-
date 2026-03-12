from selenium import webdriver
import pytest
from base_page.valid_login import valid_login
from utilities.read_propertice import read_config
from utilities.custom_logger import log_maker






class Test_valid_login():
    logger = log_maker.log_gen()
    def test_title_verification(self,setup):
        self.logger.info("******title verification has started*********")
        self.driver = setup
        self.driver.get(read_config.get_url())
        act_title = self.driver.title
        exp_title = "Swag Labs"
        assert act_title == exp_title,"Title is not matching "
        self.logger.info("********title verification has been ended*********")




    def test_valid_login(self,setup):
        self.logger.info("********valid login test case has started*********")
        self.driver = setup
        self.driver.get(read_config.get_url())
        self.login = valid_login(self.driver)
        self.login.fill_username_input_fild(read_config.get_username())
        self.login.fill_password_input_fild(read_config.get_password())
        self.login.click_login_btn()
        assert self.login.verifing_product_el_is_present().is_displayed,"Product page isn't displayed"
        self.logger.info("********valid login test case has finished*********")

    
       
        
