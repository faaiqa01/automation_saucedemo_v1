# 📚 EXAMPLES FOLDER

Folder ini berisi **example files** untuk referensi dan learning purpose.

## 📁 Struktur

```
examples/
├── tests/                          # Example test cases
│   ├── test_example.py            # Basic examples
│   ├── test_pom_example.py        # Page Object Model examples
│   ├── test_with_enhancements.py  # Priority HIGH features demo
│   └── test_wait_and_logging.py   # Priority MEDIUM features demo
│
└── Pages/                          # Example Page Objects
    ├── login_page.py              # Login page POM example
    └── dashboard_page.py          # Dashboard page POM example
```

## 🎯 Purpose

File-file ini **TIDAK** untuk production use, tapi sebagai:
- ✅ Reference untuk cara menggunakan framework
- ✅ Learning material untuk team
- ✅ Demo fitur-fitur yang tersedia
- ✅ Template untuk membuat test cases baru

## 📝 Cara Menggunakan

1. **Lihat examples** untuk understand cara kerja framework
2. **Copy & modify** sesuai kebutuhan project
3. **JANGAN** langsung run examples (locators tidak valid)
4. **BUAT** test cases baru di `tests/` folder

## 🔍 Apa yang Ada di Setiap File?

### **tests/test_example.py**
- 2 basic test cases
- Navigation example
- Form submission example

### **tests/test_pom_example.py**
- 4 test cases dengan Page Object Model
- Login validation (valid & invalid)
- Dashboard elements verification
- Logout functionality

### **tests/test_with_enhancements.py**
- Demo fitur prioritas tinggi:
  - Test data management
  - Environment configuration
  - Screenshot on failure

### **tests/test_wait_and_logging.py**
- Demo fitur prioritas sedang:
  - Custom wait helpers
  - Loading spinner handling
  - StepLogger usage
  - Logging levels

### **Pages/login_page.py**
- Example Login Page Object Model
- Generic locators (perlu disesuaikan)
- Methods: navigate_to_login(), enter_email(), login(), dll

### **Pages/dashboard_page.py**
- Example Dashboard Page Object Model
- Generic locators (perlu disesuaikan)
- Methods: navigate_to_dashboard(), logout(), dll

## ⚠️ PENTING

**File-file ini menggunakan generic selectors yang TIDAK akan work dengan aplikasi real!**

Anda perlu:
1. Inspect element dari aplikasi yang akan ditest
2. Update locators di Page Object Models
3. Sesuaikan test flow dengan aplikasi
4. Update test data di `tests/test_data.py`

## 🚀 Next Steps

1. Baca examples untuk understand framework
2. Buat Page Objects baru di `Pages/` folder (bukan di examples!)
3. Buat test cases baru di `tests/` folder (bukan di examples!)
4. Update `tests/test_data.py` dengan data real

---

**Happy Testing! 🎉**
