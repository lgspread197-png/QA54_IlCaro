import random
import uuid

from models.user import User
from pages.registration_page import RegistrationPage

def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1,1000000)
    random_suffix = uuid.uuid4().hex[:8]
    user = User(
        first_name="TestUser135",
        last_name="TestUser1235",
        email=f"qwer5{random_suffix}@gm.com",
        password="Aa_12345!"

    )
    print(random_suffix)
    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.confirmation1() == "Registered"
    assert registration_page.confirmation2() == "You are logged in success"
    registration_page.close_window()

def test_invalid_registration_with_empty_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="",
        last_name="TestUser12357",
        email="qwer1@gm.com",
        password="Aa_12345!"
    )
    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.error_message_text() == "Name is required"
    assert registration_page.submit_button_disabled()








# def test_registration_success(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_first_name_field(VALID_NAME)
#     registration_page.fill_last_name_field(VALID_LAST_NAME)
#     registration_page.fill_email_field(VALID_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.click_policy()
#     registration_page.click_registration_button()
#
#     # assert "You are logged in success" in registration_page.get_alert_text()
#     # registration_page.accept_alert()
#     assert registration_page.get_alert_text() == "You are logged in success"
#     registration_page.accept_alert()
#
#
# def test_registration_existed_user(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_page()
#     registration_page.fill_first_name_field(VALID_NAME)
#     registration_page.fill_last_name_field(VALID_LAST_NAME)
#     registration_page.fill_email_field(VALID_EMAIL)
#     registration_page.fill_password_field(VALID_PASSWORD)
#     registration_page.click_policy()
#     registration_page.click_registration_button()
#
#     assert registration_page.get_alert_text() == "User already exist"
#     registration_page.accept_alert()