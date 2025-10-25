# Selenium Automation Testing Project

Project automation testing menggunakan Selenium WebDriver dan Pytest dengan Page Object Model (POM) pattern.

## 🎯 Current Projects

### ✅ Saucedemo Login Automation
Automation testing untuk website https://www.saucedemo.com/v1/
- **10 Test Cases** (4 Positive + 6 Negative)
- **100% Success Rate**
- **Full Documentation** - Lihat `README_FINAL.txt` atau `SUMMARY_SAUCEDEMO.md`

**Quick Run:**
```bash
pytest tests\test_saucedemo_login.py -v
```

---

## Prerequisites
- Python 3.8+
- Google Chrome Browser
- ChromeDriver (auto-managed by Selenium Manager)

## Installation

1. Clone repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Create virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure credentials (optional for general use)
Edit `config.py` and update environment settings:
- ENVIRONMENTS (dev/staging/prod)
- Update BASE_URL, USERNAME, PASSWORD for each environment

## Running Tests

### Saucedemo Tests (Recommended)
```bash
# Run all saucedemo tests
pytest tests\test_saucedemo_login.py -v

# Run with detailed output
pytest tests\test_saucedemo_login.py -v -s

# Run only positive tests
pytest tests\test_saucedemo_login.py -m positive -v

# Run only negative tests
pytest tests\test_saucedemo_login.py -m negative -v

# Generate HTML report
pytest tests\test_saucedemo_login.py --html=reports/saucedemo_report.html --self-contained-html
```

### General Test Commands
```bash
# Run all tests
pytest -s --html=reports/report.html

# Run specific test file
pytest -s tests/test_example.py --html=reports/test_example.html

# Run specific test case
pytest -s tests/test_example.py::test_example_navigation

# Run tests by marker
pytest -s -m example_suite
```

Run tests with specific environment:
```bash
# Windows
set ENV=staging && pytest -s

# Linux/Mac
ENV=staging pytest -s
```

## Project Structure
```
project_root/
├── Pages/              # HTML files (untuk referensi)
├── page_objects/       # Page Object Models (POM) ✨
│   ├── base_page.py
│   ├── saucedemo_login_page.py
│   └── saucedemo_inventory_page.py
├── tests/              # Test cases
│   ├── test_saucedemo_login.py (10 test cases)
│   └── README_SAUCEDEMO.md
├── reports/            # HTML test reports
├── artifacts/          # Screenshots & logs
│   ├── screenshots/    # Auto-capture on failure
│   └── logs/          # Execution logs
├── utils/              # Helper utilities
├── conftest.py         # Pytest fixtures
├── config.py           # Configuration
├── pytest.ini          # Pytest settings
├── INDEX.md            # Navigation guide
├── README_FINAL.txt    # Complete summary
├── SUMMARY_SAUCEDEMO.md # Detailed documentation
└── QUICKSTART_SAUCEDEMO.md # Quick reference
```

## Features
- ✨ **Page Object Model (POM)** - Clean & maintainable architecture
- 🔐 **Chrome Popup Disabled** - No "Save Password" popups
- 📸 **Screenshot on Failure** - Auto-capture for debugging
- 📝 **Detailed Logging** - File & console output
- 📊 **HTML Reports** - Professional test reports
- 🎯 **Explicit Waits** - No sleep(), stable tests
- 🏷️ **Test Markers** - Easy categorization (positive/negative)
- 🌍 **Multi-Environment** - Support dev/staging/prod
- 🔄 **Reusable Components** - Base page with common methods
- 🚀 **Production Ready** - Best practices implemented

## Documentation

📚 **Start Here:**
1. **INDEX.md** - Navigation guide
2. **README_FINAL.txt** - Complete project summary
3. **QUICKSTART_SAUCEDEMO.md** - Quick commands
4. **SUMMARY_SAUCEDEMO.md** - Detailed documentation
5. **tests/README_SAUCEDEMO.md** - Test guide

## Saucedemo Test Coverage

### ✅ Positive Tests (4 test cases)
- Login dengan kredensial valid
- Login dengan problem user
- Login dengan performance glitch user
- Logout functionality

### ❌ Negative Tests (6 test cases)
- Invalid username
- Invalid password
- Empty username
- Empty password
- Empty credentials
- Locked user

**Result:** 10/10 PASSED (100% Success Rate)

## Chrome Configuration

Browser Chrome sudah dikonfigurasi untuk:
- ✅ Disable password manager popup
- ✅ Disable "Save password?" notification
- ✅ Disable automation banner
- ✅ Maximize window on start
- ✅ Clean browser experience

## Tips & Best Practices

1. **Use Page Object Model** - Semua locator di satu tempat
2. **Use Explicit Waits** - Hindari `time.sleep()`, gunakan `WebDriverWait`
3. **Use Test Markers** - Kategorisasi test dengan `@pytest.mark.xxx`
4. **Check HTML Reports** - Review hasil di folder `reports/`
5. **Check Screenshots** - Lihat `artifacts/screenshots/` saat test gagal
6. **Read Logs** - Check `artifacts/logs/` untuk detail eksekusi
7. **Run with -v -s** - Untuk output lebih detail
8. **Use Fixtures** - `driver` untuk basic, `logged_in_driver` untuk authenticated tests
9. **Follow POM Pattern** - Tambah page objects di `page_objects/`
10. **Document Your Tests** - Tambah docstring di setiap test function

## Quick Start Example

```python
# Import page objects
from page_objects.saucedemo_login_page import SaucedemoLoginPage
from page_objects.saucedemo_inventory_page import SaucedemoInventoryPage

def test_example(driver):
    """Example test case."""
    # Initialize page objects
    login_page = SaucedemoLoginPage(driver, BASE_URL)
    inventory_page = SaucedemoInventoryPage(driver, BASE_URL)
    
    # Perform actions
    login_page.login("standard_user", "secret_sauce")
    
    # Verify results
    assert inventory_page.is_inventory_page_loaded()
    assert inventory_page.get_page_title() == "Products"
```

## Support & Help

- 📖 Full documentation: `SUMMARY_SAUCEDEMO.md`
- 🚀 Quick commands: `QUICKSTART_SAUCEDEMO.md`
- 📋 Test guide: `tests/README_SAUCEDEMO.md`
- 🗺️ Navigation: `INDEX.md`

## Status

✅ **Saucedemo Automation** - COMPLETE & PRODUCTION READY
- 10 test cases implemented
- 100% success rate
- Full documentation
- Clean architecture
- Best practices followed

---

**Last Updated:** 26 Oktober 2025
**Version:** 1.0.0 - Saucedemo Login Complete
