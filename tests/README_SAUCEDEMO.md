# Saucedemo Login Automation Test

Automation testing untuk halaman login website [Saucedemo](https://www.saucedemo.com/v1/) menggunakan Selenium, Python, dan Page Object Model (POM).

## 📋 Deskripsi

Project ini berisi automation test untuk menguji fungsionalitas login website Saucedemo dengan berbagai skenario:
- **Positive Tests**: Test dengan kredensial yang valid
- **Negative Tests**: Test dengan kredensial invalid, kosong, dan user yang terkunci

## 🏗️ Arsitektur

Project menggunakan **Page Object Model (POM)** pattern:
```
template_automation_selenium/
├── page_objects/                       # Page Object Models (POM)
│   ├── base_page.py                    # Base class untuk semua page objects
│   ├── saucedemo_login_page.py         # Page object untuk halaman login
│   └── saucedemo_inventory_page.py     # Page object untuk halaman inventory
├── Pages/                              # Folder untuk HTML files (jika ada)
├── tests/
│   └── test_saucedemo_login.py         # Test cases untuk login
├── conftest.py                          # Pytest fixtures dan configurations
└── config.py                            # Global configurations
```

## ✅ Test Cases

### Positive Tests (4 test cases)
1. ✓ `test_login_with_valid_credentials` - Login dengan kredensial valid
2. ✓ `test_login_with_problem_user` - Login dengan problem user
3. ✓ `test_login_with_performance_glitch_user` - Login dengan performance glitch user
4. ✓ `test_logout_after_login` - Logout setelah login berhasil

### Negative Tests (6 test cases)
1. ✓ `test_login_with_invalid_username` - Login dengan username invalid
2. ✓ `test_login_with_invalid_password` - Login dengan password invalid
3. ✓ `test_login_with_empty_username` - Login dengan username kosong
4. ✓ `test_login_with_empty_password` - Login dengan password kosong
5. ✓ `test_login_with_empty_credentials` - Login dengan kredensial kosong
6. ✓ `test_login_with_locked_user` - Login dengan locked out user

## 🚀 Cara Menjalankan Test

### Prasyarat
```bash
# Install dependencies
pip install -r requirements.txt
```

### Menjalankan Semua Test
```bash
pytest tests\test_saucedemo_login.py -v -s
```

### Menjalankan Test Berdasarkan Marker
```bash
# Menjalankan hanya positive tests
pytest tests\test_saucedemo_login.py -m positive -v

# Menjalankan hanya negative tests
pytest tests\test_saucedemo_login.py -m negative -v

# Menjalankan semua saucedemo tests
pytest tests\test_saucedemo_login.py -m saucedemo -v
```

### Menjalankan Test Spesifik
```bash
pytest tests\test_saucedemo_login.py::test_login_with_valid_credentials -v -s
```

### Generate HTML Report
```bash
pytest tests\test_saucedemo_login.py --html=reports/saucedemo_report.html --self-contained-html
```

## 📊 Fitur Automation

- ✨ **Page Object Model (POM)**: Kode terstruktur dan mudah di-maintain
- 📸 **Screenshot on Failure**: Otomatis capture screenshot saat test gagal
- 📝 **Logging**: Logging detail untuk tracking eksekusi test
- 📈 **HTML Report**: Generate HTML report otomatis dengan pytest-html
- 🎯 **Explicit Waits**: Menggunakan WebDriverWait untuk stabilitas test
- 🏷️ **Test Markers**: Kategorisasi test dengan pytest markers

## 🎯 Valid Test Credentials

```python
Username: standard_user
Password: secret_sauce
```

### Users Lainnya:
- `locked_out_user` - User yang terkunci (akan gagal login)
- `problem_user` - User dengan masalah UI
- `performance_glitch_user` - User dengan performance delay

## 📁 Artifacts

Hasil test akan disimpan di:
- **Screenshots**: `artifacts/screenshots/` - Screenshot saat test gagal
- **Logs**: `artifacts/logs/` - Log file eksekusi test
- **Reports**: `reports/` - HTML test reports

## 🛠️ Technology Stack

- **Python 3.11+**
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **pytest-html** - HTML report generation
- **Page Object Model** - Design pattern

## 📝 Catatan

- Browser Chrome akan dibuka otomatis saat menjalankan test
- Test berjalan sekitar 1-2 menit untuk 10 test cases
- Screenshot otomatis diambil jika test gagal
- HTML report otomatis di-generate setelah test selesai
