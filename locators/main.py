from dataclasses import dataclass

from selenium.webdriver.common.by import By

from .base import BasePageLocators
from .footer import FooterLocators
from .header import LoggedInHeaderLocators, UnloggedHeaderLocators


@dataclass
class UnloggedMainLocators(UnloggedHeaderLocators, FooterLocators, BasePageLocators):
    ...


@dataclass
class LoggedInMainLocators(LoggedInHeaderLocators, FooterLocators, BasePageLocators):
    user_dashboard = By.CSS_SELECTOR, 'div.dashboard-navbar div[role="menu"]'
