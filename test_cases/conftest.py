import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




@pytest.fixture
def setup():
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    option.add_argument("--start-maximize")
    prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
}

    option.add_experimental_option("prefs", prefs)
    option.add_argument("--disable-features=PasswordLeakDetection")

    driver = webdriver.Chrome(options= option)
    yield driver

    driver.quit()