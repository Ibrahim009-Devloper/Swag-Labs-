import pytest
from selenium import webdriver
from base_page.invalid_login import Invalid_login
from utilities.read_propertice import read_config
from utilities.custom_logger import log_maker



class Test_invalid_login():
    logger = log_maker.log_gen()
    def test_invalid_login(self,setup):
        self.logger.info("*******invalid test case started*********")
        self.driver = setup
        self.driver.get(read_config.get_url())
        self.invalid_login = Invalid_login(self.driver)
        self.invalid_login.invalid_login_email()
        self.invalid_login.invalid_login_password()
        self.invalid_login.click_login_btn_for_invalid_login()
        assert self.invalid_login.error_massage().is_displayed(),"error massage not displayed"
        self.logger.info("********invalid test case finished**********")
        

