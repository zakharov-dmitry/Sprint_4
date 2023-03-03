import time

from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat


def test_order_with_navigation_to_main_page_positive_result(create_firefox_driver):
    # check the successful case of placing the order with navigating to the main page on the end
    NAME = "Виктор"
    SURNAME = "Иванов"
    ADDRESS = "Москва, Смоленская наб., 32-12"
    METRO = "1"
    NUMBER = "+79119876532"
    RENTAL_PERIOD = 1
    TEXT = "нет комментариев"

    driver = create_firefox_driver
    mp = MainPageSamokat(driver)
    mp.open_main_page()
    mp.click_on_1st_button_order()
    op = OrderPageSamokat(driver)
    op.set_name(NAME)
    op.set_surname(SURNAME)
    op.set_address(ADDRESS)
    op.choose_metro_station(METRO)
    op.set_phone_number(NUMBER)
    op.open_next_page_order()
    op.set_delivery_date_on_6th_next_month()
    op.select_rental_period(RENTAL_PERIOD)
    op.set_black_color()
    op.set_comment(TEXT)
    op.place_order()
    op.submit_order()
    op.check_successful_confirmation_window()
    op.navigate_to_order_view_after_confirmation()
    op.check_navigation_to_main_page_from_tracking_page_via_samokat_logo()


    time.sleep(2)
    driver.quit()


def test_order_with_navigation_to_yandex_page_positive_result(create_firefox_driver):
    # check the successful case of placing the order with navigating to the yandex page on the end
    NAME = "Сергей"
    SURNAME = "Орлов"
    ADDRESS = "Москва, Рабочий пр-д., 12-32"
    METRO = "2"
    NUMBER = "+79219876532"
    RENTAL_PERIOD = 2
    TEXT = "не звонить после 18-00"

    driver = create_firefox_driver
    mp = MainPageSamokat(driver)
    mp.open_main_page()
    mp.click_on_1st_button_order()
    op = OrderPageSamokat(driver)
    op.set_name(NAME)
    op.set_surname(SURNAME)
    op.set_address(ADDRESS)
    op.choose_metro_station(METRO)
    op.set_phone_number(NUMBER)
    op.open_next_page_order()
    op.set_delivery_date_on_6th_next_month()
    op.select_rental_period(RENTAL_PERIOD)
    op.set_black_color()
    op.set_comment(TEXT)
    op.place_order()
    op.submit_order()
    op.check_successful_confirmation_window()
    op.navigate_to_order_view_after_confirmation()
    op.check_navigation_to_yandex_page_from_tracking_page_via_yandex_logo()


    time.sleep(2)
    driver.quit()