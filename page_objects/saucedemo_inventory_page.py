from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base_page import BasePage

class SaucedemoInventoryPage(BasePage):
    """Page Object Model for Saucedemo Inventory page."""
    
    # Locators
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_TITLE = (By.CLASS_NAME, "product_label")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU = (By.CLASS_NAME, "bm-burger-button")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    
    def __init__(self, driver, base_url):
        """
        Initialize inventory page.
        
        Args:
            driver: Selenium WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
    
    def is_inventory_page_loaded(self):
        """
        Check if inventory page is loaded.
        
        Returns:
            Boolean
        """
        return self.is_displayed(*self.INVENTORY_CONTAINER)
    
    def get_page_title(self):
        """
        Get page title text.
        
        Returns:
            Title string
        """
        return self.get_text(*self.PRODUCT_TITLE)
    
    # Locators for inventory page elements
    PRODUCT_SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_primary.btn_inventory")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.btn_secondary.btn_inventory")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    SIDE_MENU_WRAPPER = (By.CLASS_NAME, "bm-menu-wrap")

    # Locators for product details page elements
    DETAILS_PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    BACK_TO_PRODUCTS_BUTTON = (By.CLASS_NAME, "inventory_details_back_button")

    def is_sort_dropdown_displayed(self):
        """Check if the sort dropdown is displayed."""
        return self.is_displayed(*self.PRODUCT_SORT_CONTAINER)

    def is_shopping_cart_icon_displayed(self):
        """Check if the shopping cart icon is displayed."""
        return self.is_displayed(*self.SHOPPING_CART_LINK)

    def get_shopping_cart_count(self):
        """Get the number of items in the shopping cart."""
        badge_elements = self.driver.find_elements(*self.SHOPPING_CART_BADGE)
        for badge in badge_elements:
            try:
                if not badge.is_displayed():
                    continue
            except Exception:
                continue
            badge_text = badge.text.strip()
            try:
                return int(badge_text) if badge_text else 0
            except ValueError:
                return 0
        return 0



    def wait_for_cart_count(self, expected_count, timeout=None):
        """Wait until the shopping cart badge shows the expected count."""
        expected_count = max(0, expected_count)
        wait = WebDriverWait(self.driver, timeout or self.default_timeout)
        try:
            if expected_count == 0:
                return wait.until(lambda _: self.get_shopping_cart_count() == 0)
            return wait.until(lambda _: self.get_shopping_cart_count() == expected_count)
        except TimeoutException:
            return False

    def get_product_count(self):
        """Get the number of products displayed on the page."""
        return len(self.find_elements(*self.INVENTORY_ITEM))

    def select_sort_option(self, option_value):
        """Selects a sorting option from the dropdown."""
        self.select_by_value(*self.PRODUCT_SORT_CONTAINER, option_value)

    def get_all_product_names(self):
        """Get a list of all product names displayed."""
        product_elements = self.find_elements(*self.INVENTORY_ITEM_NAME)
        return [element.text for element in product_elements]

    def get_all_product_prices(self):
        """Get a list of all product prices displayed."""
        price_elements = self.find_elements(*self.INVENTORY_ITEM_PRICE)
        return [element.text for element in price_elements]

    def _get_product_element(self, index):
        """Helper to get a specific product element by index."""
        products = self.find_elements(*self.INVENTORY_ITEM)
        if 0 <= index < len(products):
            return products[index]
        raise IndexError(f"Product with index {index} not found.")

    def add_item_to_cart(self, index):
        """Add an item to the cart by its index."""
        current_count = self.get_shopping_cart_count()
        product_element = self._get_product_element(index)
        add_button = self.wait.until(lambda _: product_element.find_element(*self.ADD_TO_CART_BUTTON))
        self.driver.execute_script("arguments[0].click();", add_button)
        try:
            self.wait.until(lambda _: self.is_remove_button_displayed(index))
        except Exception:
            pass
        self.wait_for_cart_count(current_count + 1)

    def remove_item_from_cart(self, index):
        """Remove an item from the cart by its index."""
        current_count = self.get_shopping_cart_count()
        product_element = self._get_product_element(index)
        remove_button = self.wait.until(lambda _: product_element.find_element(*self.REMOVE_BUTTON))
        self.driver.execute_script("arguments[0].click();", remove_button)
        try:
            self.wait.until(lambda _: self.is_add_to_cart_button_displayed(index))
        except Exception:
            pass
        self.wait_for_cart_count(max(current_count - 1, 0))

    def is_remove_button_displayed(self, index):
        """Check if the 'Remove' button is displayed for a product by its index."""
        product_element = self._get_product_element(index)
        return self.is_element_displayed(product_element, *self.REMOVE_BUTTON)

    def is_add_to_cart_button_displayed(self, index):
        """Check if the 'Add to cart' button is displayed for a product by its index."""
        product_element = self._get_product_element(index)
        return self.is_element_displayed(product_element, *self.ADD_TO_CART_BUTTON)

    def click_product_title(self, index):
        """Click on the title of a product to go to its details page."""
        product_element = self._get_product_element(index)
        product_element.find_element(*self.INVENTORY_ITEM_NAME).click()

    def get_product_name(self, index):
        """Get product name by index on inventory page."""
        product_element = self._get_product_element(index)
        return product_element.find_element(*self.INVENTORY_ITEM_NAME).text

    def is_product_details_page_loaded(self):
        """Check if the product details page is loaded."""
        return self.is_displayed(*self.DETAILS_PRODUCT_NAME)

    def get_product_details_name(self):
        """Get the product name from the details page."""
        return self.get_text(*self.DETAILS_PRODUCT_NAME)

    def click_back_to_products_button(self):
        """Click the 'Back to products' button on the details page."""
        button = self.wait.until(EC.element_to_be_clickable(self.BACK_TO_PRODUCTS_BUTTON))
        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)
        if not self.wait_for_url_contains("/inventory.html"):
            self.driver.back()
            self.wait_for_url_contains("/inventory.html")
        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(self.INVENTORY_CONTAINER)
        )

    def logout(self):
        """Perform logout from the inventory page."""
        try:
            menu_button = self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU_BUTTON))
        except TimeoutException:
            menu_button = self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU))
        self.driver.execute_script("arguments[0].click();", menu_button)

        try:
            self.wait.until(EC.visibility_of_element_located(self.SIDE_MENU_WRAPPER))
        except TimeoutException:
            pass
        
        logout_link = self.wait.until(EC.presence_of_element_located(self.LOGOUT_LINK))
        self.driver.execute_script("arguments[0].click();", logout_link)

        WebDriverWait(self.driver, self.default_timeout).until(
            lambda d: "inventory" not in d.current_url.lower()
        )
        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located((By.ID, "login-button"))
        )
