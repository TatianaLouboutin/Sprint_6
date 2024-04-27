from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
import allure
from locators.locators import ScooterLocators
from pages.base_page import BasePageScooter


class HomePageScooter(BasePageScooter):

    def find_questions(self, driver):
       self.agree_with_coockie(driver)
       self.scroll_to_locator(driver, ScooterLocators.one_question)








