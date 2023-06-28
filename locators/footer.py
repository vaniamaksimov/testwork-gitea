from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class FooterLocators:
    licenses_link = By.CSS_SELECTOR, 'a[href*="/assets"]'
    api_link = By.CSS_SELECTOR, 'a[href*="/api/swagger"]'
