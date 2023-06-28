import pytest
from pages.main_page import MainPage
from tests.conftest import DriverType

from locators.footer import FooterLocators


def test_guest_footer(driver: DriverType, main_page_url: str):
    page = MainPage(driver, main_page_url)
    page.open()
    assert page.element_visable(*FooterLocators.api_link)
    assert page.element_visable(*FooterLocators.licenses_link)

@pytest.mark.parametrize(
    argnames=['login', 'password'],
    argvalues=[
        ('gitea_admin', 'gitea_admin'),
        ('gitea_user', 'gitea_user'),
    ]
)
def test_user_footer(driver: DriverType, main_page_url: str, login: str, password: str):
    page = MainPage(driver, main_page_url)
    page.open()
    page.login(login, password)
    assert page.element_visable(*FooterLocators.api_link)
    assert page.element_visable(*FooterLocators.licenses_link)
