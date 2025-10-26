import pytest
from page_objects.saucedemo_login_page import SaucedemoLoginPage
from page_objects.saucedemo_inventory_page import SaucedemoInventoryPage
from config import BASE_URL, USERNAME, PASSWORD

# Valid credentials
VALID_USERNAME = USERNAME
VALID_PASSWORD = PASSWORD

@pytest.mark.saucedemo
@pytest.mark.positive
def test_login_with_valid_credentials(driver):
    """Test login with valid credentials - Positive Test."""
    
    print("\n=== Test: Login dengan kredensial valid ===")
    
    # Initialize page objects
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    inventory_page = SaucedemoInventoryPage(driver, BASE_URL)
    
    # Perform login
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    # Verify successful login - should redirect to inventory page
    inventory_page.wait_for_url_contains("/inventory.html")
    assert inventory_page.is_inventory_page_loaded(), "Inventory page should be displayed after login"
    assert inventory_page.get_page_title() == "Products", "Page title should be 'Products'"
    
    print("[OK] Login berhasil dengan kredensial valid")

@pytest.mark.saucedemo
@pytest.mark.negative
def test_login_with_invalid_username(driver):
    """Test login with invalid username - Negative Test."""
    
    print("\n=== Test: Login dengan username invalid ===")
    
    # Initialize page object
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    
    # Perform login with invalid username
    login_page.login("invalid_user", VALID_PASSWORD)
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_msg
    
    print(f"[OK] Error message ditampilkan: {error_msg}")

@pytest.mark.saucedemo
@pytest.mark.negative
def test_login_with_invalid_password(driver):
    """Test login with invalid password - Negative Test."""
    
    print("\n=== Test: Login dengan password invalid ===")
    
    # Initialize page object
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    
    # Perform login with invalid password
    login_page.login(VALID_USERNAME, "wrong_password")
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_msg
    
    print(f"[OK] Error message ditampilkan: {error_msg}")

@pytest.mark.saucedemo
@pytest.mark.negative
def test_login_with_empty_username(driver):
    """Test login with empty username - Negative Test."""
    
    print("\n=== Test: Login dengan username kosong ===")
    
    # Initialize page object
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    
    # Perform login with empty username
    login_page.login("", VALID_PASSWORD)
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Username is required" in error_msg
    
    print(f"[OK] Error message ditampilkan: {error_msg}")

@pytest.mark.saucedemo
@pytest.mark.negative
def test_login_with_empty_password(driver):
    """Test login with empty password - Negative Test."""
    
    print("\n=== Test: Login dengan password kosong ===")
    
    # Initialize page object
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    
    # Perform login with empty password
    login_page.login(VALID_USERNAME, "")
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Password is required" in error_msg
    
    print(f"[OK] Error message ditampilkan: {error_msg}")

@pytest.mark.saucedemo
@pytest.mark.negative
def test_login_with_empty_credentials(driver):
    """Test login with both username and password empty - Negative Test."""
    
    print("\n=== Test: Login dengan kredensial kosong ===")
    
    # Initialize page object
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    
    # Perform login with empty credentials
    login_page.login("", "")
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Username is required" in error_msg
    
    print(f"[OK] Error message ditampilkan: {error_msg}")

@pytest.mark.saucedemo
@pytest.mark.negative
def test_login_with_locked_user(driver):
    """Test login with locked out user - Negative Test."""
    
    print("\n=== Test: Login dengan locked user ===")
    
    # Initialize page object
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    
    # Perform login with locked user
    login_page.login("locked_out_user", VALID_PASSWORD)
    
    # Verify error message is displayed
    assert login_page.is_error_displayed(), "Error message should be displayed"
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out" in error_msg
    
    print(f"[OK] Error message ditampilkan: {error_msg}")

@pytest.mark.saucedemo
@pytest.mark.positive
def test_login_with_problem_user(driver):
    """Test login with problem user - Positive Test (user can login but has issues)."""
    
    print("\n=== Test: Login dengan problem user ===")
    
    # Initialize page objects
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    inventory_page = SaucedemoInventoryPage(driver, BASE_URL)
    
    # Perform login with problem user
    login_page.login("problem_user", VALID_PASSWORD)
    
    # Verify login is successful (even though it's a problem user)
    inventory_page.wait_for_url_contains("/inventory.html")
    assert inventory_page.is_inventory_page_loaded(), "Inventory page should be displayed"
    
    print("[OK] Problem user berhasil login (dengan masalah UI)")

@pytest.mark.saucedemo
@pytest.mark.positive
def test_login_with_performance_glitch_user(driver):
    """Test login with performance glitch user - Positive Test (slower but successful)."""
    
    print("\n=== Test: Login dengan performance glitch user ===")
    
    # Initialize page objects
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    inventory_page = SaucedemoInventoryPage(driver, BASE_URL)
    
    # Perform login with performance glitch user
    login_page.login("performance_glitch_user", VALID_PASSWORD)
    
    # Verify login is successful (may take longer)
    inventory_page.wait_for_url_contains("/inventory.html")
    assert inventory_page.is_inventory_page_loaded(), "Inventory page should be displayed"
    
    print("[OK] Performance glitch user berhasil login")

@pytest.mark.saucedemo
@pytest.mark.positive
def test_logout_after_login(driver):
    """Test logout functionality after successful login - Positive Test."""
    
    print("\n=== Test: Logout setelah login ===")
    
    # Initialize page objects
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    inventory_page = SaucedemoInventoryPage(driver, BASE_URL)
    
    # Perform login
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    # Verify successful login
    inventory_page.wait_for_url_contains("/inventory.html")
    assert inventory_page.is_inventory_page_loaded(), "Should be on inventory page"
    
    # Perform logout
    inventory_page.logout()
    
    # Verify logout - should redirect to login page
    login_page.wait_for_url_contains("saucedemo.com")
    
    print("[OK] Logout berhasil")


