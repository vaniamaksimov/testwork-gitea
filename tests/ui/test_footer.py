import pytest
from pages.main_page import MainPage
from tests.conftest import DriverType

from locators.footer import FooterLocators


@pytest.mark.parametrize(
    argnames=['login', 'password'],
    argvalues=[
        (None, None),
        ('gitea_admin', 'gitea_admin'),
        ('gitea_user', 'gitea_user'),
    ]
)
def test_footer(driver: DriverType, main_page_url: str, login: str, password: str):
    """Тест футера для анонимного / залогиненного пользователя / администратора."""
    page = MainPage(driver, main_page_url)
    page.open()
    if login and password:
        page.login(login, password)
    assert page.element_visable(*FooterLocators.api_link)
    assert page.element_visable(*FooterLocators.licenses_link)
