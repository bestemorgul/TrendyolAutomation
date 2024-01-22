import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def get_url(self):
        """
     it returns the current url of the page
        """

        return self.driver.current_url

    def hover_to_element(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def find_element(self, *locator):
        """
     it returns the locator
        """

        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        """
     it clicks the locator
        """

        self.driver.find_element(*locator).click()

    def send_text(self, text, *locator):
        """
     it sends the text on the locator
        """

        self.driver.find_element(*locator).send_keys(text)

    def get_element_list(self, *element):
        """
     it returns the locators
        """

        return self.driver.find_elements(*element)

    def scroll(self):
        """
     it scrolls down on the page (0,250)
        """

        self.driver.execute_script("window.scrollBy(0, 100);")
