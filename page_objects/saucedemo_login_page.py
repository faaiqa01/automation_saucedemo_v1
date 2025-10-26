from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class SaucedemoLoginPage(BasePage):
    """Page Object Model for Saucedemo Login page."""
    
    # Locators
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    ERROR_BUTTON = (By.CLASS_NAME, "error-button")
    
    def __init__(self, driver, base_url):
        """
        Initialize login page.
        
        Args:
            driver: Selenium WebDriver instance
            base_url: Base URL of the application
        """
        super().__init__(driver)
        self.base_url = base_url
    
    def navigate_to_login(self):
        """Navigate to the login page."""
        self.driver.get(self.base_url)
    
    def enter_username(self, username):
        """
        Enter username.
        
        Args:
            username: Username string
        """
        self.input_text(*self.USERNAME_FIELD, username)
    
    def enter_password(self, password):
        """
        Enter password.
        
        Args:
            password: Password string
        """
        self.input_text(*self.PASSWORD_FIELD, password)
    
    def click_login_button(self):
        """Click the login button."""
        self.click(*self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """
        Perform login with credentials.
        
        Args:
            username: Username
            password: Password
        """
        self.navigate_to_login()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """
        Get error message text.
        
        Returns:
            Error message string
        """
        return self.get_text(*self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """
        Check if error message is displayed.
        
        Returns:
            Boolean
        """
        return self.is_displayed(*self.ERROR_MESSAGE)
    
    def clear_username(self):
        """Clear username field."""
        element = self.find_element(*self.USERNAME_FIELD)
        element.clear()
    
    def clear_password(self):
        """Clear password field."""
        element = self.find_element(*self.PASSWORD_FIELD)
        element.clear()

    def is_login_button_displayed(self):
        """Check if login button is visible (used after logout)."""
        return self.is_displayed(*self.LOGIN_BUTTON)
