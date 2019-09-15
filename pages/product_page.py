from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout=timeout)
        self.item_price = "Your basket total is now "
        self.item_name = " has been added to your basket."
        self.add_to_basket_text = "Add to basket"

    def item_should_be_in_basket(self):
        assert "has been added to your basket." in self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET).text, "Item was not added to basket "
        found = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET).text
        assert self.item_name == found, f"Wrong item was added to basket. Should be '{self.item_name}' " \
                                        f"but '{found}' was found"
        found = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert self.item_price == found, f"Wrong basket total. Should be '{self.item_price}' " \
                                         f"but '{found}' was found"

    def press_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message does not disappeared, but should"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not " \
                                                                                   "presented "
        found = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).text
        assert found == self.add_to_basket_text, f"Wrong name for 'Add to basket button'." \
                                                 f"Should be '{self.add_to_basket_text}' but '{found}' was found"

    def should_be_price_on_the_page(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"
        self.item_price += self.browser.find_element(*ProductPageLocators.PRICE).text

    def should_be_item_name_on_the_page(self):
        assert self.is_element_present(*ProductPageLocators.NAME), "Item name is not presented"
        self.item_name = self.browser.find_element(*ProductPageLocators.NAME).text + self.item_name

    def solve_quiz(self):
        self.solve_quiz_and_get_code()
