from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout=10)
        self.item_price = ""
        self.item_name = ""

    def press_add_to_basket(self):
        # link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link = self.browser.find_element(By.XPATH, "//button[contains(text(),'basket')]")
        link.click()

    def item_should_be_in_basket(self):
        assert "has been added to your basket." in self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET).text, "Item was not added to basket "
        assert self.item_name in self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET).text, "Wrong item was added to basket "
        assert self.item_price in self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL).text, "Wrong basket total"

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not " \
                                                                                   "presented "

    def should_be_price_on_the_page(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"
        self.item_price = self.browser.find_element(*ProductPageLocators.PRICE).text

    def should_be_item_name_on_the_page(self):
        assert self.is_element_present(*ProductPageLocators.NAME), "Item name is not presented"
        self.item_name = self.browser.find_element(*ProductPageLocators.NAME).text
