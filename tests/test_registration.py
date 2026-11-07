from pages.registration_page import RegistrationPage
import uuid

VALID_NAME = "Vova"
VALID_LAST_NAME = "Vladimir"
VALID_EMAIL = "manuel2356@gmail.com"
VALID_PASSWORD = "Manuel12345$"



def test_successful_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_first_name_field(VALID_NAME)
    registration_page.fill_last_name_field(VALID_LAST_NAME)
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_policy()
    registration_page.click_on_registration_button()

    # assert "You are logged in success" in registration_page.get_alert_text()
    # registration_page.accept_alert()
    assert registration_page.get_alert_text() == "You are logged in success"
    registration_page.accept_alert()


def test_registration_existed_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_first_name_field(VALID_NAME)
    registration_page.fill_last_name_field(VALID_LAST_NAME)
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_policy()
    registration_page.click_on_registration_button()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()