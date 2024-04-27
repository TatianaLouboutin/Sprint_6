from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePageScooter
from locators.locators import ScooterLocators
import settings
import data
import allure


class OrderPageScooter(BasePageScooter):


    @allure.step('Нажимаем верхнюю кнопку Заказать')
    def click_home_button_order(self, driver):
        driver.find_element(*ScooterLocators.home_page_button_order).click()


    @allure.step('Нажимаем нижнюю кнопку Заказать')
    def click_home_button_order_lower(self, driver):
        BasePageScooter.scroll_to_locator(self, driver, ScooterLocators.home_page_button_order_lower)
        WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(ScooterLocators.home_page_button_order_lower))
        driver.find_element(*ScooterLocators.home_page_button_order_lower).click()


    @allure.step('Заполняем Имя')
    def fill_name(self, driver, name):
        driver.find_element(*ScooterLocators.name).send_keys(name)


    @allure.step('Заполняем Фамилию')
    def fill_surname(self, driver, surname):
        driver.find_element(*ScooterLocators.surname).send_keys(surname)


    @allure.step('Заполняем Адресс')
    def fill_adress(self, driver, adress):
        driver.find_element(*ScooterLocators.adress).send_keys(adress)


    @allure.step('Выбираем станцию метро Сокольники')
    def fill_metro_station(self, driver):
        input_metro = driver.find_element(*ScooterLocators.metro_input)
        input_metro.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ScooterLocators.metro_station))
        driver.find_element(*ScooterLocators.metro_station).click()


    @allure.step('Выбираем станцию метро Черкизовская')
    def fill_metro_station_2(self, driver):
        input_metro = driver.find_element(*ScooterLocators.metro_input)
        input_metro.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ScooterLocators.metro_station_2))
        driver.find_element(*ScooterLocators.metro_station_2).click()


    @allure.step('Заполняем поле Телефон')
    def fill_phone(self, driver, phone):
        driver.find_element(*ScooterLocators.phone).send_keys(phone)


    @allure.step('Нажимаем кнопку Далее')
    def click_button_futher(self, driver):
        driver.find_element(*ScooterLocators.button_futher).click()


    @allure.step('Выбираем дату 20 в датапикере')
    def fill_data_20(self, driver):
        driver.find_element(*ScooterLocators.data_input).click()
        driver.find_element(*ScooterLocators.date_20).click()


    @allure.step('Выбираем дату 23 в датапикере')
    def fill_data_23(self, driver):
        driver.find_element(*ScooterLocators.data_input).click()
        driver.find_element(*ScooterLocators.date_23).click()


    @allure.step('Выбираем одни сутки')
    def fill_time_one_day(self, driver):
        driver.find_element(*ScooterLocators.time_input).click()
        driver.find_element(*ScooterLocators.time_one_day).click()


    @allure.step('Выбираем двое суток')
    def fill_time_two_day(self, driver):
        driver.find_element(*ScooterLocators.time_input).click()
        driver.find_element(*ScooterLocators.time_two_day).click()


    @allure.step('Выбираем черный цвет самоката')
    def check_color_scooter_black(self, driver):
        driver.find_element(*ScooterLocators.color_scooter_black).click()


    @allure.step('Выбираем серый цвет самоката')
    def check_color_scooter_gray(self, driver):
        driver.find_element(*ScooterLocators.color_scooter_gray).click()


    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self, driver):
        driver.find_element(*ScooterLocators.button_order).click()


    @allure.step('Нажимаем кнопку Да')
    def click_button_yes(self, driver):
        driver.find_element(*ScooterLocators.button_yes).click()


    @allure.step('Нажимаем Посмотреть статус')
    def click_button_status(self, driver):
        driver.find_element(*ScooterLocators.button_see_status).click()


    @allure.step('Первый позитивный сценарий')
    def do_first_order(self, driver):
        self.click_home_button_order(driver)
        self.fill_name(driver, data.NAME_1)
        self.fill_surname(driver, data.SURNAME_1)
        self.fill_adress(driver, data.ADRESS_1)
        self.fill_metro_station(driver)
        self.fill_phone(driver, data.PHONE_NUMBER_1)
        self.click_button_futher(driver)
        self.fill_data_20(driver)
        self.fill_time_one_day(driver)
        self.check_color_scooter_black(driver)
        self.click_order_button(driver)
        self.click_button_yes(driver)


    @allure.step('Второй позитивный сценарий')
    def do_second_order(self, driver):
        self.click_home_button_order_lower(driver)
        self.fill_name(driver, data.NAME_2)
        self.fill_surname(driver, data.SURNAME_2)
        self.fill_adress(driver, data.ADRESS_2)
        self.fill_metro_station_2(driver)
        self.fill_phone(driver, data.PHONE_NUMBER_2)
        self.click_button_futher(driver)
        self.fill_data_23(driver)
        self.fill_time_two_day(driver)
        self.check_color_scooter_gray(driver)
        self.click_order_button(driver)
        self.click_button_yes(driver)