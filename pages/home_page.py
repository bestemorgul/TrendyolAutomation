from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    POP_UP_CLOSE = (By.CLASS_NAME, 'modal-close')
    WOMEN_CATEGORY = (By.LINK_TEXT, 'Kadın')

    def hover_to_women(self):
        self.click_element(*self.POP_UP_CLOSE)
        self.click_element(*self.WOMEN_CATEGORY)



