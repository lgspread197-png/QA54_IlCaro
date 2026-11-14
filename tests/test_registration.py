import random
import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1, 1000000)
    random_suffix = uuid.uuid4().hex[:8]
    user = User(
        first_name="TestUser1357",
        last_name="TestUser12357",
        email=f"qwer{random_suffix}@gm.com",
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
    assert registration_page.error_message_text1() == "Name is required"
    assert registration_page.submit_button_disabled()

def test_invalid_registration_with_empty_last_name(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="TestUser1357",
        last_name="",
        email="qwer1@gm.com",
        password="Aa_12345!"
    )
    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.error_message_text2() == "Last name is required"
    assert registration_page.submit_button_disabled()

def test_invalid_registration_with_wrong_format_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="TestUser1357",
        last_name="TestUser12357",
        email="qwer1gm.com",
        password="Aa_12345!"
    )
    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.error_message_text3() == "Wrong email format"
    assert registration_page.submit_button_disabled()

def test_invalid_registration_with_short_length_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        first_name="TestUser1357",
        last_name="TestUser12357",
        email="qwer1@gm.com",
        password="Aa_1!"
    )
    registration_page.open_registration_page()
    registration_page.fill_registration_form(user)
    assert registration_page.error_message_text4() == "Password must contain minimum 6 symbols"
    assert registration_page.submit_button_disabled()