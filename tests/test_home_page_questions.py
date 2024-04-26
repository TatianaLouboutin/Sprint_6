from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from pages.base_page import BasePageScooter
from locators.locators import ScooterLocators
import allure


class TestHomePageScooter():

    @allure.title("Проверка вопросов")
    @allure.description("Проверка восьми вопросов на главной странице и ответов на них")
    @pytest.mark.parametrize('question, answer', ScooterLocators.lst_questions_answers)
    def test_check_answer(self, driver, question, answer):
        basepage = BasePageScooter(driver)
        basepage.agree_with_coockie(driver)
        basepage.scroll_to_locator(driver, ScooterLocators.one_question)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(question))
        driver.find_element(*question).click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(answer))
        assert driver.find_element(*answer).is_displayed()






