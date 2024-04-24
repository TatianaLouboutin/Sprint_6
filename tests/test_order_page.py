from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter
import allure


class TestOrderPageScooter():

    @allure.title("Первый позитивный сценарий")
    @allure.description("Первый позитивный сценарий")
    def test_order_page_first_set(self, driver):
        orderpage = OrderPageScooter(self)
        orderpage.do_first_order(driver)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(OrderPageScooter.header_order_ready))
        assert driver.find_element(*OrderPageScooter.header_order_ready).is_displayed()

    @allure.title("Второй позитивный сценарий")
    @allure.description("Второй позитивный сценарий")
    def test_order_page_second_set(self, driver):
        orderpage = OrderPageScooter(self)
        orderpage.do_second_order(driver)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(OrderPageScooter.header_order_ready))
        assert driver.find_element(*OrderPageScooter.header_order_ready).is_displayed()
    @allure.title("Редирект на страницу самоката")
    @allure.description("Нажататие лого Самоката ведет на страницу самоката")
    def test_order_page_first_set_click_image_scooter(self, driver):
        homepage = HomePageScooter(driver)
        orderpage = OrderPageScooter(driver)
        orderpage.do_first_order(driver)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(OrderPageScooter.header_order_ready))
        orderpage.click_button_status(driver)
        homepage.click_link_scooter(driver)
        assert driver.current_url == settings.URL
    @allure.title("Редирект на Дзен")
    @allure.description("Редирект на Дзен")
    def test_order_page_second_set_click_logo(self, driver):
        homepage = HomePageScooter(driver)
        orderpage = OrderPageScooter(driver)
        orderpage.do_second_order(driver)
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(OrderPageScooter.header_order_ready))
        orderpage.click_button_status(driver)
        homepage.click_link_logo(driver)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(OrderPageScooter.button_dzen))
        assert  driver.current_url == settings.DZEN