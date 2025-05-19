
## 🧪 Script and Automation Features For SQA Final Project 

This project demonstrates comprehensive **Selenium automation** with the following implemented:

### ✅ Functionalities Implemented

1. **Login Automation** on [StackOverflow Login Page](https://stackoverflow.com/users/login)
2. **Dropdown Selection and Mouse Hover** on W3Schools select element playground

### ✅ Selenium Features Used

| Feature              | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| 🔄 **Implicit Wait** | Globally waits for up to 5 seconds when finding elements   |
| ⏱️ **Explicit Wait** | Waits for specific conditions like visibility of elements  |
| 🌀 **Fluent Wait**   | Implemented via `WebDriverWait` with custom poll frequency |
| 🎯 **Actions Class** | Mouse hover over elements using `ActionChains`             |
| 🧾 **Select Class**  | Dropdown interactions using Selenium's `Select` class      |

---

## ⚙️ TestNG-style Features (using Pytest and logging)

Although we're using **Pytest** instead of Java-based **TestNG**, equivalent features have been implemented:

| TestNG Feature                         | Pytest Equivalent                                                    |
| -------------------------------------- | -------------------------------------------------------------------- |
| `@BeforeClass`, `@Test`, `@AfterClass` | `@pytest.fixture`, test functions                                    |
| **Log Files**                          | `logging` module saves test logs to `report/test_report.txt`         |
| **Screenshots**                        | Captured after key steps and errors (saved in `screenshots/` folder) |
| **Test Reports**                       | Automatically logged; can be extended with `pytest-html` plugin      |

---

## 📝 BDD Integration

Also included:
**pytest-bdd** setup to demonstrate Gherkin syntax and behavior-driven testing.

| BDD Feature         | Status                                  |
| ------------------- | --------------------------------------- |
| Gherkin Scenario    | ✅ `login.feature`                       |
| Steps Implemented   | ✅ `@given`, `@when`, `@then` decorators |
| Selenium Automation | ✅ Integrated into BDD steps             |

---

## 📂 File Structure

```bash
project/
├── report/
│   └── test_report.txt          # Logs
├── screenshots/
│   └── *.png                    # Screenshots for test steps
├── features/
│   └── login.feature            # BDD Feature File
├── main.py              # Main functional test
└── stackOverflowTestScript.py           # BDD-style test
```

---

## 🚀 How to Run

Make sure you have installed the dependencies:

```bash
pip install selenium pytest pytest-bdd
```

Run the tests:

```bash
pytest test_script.py
pytest test_bdd_login.py
```

---

## 📌 Notes

* Update credentials (`email@gmail.com` and `password`) to valid test data before running.
* Ensure ChromeDriver is in your system path.
* This project can be uploaded to GitHub and used as a part of your **Final QA Automation Assignment**.

---

Teammembers: Duman Akhatov, Maxim Samodelkov, Yernur Bidollin, Begaly Zhomart
