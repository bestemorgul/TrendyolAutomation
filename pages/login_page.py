from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    TRENDYOL_LOGO = (By.ID, 'logo')

    def go_back_to_main_page(self):
        self.wait.until(EC.element_to_be_clickable(self.TRENDYOL_LOGO)).click()
