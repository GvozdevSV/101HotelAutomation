import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CromeServise
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=CromeServise(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
