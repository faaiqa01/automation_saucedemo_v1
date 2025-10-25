from selenium.webdriver.common.by import By
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
    
    def logout(self):
        """Perform logout."""
        import time
        self.click(*self.BURGER_MENU)
        time.sleep(1)  # Wait for menu animation
        self.click(*self.LOGOUT_LINK)
