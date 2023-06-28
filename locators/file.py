from dataclasses import dataclass

from selenium.webdriver.common.by import By

from locators.base import BasePageLocators


@dataclass
class FileLocators(BasePageLocators):
    code = By.CSS_SELECTOR, 'code.code-inner'
