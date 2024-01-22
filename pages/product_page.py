from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.CLASS_NAME, 'add-to-basket')
    BASKET = (By.CLASS_NAME, "add-to-basket-button-text-success")
    GO_TO_BASKET = (By.CLASS_NAME, "goBasket")

    def add_to_cart(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click_element(*self.ADD_TO_CART_BTN)

    def add_to_cart_btn_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ADD_TO_CART_BTN)).text

    def hover_to_basket(self):
        self.hover_to_element(*self.BASKET)

    def go_to_basket_page(self):
        self.wait.until(EC.visibility_of_element_located(self.GO_TO_BASKET)).click()


