from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators.main_page_locators as mpl


class MainPageSamokat:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    def wait_for_loading_faq_accordion(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(mpl.accordion_question_1))

    def scroll_to_faq_accordion_question(self, number):
        accordion_question = self.driver.find_element(*getattr(mpl, f'accordion_question_{number}'))
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_question)

    def click_on_accordion_question(self, number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(getattr(mpl, f'accordion_question_{number}')))
        self.driver.find_element(*getattr(mpl, f'accordion_question_{number}')).click()

    def check_faq_answer_is_correct(self, number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(getattr(mpl, f'accordion_answer_{number}')))
        expected_answer = getattr(mpl, f'ANSWER_{number}')
        actual_answer = self.driver.find_element(*getattr(mpl, f'accordion_answer_{number}')).text
        assert expected_answer == actual_answer

    def check_faq_answer_not_hidden(self, number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(getattr(mpl, f'accordion_answer_panel_{number}')))
        assert not self.driver.find_element(*getattr(mpl, f'accordion_answer_panel_{number}')).get_attribute("hidden")

    def click_on_1st_button_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(mpl.small_button_order))
        self.driver.find_element(*mpl.small_button_order).click()

    def click_on_2nd_button_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(mpl.big_button_order))
        big_button_order = self.driver.find_element(*mpl.big_button_order)
        self.driver.execute_script("arguments[0].scrollIntoView();", big_button_order)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(mpl.big_button_order))
        big_button_order.click()
