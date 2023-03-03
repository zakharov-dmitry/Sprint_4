import pytest
from selenium.webdriver.firefox import webdriver


@pytest.fixture()  # creates driver instance for firefox
def create_firefox_driver():
    driver = webdriver.WebDriver()
    driver.maximize_window()
    return driver
