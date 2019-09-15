from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_form()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Basket URL is malformed"

    def should_be_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TITLE), "Basket title is not presented"
        assert self.is_element_present(*BasketPageLocators.BASKET_BREADCRUMB), "Basket breadcrumb is not presented"

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket is not empty, but should be"

    def should_not_be_goods_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There are good in basket, but should not be"
