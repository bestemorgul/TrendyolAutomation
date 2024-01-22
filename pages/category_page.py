from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    MOST_ADDED_ITEMS = (By.XPATH, "//a[@href='/sr?fl=sepettekiurunler']")
    THIRD_PRODUCT = (By.XPATH, './/*[contains(@class, "p-card-wrppr with-campaign-view")]')
    ADD_TO_WISHLIST = (By.XPATH, "(//i[@class='fvrt-btn'])[1]")
    SEARCH_TEXT = (By.XPATH, "//h1[normalize-space()='kahve makinesi']")

    def click_most_added_items(self):
        self.click_element(*self.MOST_ADDED_ITEMS)

    def click_third_item(self, index=0):
        self.get_element_list(*self.THIRD_PRODUCT)[index].click()

    def add_to_wishlist(self):
        self.scroll()
        self.click_element(*self.ADD_TO_WISHLIST)

    def get_search_text(self):
        return self.find_element(*self.SEARCH_TEXT)


