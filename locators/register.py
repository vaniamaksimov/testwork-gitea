from dataclasses import dataclass

from selenium.webdriver.common.by import By

from locators.base import BasePageLocators


@dataclass
class RegisterLocators(BasePageLocators):
    user_name_input = By.ID, 'user_name'
    email_input = By.ID, 'email'
    password_input = By.ID, 'password'
    retype_password_input = By.ID, 'retype'
    enter_button = By.XPATH, '//button[contains(text(), "Регистрация аккаунта")]'
    register_link = By.XPATH, '//a[contains(text(), "Уже есть аккаунт? Авторизуйтесь!")]'

    successfull_message = By.CSS_SELECTOR, 'div.ui.positive > p'
