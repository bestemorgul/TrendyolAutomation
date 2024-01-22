from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    MY_BASKET_TEXT = (By.CLASS_NAME, "pb-header")
    REMOVE_BTN = (By.CLASS_NAME, 'i-trash')
    SEARCH_BOX = (By.CLASS_NAME, 'V8wbcUhU')
    SEARCH_BTN = (By.CLASS_NAME, 'cyrzo7gC')

    def get_basket_text(self):
        return self.find_element(*self.MY_BASKET_TEXT).text

    def remove_item_from_cart(self):
        self.click_element(*self.REMOVE_BTN)

    def fill_search_box(self, search_input):
        self.send_text(search_input, *self.SEARCH_BOX)

    def click_search_btn(self):
        self.click_element(*self.SEARCH_BTN)
