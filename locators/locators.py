from selenium.webdriver.common.by import By


class ScooterLocators:
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
    six_answer = [By.XPATH,  ".//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
    seven_answer = [By.XPATH, ".//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
    eight_answer = [By.XPATH, ".//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]

    button_coockie = [By.XPATH, ".//button[text()='да все привыкли']"]                 # Кнопка Принять куки
    link_scooter = (By.XPATH, ".// img[@alt='Scooter']")                               # Логотип Самоката
    link_yandex = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")                # Логотип Яндекса

    home_page_button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]    # Верхняя кнопка "Заказать"
    home_page_button_order_lower = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"] # Нижняя кнопка "Заказать"

    name = [By.XPATH, ".//input[@placeholder='* Имя']"]                                # Поле Имя
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]                         # Поле Фамилия
    adress = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]       # Поле Адрес
    metro_input = [By.XPATH, ".//input[@placeholder='* Станция метро']"]               # Поле ввода станции метро
    metro_station = [By.XPATH, ".//div[contains(text(), 'Сокольники')]"]               # Станция Сокольники
    metro_station_2 = [By.XPATH, ".//div[contains(text(), 'Черкизовская')]"]           # Станция Черкизовская
    phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле Телефон
    button_futher = [By.XPATH, ".//button[text()='Далее']"]                            # Кнопка Далее
    data_input = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]       # Поле ввода даты начала аренды
    date_23 = [By.XPATH, ".//div[text()='23']"]                                        # 23 число текущего месяца
    date_20 = [By.XPATH, ".//div[text()='20']"]                                        # 20 число текущего месяца
    time_input = [By.XPATH, ".//div[text()='* Срок аренды']"]                          # Поле ввода длительности аренды
    time_one_day = [By.XPATH, ".//div[text()='сутки']"]                                # Одни сутки
    time_two_day = [By.XPATH, ".//div[text()='двое суток']"]                           # Двое суток
    color_scooter_black = [By.XPATH, ".//input[@id='black']"]                          # Чекбокс цвет: чёрный жемчуг
    color_scooter_gray = [By.XPATH, ".//input[@id='grey']"]                            # Чекбокс цвет: серая безысходность

    button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]  # Кнопка заказа на странице заказа
    button_yes = [By.XPATH, ".//button[text()='Да']"]                                  # Кнопка Да
    header_order_ready = [By.XPATH, ".//div[text()='Заказ оформлен']"]                 # Заголовок Заказ оформлен
    button_see_status = (By.XPATH, ".//button[text()='Посмотреть статус']")            # Кнопка Посмотреть статус
    button_dzen = (By.XPATH, ".//button[@class='dzen-search-arrow-common__button']")   # Кнопка Дзен

    lst_questions_answers = [[one_question, one_answer], [two_question, two_answer], [three_question, three_answer],
                             [four_question, four_answer], [five_question, five_answer], [six_question, six_answer],
                             [seven_question, seven_answer],
                             [eight_question, eight_answer]]                            # Список списков: вопрос - ответ