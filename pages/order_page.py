import time

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators.order_page_locators as opl
import locators.main_page_locators as mpl


class OrderPageSamokat:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page_for_order(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/order")

    def set_name(self, name):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.name_field))
        self.driver.find_element(*opl.name_field).send_keys(name)

    def set_surname(self, surname):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.surname_field))
        self.driver.find_element(*opl.surname_field).send_keys(surname)

    def set_address(self, address):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.address_field))
        self.driver.find_element(*opl.address_field).send_keys(address)

    def choose_metro_station(self, metro_item_number):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.metro_field))
        self.driver.find_element(*opl.metro_field).click()
        self.driver.find_element(*getattr(opl, f'metro_item_{metro_item_number}')).click()

    def set_phone_number(self, number):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.phone_field))
        self.driver.find_element(*opl.phone_field).send_keys(number)

    def open_next_page_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.button_further))
        self.driver.find_element(*opl.button_further).click()

    def set_delivery_date_on_6th_next_month(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.date_field))
        self.driver.find_element(*opl.date_field).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.calendar))
        self.driver.find_element(*opl.button_next_month).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.date_6))
        self.driver.find_element(*opl.date_6).click()

    def select_rental_period(self, rental_period):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.rental_period_field))
        self.driver.find_element(*opl.rental_period_field).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(opl.rental_period_dropdown))
        all_periods = self.driver.find_elements(*opl.list_of_rental_periods)
        selected_period = all_periods[rental_period]
        selected_period.click()

    def set_black_color(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.checkbox_color_black))
        self.driver.find_element(*opl.checkbox_color_black).click()

    def set_comment(self, text):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.comment_field))
        self.driver.find_element(*opl.comment_field).send_keys(text)

    def place_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.button_order))
        self.driver.find_element(*opl.button_order).click()

    def submit_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.confirm_order_button))
        confirm_button = self.driver.find_element(*opl.confirm_order_button)
        self.driver.execute_script("arguments[0].click();", confirm_button)

    def check_successful_confirmation_window(self):
        expected_message = "Заказ оформлен"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.confirmation_dialog))
        actual_message = self.driver.find_element(*opl.confirmation_dialog).text
        assert expected_message in actual_message

    def navigate_to_order_view_after_confirmation(self):
        #sleep is needed to wait for DB responce with order ID
        time.sleep(1)
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(opl.button_view_status_of_order))
        button_view_status = self.driver.find_element(*opl.button_view_status_of_order)
        self.driver.execute_script("arguments[0].click();", button_view_status)

    def check_navigation_to_main_page_from_tracking_page_via_samokat_logo(self):
        initial_url = self.driver.current_url
        main_page_url = "https://qa-scooter.praktikum-services.ru/"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.samokat_logo))
        self.driver.find_element(*opl.samokat_logo).click()
        # wait for loading main page
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(mpl.accordion_question_1))
        actual_url = self.driver.current_url

        assert actual_url == main_page_url != initial_url

    def check_navigation_to_yandex_page_from_tracking_page_via_yandex_logo(self):
        initial_url = self.driver.current_url
        yandex_page_url = "https://dzen.ru/?yredirect=true"
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.yandex_logo))
        self.driver.find_element(*opl.yandex_logo).click()
        # wait for loading ya page and switch on the new tab
        next_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(next_tab)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(opl.yandex_button_search))
        actual_url = self.driver.current_url
        print(f"Initial URL -->> {initial_url}")
        print(f"Yandex_page_url -->> {yandex_page_url}")
        print(f"Actual_url -->> {actual_url}")
        assert actual_url == yandex_page_url != initial_url
