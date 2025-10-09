from selenium.webdriver.common.by import By

# global variables with exact answers
ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

# questions in FAQ accordion
accordion_question_1 = [By.XPATH, ".//div[text()='Сколько это стоит? И как оплатить?']"]
accordion_question_2 = [By.XPATH, ".//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
accordion_question_3 = [By.XPATH, ".//div[text()='Как рассчитывается время аренды?']"]
accordion_question_4 = [By.XPATH, ".//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
accordion_question_5 = [By.XPATH, ".//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
accordion_question_6 = [By.XPATH, ".//div[text()='Вы привозите зарядку вместе с самокатом?']"]
accordion_question_7 = [By.XPATH, ".//div[text()='Можно ли отменить заказ?']"]
accordion_question_8 = [By.XPATH, ".//div[text()='Я жизу за МКАДом, привезёте?']"]

# actual answers for the questions in FAQ accordion
accordion_answer_panel_1 = [By.XPATH, ".//div[@id='accordion__panel-0']"]
accordion_answer_panel_2 = [By.XPATH, ".//div[@id='accordion__panel-1']"]
accordion_answer_panel_3 = [By.XPATH, ".//div[@id='accordion__panel-2']"]
accordion_answer_panel_4 = [By.XPATH, ".//div[@id='accordion__panel-3']"]
accordion_answer_panel_5 = [By.XPATH, ".//div[@id='accordion__panel-4']"]
accordion_answer_panel_6 = [By.XPATH, ".//div[@id='accordion__panel-5']"]
accordion_answer_panel_7 = [By.XPATH, ".//div[@id='accordion__panel-6']"]
accordion_answer_panel_8 = [By.XPATH, ".//div[@id='accordion__panel-7']"]

# actual text of the answers for the questions in FAQ accordion
accordion_answer_1 = [By.XPATH, ".//div[@id='accordion__panel-0']/p"]
accordion_answer_2 = [By.XPATH, ".//div[@id='accordion__panel-1']/p"]
accordion_answer_3 = [By.XPATH, ".//div[@id='accordion__panel-2']/p"]
accordion_answer_4 = [By.XPATH, ".//div[@id='accordion__panel-3']/p"]
accordion_answer_5 = [By.XPATH, ".//div[@id='accordion__panel-4']/p"]
accordion_answer_6 = [By.XPATH, ".//div[@id='accordion__panel-5']/p"]
accordion_answer_7 = [By.XPATH, ".//div[@id='accordion__panel-6']/p"]
accordion_answer_8 = [By.XPATH, ".//div[@id='accordion__panel-7']/p"]

# buttons to initiate an order
small_button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
big_button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']"]

# TODO: base element from header, should be moved to the separate POM class Header during next refiniment
samokat_logo = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
yandex_logo = [By.XPATH, ".//img[@src='/assets/ya.svg']"]


