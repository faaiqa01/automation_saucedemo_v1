from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import TIMEOUT
from utils.wait_helpers import CustomWaitHelpers

class BasePage:
    def __init__(self, driver, default_timeout: int = TIMEOUT):
        self.driver = driver
        self.default_timeout = default_timeout
        self.wait = WebDriverWait(driver, default_timeout)
        self.wait_helpers = CustomWaitHelpers(driver, default_timeout)

    # --- Element finders ---
    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        try:
            self.wait.until(EC.presence_of_all_elements_located((by, value)))
        except TimeoutException:
            return []
        return self.driver.find_elements(by, value)

    # --- Interactions ---
    def click(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input_text(self, by, value, text: str, clear: bool = True):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        if clear:
            element.clear()
        element.send_keys(text)

    def select_by_value(self, by, value, option_value: str):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        Select(element).select_by_value(option_value)

    # --- Getters ---
    def get_text(self, by, value) -> str:
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        return element.text

    # --- Checks ---
    def is_displayed(self, by, value) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False

    def is_element_displayed(self, parent_element, by, value) -> bool:
        try:
            child = parent_element.find_element(by, value)
            return child.is_displayed()
        except Exception:
            return False

    # --- Navigation / Waits ---
    def wait_for_url_contains(self, partial_url: str, timeout: int | None = None) -> bool:
        try:
            WebDriverWait(self.driver, timeout or self.default_timeout).until(EC.url_contains(partial_url))
            return True
        except TimeoutException:
            return False
