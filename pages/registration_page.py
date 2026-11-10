from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    REGISTRATION_LINK = (By.CSS_SELECTOR, "[href='/register']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='lastName']")


    def __init__(self, driver):
        self.driver = driver

    def open_registration_page(self):
        self.driver.find_element(*self.REGISTRATION_LINK).click()


        self.driver.find_element(*self.LAST_NAME_INPUT).clear()

    def fill_email_field(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_policy(self):

        self.driver.find_element(*self.BUTTON_REGISTRATION).click()


        )
