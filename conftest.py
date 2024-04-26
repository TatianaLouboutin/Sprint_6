import pytest
from selenium import webdriver
import settings


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(settings.URL)

    yield firefox_driver

    firefox_driver.quit()



