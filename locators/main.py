from dataclasses import dataclass

from selenium.webdriver.common.by import By

from .header import UnloggedHeaderLocators, LoggedInHeaderLocators
from .footer import FooterLocators
from .base import BasePageLocators


@dataclass
class UnloggedMainLocators(UnloggedHeaderLocators, FooterLocators, BasePageLocators):
    ...


@dataclass
class LoggedInMainLocators(LoggedInHeaderLocators, FooterLocators, BasePageLocators):
    user_dashboard = By.CSS_SELECTOR, 'div.dashboard-navbar div[role="menu"]'