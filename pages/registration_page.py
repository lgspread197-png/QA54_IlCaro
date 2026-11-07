# логин \ пароль - manuel@gmail.com   Manuel12345$
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[href='/register']")
    # REGISTRATION_LINK = (By.CSS_SELECTOR, "div[class='header '] a:nth-child(5)")
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    TERM_OF_USE_CHECK_BOX = (By.CSS_SELECTOR, "#terms-of-use")
    BUTTON_REGISTRATION = (By.XPATH, "//button[contains(text(),'Y’alla!')]")


    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()

    def fill_first_name_field(self, firstname):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(firstname)

    def fill_last_name_field(self, lastname):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(lastname)

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_policy(self):
        self.driver.find_element(*self.TERM_OF_USE_CHECK_BOX).click()

    def click_on_registration_button(self):
        self.driver.find_element(*self.BUTTON_REGISTRATION).click()


    def get_alert_text(self):
        alert = WebDriverWait(self.driver, timeout=10).until(
            expected_conditions.alert_is_present()
        )
        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()