# 🚀 Quick Start Guide - Saucedemo Automation

## 📌 Quick Commands

### 1. Run All Tests
```bash
pytest tests\test_saucedemo_login.py -v
```

### 2. Run with Output
```bash
pytest tests\test_saucedemo_login.py -v -s
```

### 3. Run Positive Tests Only
```bash
pytest tests\test_saucedemo_login.py -m positive -v
```

### 4. Run Negative Tests Only
```bash
pytest tests\test_saucedemo_login.py -m negative -v
```

### 5. Generate HTML Report
```bash
pytest tests\test_saucedemo_login.py --html=reports/report.html --self-contained-html
```

### 6. Run Specific Test
```bash
pytest tests\test_saucedemo_login.py::test_login_with_valid_credentials -v -s
```

---

## 📊 Test Summary

| Category | Count | Status |
|----------|-------|--------|
| Positive Tests | 4 | ✅ ALL PASS |
| Negative Tests | 6 | ✅ ALL PASS |
| **TOTAL** | **10** | ✅ **100%** |

---

## 🎯 Valid Credentials

```
URL: https://www.saucedemo.com/v1/
Username: standard_user
Password: secret_sauce
```

---

## 📁 File Structure

```
├── Pages/
│   ├── saucedemo_login_page.py
│   └── saucedemo_inventory_page.py
├── tests/
│   ├── test_saucedemo_login.py
│   └── README_SAUCEDEMO.md
├── reports/
│   └── saucedemo_report.html
└── SUMMARY_SAUCEDEMO.md
```

---

## 🔍 What's Tested?

✅ Valid Login  
✅ Invalid Username  
✅ Invalid Password  
✅ Empty Username  
✅ Empty Password  
✅ Empty Credentials  
✅ Locked User  
✅ Problem User  
✅ Performance Glitch User  
✅ Logout Functionality  

---

## 📈 Results

- **Duration:** ~60 seconds
- **Success Rate:** 100%
- **Coverage:** Login & Logout features
- **Stability:** All tests stable & reliable

---

## 🎓 Features

✨ Page Object Model  
📸 Screenshot on Failure  
📝 Detailed Logging  
📊 HTML Reports  
🏷️ Test Markers  
🎯 Explicit Waits  

---

## 📖 Full Documentation

- **Complete Guide:** `tests/README_SAUCEDEMO.md`
- **Full Summary:** `SUMMARY_SAUCEDEMO.md`
- **Test Code:** `tests/test_saucedemo_login.py`

---

**Status:** ✅ PRODUCTION READY  
**Last Updated:** 26 Oktober 2025
