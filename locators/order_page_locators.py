from selenium.webdriver.common.by import By

# all fields for data input on the first order page
name_field = [By.XPATH, ".//input[@placeholder='* Имя']"]
surname_field = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
address_field = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
metro_field = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
metro_item_1 = [By.XPATH, ".//div[@class='select-search__select']//div[text()='Бульвар Рокоссовского']"]
metro_item_2 = [By.XPATH, ".//div[@class='select-search__select']//div[text()='Черкизовская']"]
metro_item_3 = [By.XPATH, ".//div[@class='select-search__select']//div[text()='Сокольники']"]
metro_item_4 = [By.XPATH, ".//div[@class='select-search__select']//div[text()='Красносельская']"]
phone_field = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]

# button to navigate to the second page for ordering
button_further = [By.XPATH, ".//button[text()='Далее']"]

# all fields for data input on the second order page
date_field = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
calendar = [By.XPATH, ".//div[@class='react-datepicker__month-container']"]
button_next_month = [By.XPATH, ".//button[@aria-label='Next Month']"]
date_10 = [By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--010']"]

rental_period_field = [By.XPATH, ".//div[text()='* Срок аренды']"]
rental_period_dropdown = [By.XPATH, ".//div[@class='Dropdown-root is-open']//div[@class='Dropdown-menu']"]
list_of_rental_periods = [By.XPATH, ".//div[@class='Dropdown-root is-open']//div[@class='Dropdown-option']"]
checkbox_color_black = [By.XPATH, ".//input[@id='black']"]
checkbox_color_gray = [By.XPATH, ".//input[@id='gray']"]
comment_field = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]

# order button on the second order page
button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

# final confirmation button in the dialog window
confirm_order_button = [By.XPATH, ".//button[text()='Да']"]

# confirmation window with tracking information about placed order
confirmation_dialog = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]
button_view_status_of_order = [By.XPATH, ".//button[text()='Посмотреть статус']"]

# TODO: base element from header, should be moved to the separate POM class Header during next refiniment
samokat_logo = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
yandex_logo = [By.XPATH, ".//img[@src='/assets/ya.svg']"]

#locator of the search button on the yandex page for testing the navigation, not related to the order page
yandex_button_search = [By.XPATH, ".//button[text()='Найти']"]