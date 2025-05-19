from pathlib import Path
import pytest
import logging
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

logging.basicConfig(
    filename='report/test_report.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

featureFileDir = "features"
featureFile = "login.feature"
Base_Dir = Path(__file__).resolve().parent
Feature_File = Base_Dir.joinpath(featureFileDir).joinpath(featureFile)


@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@scenario(Feature_File, "User opens the login page")
def test_login():
    pass


@given('I open the StackOverflow login page')
def open_login_page(driver):
    driver.get("https://stackoverflow.com/users/login")
    logging.info("Opened StackOverflow login page")
    assert "Log In" in driver.title


@when("I enter the username 'zhomart.begaly@gmail.com' and password 'Zhomart981005'")
def enter_credentials(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "email"))
    ).send_keys("zhomart.begaly@gmail.com")
    logging.info("Entered username")
    driver.find_element(By.ID, "password").send_keys("Zhomart981005")
    logging.info("Entered password")


@when('I click the login button')
def click_login_button(driver):
    driver.find_element(By.ID, "submit-button").click()
    logging.info("Clicked Login button")


@then('I should be successfully logged into the site')
def successfully_login(driver):
    time.sleep(3)
    logging.info("Checked login result")
    driver.save_screenshot("report/account_page.png")
