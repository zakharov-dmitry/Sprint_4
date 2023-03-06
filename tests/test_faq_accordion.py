from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPageSamokat


class TestFaqAccordionAnswers:
    # this test class check all answers for the questions in the FAQ accordion, test to be executed all together,
    # because of the state dependencies
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = driver = webdriver.WebDriver(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.maximize_window()

    def test_1st_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.open_main_page()
        mp.wait_for_loading_faq_accordion()
        mp.scroll_to_faq_accordion_question(1)
        mp.click_on_accordion_question(1)
        mp.check_faq_answer_is_correct(1)
        mp.check_faq_answer_not_hidden(1)

    def test_2nd_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(2)
        mp.click_on_accordion_question(2)
        mp.check_faq_answer_is_correct(2)
        mp.check_faq_answer_not_hidden(2)

    def test_3d_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(3)
        mp.click_on_accordion_question(3)
        mp.check_faq_answer_is_correct(3)
        mp.check_faq_answer_not_hidden(3)

    def test_4s_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(4)
        mp.click_on_accordion_question(4)
        mp.check_faq_answer_is_correct(4)
        mp.check_faq_answer_not_hidden(4)

    def test_5s_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(5)
        mp.click_on_accordion_question(5)
        mp.check_faq_answer_is_correct(5)
        mp.check_faq_answer_not_hidden(5)

    def test_6s_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(6)
        mp.click_on_accordion_question(6)
        mp.check_faq_answer_is_correct(6)
        mp.check_faq_answer_not_hidden(6)

    def test_7s_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(7)
        mp.click_on_accordion_question(7)
        mp.check_faq_answer_is_correct(7)
        mp.check_faq_answer_not_hidden(7)

    def test_8s_faq_answer_is_correct(self):
        mp = MainPageSamokat(self.driver)
        mp.scroll_to_faq_accordion_question(8)
        mp.click_on_accordion_question(8)
        mp.check_faq_answer_is_correct(8)
        mp.check_faq_answer_not_hidden(8)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
