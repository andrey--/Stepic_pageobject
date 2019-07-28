import pytest

from Pages.login_page import LoginPage
from Pages.product_page import ProductPage


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at- work_207/?promo=offer7",
                              # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_cart(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_item_name_on_the_page()
        page.should_be_price_on_the_page()
        page.press_add_to_basket()
        page.solve_quiz()
        page.item_should_be_in_basket()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_item_name_on_the_page()
        page.should_be_price_on_the_page()
        page.should_not_be_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
