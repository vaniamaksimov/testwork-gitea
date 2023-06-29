from dataclasses import dataclass

from selenium.webdriver.common.by import By

from .header import LoggedInHeaderLocators
from .footer import FooterLocators
from .base import BasePageLocators


@dataclass
class CreateRepoLocators(LoggedInHeaderLocators, FooterLocators, BasePageLocators):
    owner_dropdown_menu = By.XPATH, '//label[contains(text(), "Владелец")]/following-sibling::div'
    repo_name_input = By.ID, 'repo_name'
    repo_visability_checkbox = By.CSS_SELECTOR, 'input[name="private"]'
    repo_description_input = By.ID, 'description'
    repo_template_dropdown_menu = By.ID, 'repo_template_search'
    issue_labels_dropdown_menu = (
        By.XPATH,
        (
            '//div[@class="inline field"]/label[contains(text(), "Метки задач")]'
            '/following-sibling::div'
        ),
    )
    gitignore_template_dropdown_menu = (
        By.XPATH,
        '//div[@class="inline field"]/label[contains(text(), ".gitignore")]/following-sibling::div',
    )
    license_template_dropdown_menu = (
        By.XPATH,
        '//div[@class="inline field"]/label[contains(text(), "Лицензия")]/following-sibling::div',
    )
    license_choose_link = By.CSS_SELECTOR, 'a[href*="https://choosealicense.com"]'
    readme_template_dropdown_menu = (
        By.XPATH,
        '//div[@class="inline field"]/label[contains(text(), "README")]/following-sibling::div',
    )
    init_repo_checkbox = By.CSS_SELECTOR, 'div#auto-init > label'
    default_branch_input = By.ID, 'default_branch'
    subscription_trust_model_dropdown_menu = (
        By.XPATH,
        (
            '//div[@class="inline field"]/label[contains(text(), "Модель доверия подписи")]'
            '/following-sibling::div[contains(@class, "dropdown")]'
        ),
    )
    make_template_checkbox = By.CSS_SELECTOR, 'input[name="template"]'
    create_repo_button = By.CSS_SELECTOR, 'button.green.ui.button'
