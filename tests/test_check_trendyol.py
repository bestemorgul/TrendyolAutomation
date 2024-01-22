import logging
import time

from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestCheckTrendyol(BaseTest):
    """Test case is:

      1. Go to the main page, click women category, and then click most added items category, select the third
      item on most added items category page
      2. Add to cart the item and go to basket page
      3. Remove the item from the cart, send text to the searchbox and click the search button
      4. Click add to wish button on the first item, and go back to home page

      """
    most_added_items_text = "sepettekiurunler"
    search_input_text = "kahve makinesi"
    added_to_cart_text = "Sepete Eklendi"
    filled_basket_text = "Sepetim (1 Ürün)"
    empty_basket_text = "Sepetim (0 Ürün)"
    trendyol_main_page_url = "https://www.trendyol.com/"

    def test_check_trendyol(self):
        self.logger = logging.getLogger()

        self.logger.info("1. Go to www.trendyol.com, click women category, and then click most added items category, "
                         "select the third item on most added items category page")
        home_page = HomePage(self.driver)
        home_page.hover_to_women()
        category_page = CategoryPage(self.driver)
        category_page.click_most_added_items()
        self.assertIn(self.most_added_items_text, self.driver.current_url, "You are not on most added items page!")
        category_page.click_third_item(3)
        self.logger.info("Third item is clicked successfully!")

        self.logger.info("2. Add to cart the item and go to basket page")
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        time.sleep(3)
        self.assertEqual(self.added_to_cart_text, product_page.add_to_cart_btn_text())
        product_page.hover_to_basket()
        product_page.go_to_basket_page()
        self.logger.info("Basket page is opened successfully!")

        self.logger.info("3. Remove the item from the cart, send text to the searchbox and click the search button")
        cart_page = CartPage(self.driver)
        self.assertEqual(self.filled_basket_text, cart_page.get_basket_text(),
                         "Your item at the cart is not equal to 1!")
        cart_page.remove_item_from_cart()
        time.sleep(3)
        self.assertEqual(self.empty_basket_text, cart_page.get_basket_text(), "Your cart is not empty!")
        cart_page.fill_search_box(self.search_input_text)
        cart_page.click_search_btn()
        time.sleep(3)
        self.assertTrue(category_page.get_search_text(), "There is no result!")
        self.logger.info("Search result is got successfully!")

        self.logger.info("4. Click add to wish button on the first item, and go back to home page")
        category_page.add_to_wishlist()
        login_page = LoginPage(self.driver)
        time.sleep(3)
        login_page.go_back_to_main_page()
        self.assertEqual(self.trendyol_main_page_url, self.driver.current_url, "It is not home page!")
        self.logger.info("Home page is opened successfully!")
