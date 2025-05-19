import pytest
import logging
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# Create folders if not exist
if not os.path.exists('report'):
    os.makedirs('report')
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

# Logging setup
log_file = os.path.join('report', 'test_report.txt')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # ✅ Implicit wait
    driver.implicitly_wait(5)

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestStackOverflowLogin:

    def test_open_login_page(self):
        self.driver.get("https://stackoverflow.com/users/login")
        logging.info("Opened StackOverflow login page")
        self.driver.save_screenshot("screenshots/login_page.png")
        assert "Log In" in self.driver.title

    def test_login_attempt(self):
        try:
            # ✅ Explicit wait
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "email"))
            ).send_keys("email@gmail.com")
            logging.info("Entered username")

            self.driver.find_element(By.ID, "password").send_keys("password")
            logging.info("Entered password")

            # ✅ Fluent-style wait using WebDriverWait
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
            submit_btn = wait.until(lambda driver: driver.find_element(By.ID, "submit-button"))
            submit_btn.click()
            logging.info("Clicked Login button")

            time.sleep(3)
            self.driver.save_screenshot("screenshots/no_error_found.png")

        except Exception as e:
            logging.error(f"Login test failed: {e}")
            pytest.fail("Exception during login test")

    def test_actions_and_select(self):
        try:
            self.driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

            # Switch to iframe to access dropdown
            WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult"))
            )

            # ✅ Select class example
            dropdown = Select(self.driver.find_element(By.TAG_NAME, "select"))
            dropdown.select_by_visible_text("Opel")
            logging.info("Selected 'Opel' from dropdown")

            # ✅ Actions class example
            actions = ActionChains(self.driver)
            para = self.driver.find_element(By.XPATH, "//p")
            actions.move_to_element(para).perform()
            logging.info("Hovered over paragraph")

            self.driver.save_screenshot("screenshots/select_and_action.png")

        except Exception as e:
            logging.error(f"Actions/Select test failed: {e}")
            pytest.fail("Exception during action/select interaction")
