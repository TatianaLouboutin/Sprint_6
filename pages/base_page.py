from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
import allure
from locators.locators import ScooterLocators


class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Нажимаем кнопку Принять куки')
    def agree_with_coockie(self, driver):
        driver.find_element(*ScooterLocators.button_coockie).click()


    @allure.step('Скроллим страницу до локатора')
    def scroll_to_locator(self, driver, locator):
        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('Нажимаем лого Самокат')
    def click_link_scooter(self, driver):
        driver.find_element(*ScooterLocators.link_scooter).click()


    @allure.step('Нажимаем лого Яндекса')
    def click_link_logo(self, driver):
        driver.find_element(*ScooterLocators.link_yandex).click()





