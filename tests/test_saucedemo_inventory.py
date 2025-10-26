import pytest
from page_objects.saucedemo_login_page import SaucedemoLoginPage
from page_objects.saucedemo_inventory_page import SaucedemoInventoryPage
from config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.saucedemo
@pytest.mark.inventory
class TestSaucedemoInventory:

    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        """Setup for each test method: Login and navigate to inventory page."""
        self.driver = driver
        self.login_page = SaucedemoLoginPage(driver, BASE_URL)
        self.inventory_page = SaucedemoInventoryPage(driver, BASE_URL)

        self.login_page.login(USERNAME, PASSWORD)
        self.inventory_page.wait_for_url_contains("/inventory.html")
        assert self.inventory_page.is_inventory_page_loaded(), "Inventory page should be displayed after login"
        assert self.inventory_page.get_page_title() == "Products", "Page title should be 'Products'"
        print(f"[OK] Berhasil login dan navigasi ke halaman inventaris sebagai {USERNAME}")

    @pytest.mark.positive
    def test_verify_inventory_page_elements(self):
        """Test to verify key elements on the inventory page."""
        print("\n=== Test: Verifikasi elemen halaman inventaris ===")
        assert self.inventory_page.is_sort_dropdown_displayed(), "Dropdown pengurutan harus terlihat"
        assert self.inventory_page.is_shopping_cart_icon_displayed(), "Ikon keranjang belanja harus terlihat"
        assert self.inventory_page.get_product_count() > 0, "Setidaknya satu produk harus ditampilkan"
        print("[OK] Elemen halaman inventaris terlihat dengan benar.")

    @pytest.mark.positive
    def test_sort_products_a_to_z(self):
        """Test sorting products by Name (A to Z)."""
        print("\n=== Test: Urutkan produk berdasarkan Nama (A ke Z) ===")
        self.inventory_page.select_sort_option("az")
        product_names = self.inventory_page.get_all_product_names()
        assert product_names == sorted(product_names), "Produk harus diurutkan dari A ke Z"
        print("[OK] Produk berhasil diurutkan dari A ke Z.")

    @pytest.mark.positive
    def test_sort_products_price_low_to_high(self):
        """Test sorting products by Price (low to high)."""
        print("\n=== Test: Urutkan produk berdasarkan Harga (rendah ke tinggi) ===")
        self.inventory_page.select_sort_option("lohi")
        product_prices = self.inventory_page.get_all_product_prices()
        # Convert prices to float for comparison
        float_prices = [float(price.replace('$', '')) for price in product_prices]
        assert float_prices == sorted(float_prices), "Produk harus diurutkan berdasarkan harga rendah ke tinggi"
        print("[OK] Produk berhasil diurutkan berdasarkan harga rendah ke tinggi.")

    @pytest.mark.positive
    def test_add_and_remove_item_from_cart(self):
        """Test adding and removing an item from the cart."""
        print("\n=== Test: Tambah dan hapus item dari keranjang ===")
        initial_cart_count = self.inventory_page.get_shopping_cart_count()
        assert initial_cart_count == 0, "Keranjang belanja harus kosong pada awalnya"

        # Add first item to cart
        self.inventory_page.add_item_to_cart(0) # Add the first product
        assert self.inventory_page.get_shopping_cart_count() == 1, "Keranjang belanja harus memiliki 1 item"
        assert self.inventory_page.is_remove_button_displayed(0), "Tombol 'Remove' harus terlihat"
        print("[OK] Item berhasil ditambahkan ke keranjang.")

        # Remove the item from cart
        self.inventory_page.remove_item_from_cart(0)
        assert self.inventory_page.get_shopping_cart_count() == 0, "Keranjang belanja harus kosong setelah penghapusan"
        assert self.inventory_page.is_add_to_cart_button_displayed(0), "Tombol 'Add to cart' harus terlihat"
        print("[OK] Item berhasil dihapus dari keranjang.")

    @pytest.mark.positive
    def test_navigate_to_product_details_and_back(self):
        """Test navigating to product details page and back to inventory."""
        print("\n=== Test: Navigasi ke detail produk dan kembali ===")
        product_name_on_inventory = self.inventory_page.get_product_name(0)
        self.inventory_page.click_product_title(0)

        self.inventory_page.wait_for_url_contains("/inventory-item.html")
        assert self.inventory_page.is_product_details_page_loaded(), "Halaman detail produk harus ditampilkan"
        product_name_on_details = self.inventory_page.get_product_details_name()
        assert product_name_on_details == product_name_on_inventory, "Nama produk di halaman detail harus cocok"
        print("[OK] Berhasil navigasi ke halaman detail produk.")

        self.inventory_page.click_back_to_products_button()
        self.inventory_page.wait_for_url_contains("/inventory.html")
        assert self.inventory_page.is_inventory_page_loaded(), "Harus kembali ke halaman inventaris"
        print("[OK] Berhasil kembali ke halaman inventaris.")

    @pytest.mark.positive
    def test_logout_from_inventory_page(self):
        """Test logout functionality from the inventory page."""
        print("\n=== Test: Logout dari halaman inventaris ===")
        self.inventory_page.logout()
        self.login_page.wait_for_url_contains("saucedemo.com")
        assert self.login_page.is_login_button_displayed(), "Tombol login harus terlihat setelah logout"
        print("[OK] Berhasil logout dari halaman inventaris.")
