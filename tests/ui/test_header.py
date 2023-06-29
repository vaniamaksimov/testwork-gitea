import pytest
from pages.main_page import MainPage
from utils.app_types import Driver

from locators.header import LoggedInHeaderLocators, UnloggedHeaderLocators


def test_guest_header(driver: Driver, main_page_url: str):
    """Тест хидера для анонимного пользователя."""
    page = MainPage(driver, main_page_url)
    page.open()
    assert page.element_visable(*UnloggedHeaderLocators.main_link)
    assert page.element_visable(*UnloggedHeaderLocators.explore_link)
    assert page.element_visable(*UnloggedHeaderLocators.register_link)
    assert page.element_visable(*UnloggedHeaderLocators.login_link)
    assert page.element_visable(*UnloggedHeaderLocators.help_link)
    assert page.not_element_present(*LoggedInHeaderLocators.issues_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.pulls_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.milestones_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.notifications_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.create_dropdown_menu, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.new_repo_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.new_migrate_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.new_org_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.profile_dropdown_menu, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.profile_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.favorite_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.notifications_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.settings_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.help_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.admin_menu_dropdown_link, 1)
    assert page.not_element_present(*LoggedInHeaderLocators.logout_dropdown_link, 1)


@pytest.mark.parametrize(
    argnames=['login', 'password'],
    argvalues=[
        ('gitea_admin', 'gitea_admin'),
        ('gitea_user', 'gitea_user'),
    ],
)
def test_user_header(driver: Driver, main_page_url: str, login: str, password: str):
    """Тест хидера для зарегистрированного пользователя / администратора."""
    page = MainPage(driver, main_page_url)
    page.open()
    page.login(login, password)
    assert page.not_element_present(*UnloggedHeaderLocators.register_link)
    assert page.not_element_present(*UnloggedHeaderLocators.login_link)
    assert page.not_element_present(*UnloggedHeaderLocators.help_link)
    assert page.element_visable(*LoggedInHeaderLocators.main_link)
    assert page.element_visable(*LoggedInHeaderLocators.explore_link)
    assert page.element_visable(*LoggedInHeaderLocators.issues_link)
    assert page.element_visable(*LoggedInHeaderLocators.pulls_link)
    assert page.element_visable(*LoggedInHeaderLocators.milestones_link)
    assert page.element_visable(*LoggedInHeaderLocators.notifications_link)
    assert page.element_visable(*LoggedInHeaderLocators.create_dropdown_menu)
    assert not page.element_visable(*LoggedInHeaderLocators.new_repo_dropdown_link)
    assert not page.element_visable(*LoggedInHeaderLocators.new_migrate_dropdown_link)
    if login == 'gitea_admin':
        assert not page.element_visable(*LoggedInHeaderLocators.new_org_dropdown_link)
    else:
        assert page.not_element_present(*LoggedInHeaderLocators.new_org_dropdown_link)
    driver.find_element(*LoggedInHeaderLocators.create_dropdown_menu).click()
    assert page.element_visable(*LoggedInHeaderLocators.new_repo_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.new_migrate_dropdown_link)
    if login == 'gitea_admin':
        assert page.element_visable(*LoggedInHeaderLocators.new_org_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.profile_dropdown_menu)
    assert not page.element_visable(*LoggedInHeaderLocators.profile_dropdown_link)
    assert not page.element_visable(*LoggedInHeaderLocators.favorite_dropdown_link)
    assert not page.element_visable(*LoggedInHeaderLocators.notifications_dropdown_link)
    assert not page.element_visable(*LoggedInHeaderLocators.settings_dropdown_link)
    assert not page.element_visable(*LoggedInHeaderLocators.help_dropdown_link)
    if login == 'gitea_admin':
        assert not page.element_visable(*LoggedInHeaderLocators.admin_menu_dropdown_link)
    else:
        assert page.not_element_present(*LoggedInHeaderLocators.admin_menu_dropdown_link)
    assert not page.element_visable(*LoggedInHeaderLocators.logout_dropdown_link)
    driver.find_element(*LoggedInHeaderLocators.profile_dropdown_menu).click()
    assert page.element_visable(*LoggedInHeaderLocators.profile_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.favorite_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.favorite_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.notifications_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.settings_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.help_dropdown_link)
    if login == 'gitea_admin':
        assert page.element_visable(*LoggedInHeaderLocators.admin_menu_dropdown_link)
    assert page.element_visable(*LoggedInHeaderLocators.logout_dropdown_link)
