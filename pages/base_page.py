from abc import ABC, abstractmethod
from typing import Protocol

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.header import UnloggedHeaderLocators
from locators.login import LoginLocators
from utils.app_types import Driver


class Page(ABC):
    def __init__(self, browser: Driver, url: str, timeout: int | float = 1) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    @abstractmethod
    def open(self) -> None:
        """Открывает страницу."""

    @abstractmethod
    def element_present(self, method: By, selector: str) -> bool:
        """Проеряет присуствие элемента на странице"""

    @abstractmethod
    def not_element_present(self, method: By, selector: str) -> bool:
        """Проверят отсуствие элемента на странице"""


class BasePage(Page):
    def open(self) -> None:
        self.browser.get(self.url)

    def element_present(self, method: By, selector: str) -> bool:
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def not_element_present(
        self, method: By, selector: str, timeout: int | float = 1
    ) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, selector))
            )
        except TimeoutException:
            return True
        return False

    def element_visable(
        self, method: By, selector: str, timeout: int | float = 1
    ) -> bool:
        """Проверяет визуальное присуствие элемента на странице."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((method, selector))
            )
        except TimeoutException:
            return False
        return True


class PageProtocol(Protocol):
    @property
    def browser(self) -> WebDriver: ...

    @property
    def url(self) -> str: ...


class LoginMixin:
    """Миксин определяющий возможность перейти на страницу логина с текущей страницы."""

    def login(self: PageProtocol, login: str, password: str) -> None:
        """Логин на страницу."""
        login_link = self.browser.find_element(*UnloggedHeaderLocators.login_link)
        login_link.click()
        user_input = self.browser.find_element(*LoginLocators.user_name_input)
        user_input.send_keys(login)
        password_input = self.browser.find_element(*LoginLocators.password_input)
        password_input.send_keys(password)
        enter_button = self.browser.find_element(*LoginLocators.enter_button)
        enter_button.click()
