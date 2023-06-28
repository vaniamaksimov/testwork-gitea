from dataclasses import dataclass

from selenium.webdriver.common.by import By

from locators.base import BasePageLocators
from locators.footer import FooterLocators
from locators.header import UnloggedHeaderLocators


@dataclass
class LoginLocators(BasePageLocators, FooterLocators, UnloggedHeaderLocators):
    user_name_input = By.CSS_SELECTOR, '#user_name'
    password_input = By.CSS_SELECTOR, '#password'
    enter_button = By.XPATH, '//button[contains(text(), "Вход")]'
    forgot_password = By.CSS_SELECTOR, 'a[href*="/forgot_password"]'
    register_link = By.XPATH, '//a[contains(text(), "Нужен аккаунт?")]'
