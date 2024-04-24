import pytest
from selenium import webdriver
import settings


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(settings.URL)

    yield firefox_driver

    firefox_driver.quit()

@pytest.fixture(scope='function')
def driver2():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(settings.URL_ORDER)

    yield firefox_driver

    firefox_driver.quit()

