from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePageScooter
import settings
import data
import allure


class OrderPageScooter(HomePageScooter):
    home_page_button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]                            # Верхняя кнопка "Заказать"
    home_page_button_order_lower = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"] # Нижняя кнопка "Заказать"
    name = [By.XPATH, ".//input[@placeholder='* Имя']"]                                                        # Поле Имя
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]                                                 # Поле Фамилия
    adress = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]                               # Поле Адрес
    metro_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"]                                       # Поле ввода станции метро
    metro_station = [By.XPATH, ".//div[contains(text(), 'Сокольники')]"]                                       # Станция Сокольники
    metro_station_2 = [By.XPATH, ".//div[contains(text(), 'Черкизовская')]"]                                   # Станция Черкизовская
    phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]                          # Поле Телефон
    button_futher = [By.XPATH, ".//button[text()='Далее']"]                                                    # Кнопка Далее
    data_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]                               # Поле ввода даты начала аренды
    date_23 = [By.XPATH, ".//div[text()='23']"]                                                                # 23 число текущего месяца
    date_20 = [By.XPATH, ".//div[text()='20']"]                                                                # 20 число текущего месяца
    time_input = [By.XPATH, ".//div[text()='* Срок аренды']"]                                                  # Поле ввода длительности аренды
    time_one_day = [By.XPATH, ".//div[text()='сутки']"]                                                        # Одни сутки
    time_two_day = [By.XPATH, ".//div[text()='двое суток']"]                                                   # Двое суток
    color_scooter_black = [By.XPATH, ".//input[@id='black']"]                                                  # Чекбокс цвет: чёрный жемчуг
    color_scooter_gray = [By.XPATH, ".//input[@id='grey']"]                                                    # Чекбокс цвет: серая безысходность
    button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]                 # Кнопка заказа на странице заказа
    button_yes = [By.XPATH, ".//button[text()='Да']"]                                                          # Кнопка Да
    header_order_ready = [By.XPATH, ".//div[text()='Заказ оформлен']"]                                         # Заголовок Заказ оформлен
    button_see_status = (By.XPATH, ".//button[text()='Посмотреть статус']")                                    # Кнопка Посмотреть статус
    button_dzen = (By.XPATH, ".//button[@class='dzen-search-arrow-common__button']")                           # Кнопка Дзен

    @allure.step('Нажимаем верхнюю кнопку Заказать')
    def click_home_button_order(self, driver):
        driver.find_element(*self.home_page_button_order).click()

    @allure.step('Нажимаем нижнюю кнопку Заказать')
    def click_home_button_order_lower(self, driver):
        element = driver.find_element(*self.home_page_button_order_lower)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable(self.home_page_button_order_lower))
        element.click()

    @allure.step('Заполняем Имя')
    def fill_name(self, driver2, name):
        driver2.find_element(*self.name).send_keys(name)

    @allure.step('Заполняем Фамилию')
    def fill_surname(self, driver2, surname):
        driver2.find_element(*self.surname).send_keys(surname)

    @allure.step('Заполняем Адресс')
    def fill_adress(self, driver2, adress):
        driver2.find_element(*self.adress).send_keys(adress)

    @allure.step('Выбираем станцию метро Сокольники')
    def fill_metro_station(self, driver2):
        input_metro = driver2.find_element(*self.metro_input)
        input_metro.click()
        WebDriverWait(driver2, 3).until(expected_conditions.visibility_of_element_located(self.metro_station))
        driver2.find_element(*self.metro_station).click()

    @allure.step('Выбираем станцию метро Черкизовская')
    def fill_metro_station_2(self, driver2):
        input_metro = driver2.find_element(*self.metro_input)
        input_metro.click()
        WebDriverWait(driver2, 3).until(expected_conditions.visibility_of_element_located(self.metro_station_2))
        driver2.find_element(*self.metro_station_2).click()

    @allure.step('Заполняем поле Телефон')
    def fill_phone(self, driver2, phone):
        driver2.find_element(*self.phone).send_keys(phone)

    @allure.step('Нажимаем кнопку Далее')
    def click_button_futher(self, driver2):
        driver2.find_element(*self.button_futher).click()

    @allure.step('Выбираем дату 20 в датапикере')
    def fill_data_20(self, driver2):
        driver2.find_element(*self.data_input).click()
        driver2.find_element(*self.date_20).click()

    @allure.step('Выбираем дату 23 в датапикере')
    def fill_data_23(self, driver2):
        driver2.find_element(*self.data_input).click()
        driver2.find_element(*self.date_23).click()

    @allure.step('Выбираем одни сутки')
    def fill_time_one_day(self, driver2):
        driver2.find_element(*self.time_input).click()
        driver2.find_element(*self.time_one_day).click()

    @allure.step('Выбираем двое суток')
    def fill_time_two_day(self, driver2):
        driver2.find_element(*self.time_input).click()
        driver2.find_element(*self.time_two_day).click()

    @allure.step('Выбираем черный цвет самоката')
    def check_color_scooter_black(self, driver2):
        driver2.find_element(*self.color_scooter_black).click()

    @allure.step('Выбираем серый цвет самоката')
    def check_color_scooter_gray(self, driver2):
        driver2.find_element(*self.color_scooter_gray).click()

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self, driver2):
        driver2.find_element(*self.button_order).click()

    @allure.step('Нажимаем кнопку Да')
    def click_button_yes(self, driver2):
        driver2.find_element(*self.button_yes).click()

    @allure.step('Нажимаем Посмотреть статус')
    def click_button_status(self, driver2):
        driver2.find_element(*self.button_see_status).click()

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