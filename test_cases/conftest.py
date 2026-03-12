import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




@pytest.fixture
def setup():
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    option.add_argument("--start-maximize")

    driver = webdriver.Chrome(options= option)
    yield driver

    driver.quit()