from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class BaseHeader:
    main_link = By.CSS_SELECTOR, 'a[href="/"]'
    explore_link = By.CSS_SELECTOR, '.item[href*="/explore"]'
    help_link = By.CSS_SELECTOR, '#navbar > a:nth-child(3)[href*="docs.gitea.io"]'

@dataclass
class UnloggedHeaderLocators(BaseHeader):
    register_link = By.CSS_SELECTOR, 'div.right.menu a.item[href*="/user/sign_up"]'
    login_link = By.CSS_SELECTOR, 'div.right.menu a.item[href*="/user/login"]'


@dataclass
class LoggedInHeaderLocators(BaseHeader):
    issues_link = By.CSS_SELECTOR, '.item[href*="/issues"]'
    pulls_link = By.CSS_SELECTOR, '.item[href*="/pulls"]'
    milestones_link = By.CSS_SELECTOR, '.item[href*="/milestones"]'
    notifications_link = By.CSS_SELECTOR, 'a[href*="/notifications"].not-mobile'

    create_dropdown_menu = By.CSS_SELECTOR, '.ui.dropdown[data-tooltip-content="Создать…"]'
    new_repo_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="/repo/create"]'
    new_migrate_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="/repo/migrate"]'
    new_org_dropdown_link = By.CSS_SELECTOR, 'div.menu.left a.item[role="menuitem"][href*="/org/create"]'

    profile_dropdown_menu = By.CSS_SELECTOR, '.ui.dropdown[data-tooltip-content="Профиль и настройки..."]'
    profile_dropdown_link = By.CSS_SELECTOR, 'div.user-menu a:first-of-type'
    favorite_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="?tab=stars"]'
    notifications_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="/notifications/subscriptions"]'
    settings_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="/user/settings"]'
    help_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="https://docs.gitea.io"]'
    admin_menu_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][href*="/admin"]'
    logout_dropdown_link = By.CSS_SELECTOR, 'a.item[role="menuitem"][data-url*="/user/logout"]'
