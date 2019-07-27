from Pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_item_name_on_the_page()
    page.should_be_price_on_the_page()
    page.press_add_to_basket()
    page.solve_quiz()
    page.item_should_be_in_basket()
