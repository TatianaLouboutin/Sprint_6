from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
import allure

class HomePageScooter:
    one_question = [By.XPATH, ".//div/div[text()='Сколько это стоит? И как оплатить?']"]
    two_question = [By.XPATH, ".//div/div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    three_question = [By.XPATH, ".//div/div[text()='Как рассчитывается время аренды?']"]
    four_question = [By.XPATH, ".//div/div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    five_question = [By.XPATH, ".//div/div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    six_question = [By.XPATH, ".//div/div[text()='Вы привозите зарядку вместе с самокатом?']"]
    seven_question = [By.XPATH, ".//div/div[text()='Можно ли отменить заказ?']"]
    eight_question = [By.XPATH, ".//div/div[text()='Я жизу за МКАДом, привезёте?']"]

    one_answer = [By.XPATH, ".//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]
    two_answer = [By.XPATH, ".//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]
    three_answer = [By.XPATH, ".//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]
    four_answer = [By.XPATH, ".//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]
    five_answer = [By.XPATH, ".//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]
    six_answer = [By.XPATH, ".//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
    seven_answer = [By.XPATH, ".//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
    eight_answer = [By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]

    button_coockie = [By.XPATH, ".//button[text()='да все привыкли']"]   # Кнопка Принять куки
    link_scooter = (By.XPATH, ".// img[@alt='Scooter']")                 # Логотип Самоката
    link_yandex = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")  # Логотип Яндекса

    lst_questions_answers = [[one_question,one_answer],[two_question,two_answer], [three_question,three_answer],
                             [four_question, four_answer], [five_question, five_answer], [six_question, six_answer],
    [seven_question, seven_answer], [eight_question, eight_answer]]      # Список списков: вопрос - ответ
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку Принять куки')
    def agree_with_coockie(self, driver):
        driver.find_element(*self.button_coockie).click()

    @allure.step('Скроллим страницу до вопросов')
    def scroll_to_questions(self, driver):
        element = driver.find_element(*self.one_question)
        driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Нажимаем лого Самокат')
    def click_link_scooter(self, driver):
        driver.find_element(*self.link_scooter).click()

    @allure.step('Нажимаем лого Яндекса')
    def click_link_logo(self, driver):
        driver.find_element(*self.link_yandex).click()

    def find_questions(self, driver):
        self.agree_with_coockie(driver)
        self.scroll_to_questions(driver)


