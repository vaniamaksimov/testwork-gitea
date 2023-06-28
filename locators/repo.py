from dataclasses import dataclass

from selenium.webdriver.common.by import By

from locators.base import BasePageLocators


@dataclass
class RepoBaseLocators(BasePageLocators):
    ...


@dataclass
class InitRepoCodeLocators(RepoBaseLocators):
    go_to_file_link = By.XPATH, '//a[contains(text(), "Перейти к файлу")]'
    add_file_dropdown_menu = By.XPATH, '//span[contains(text(), "Добавить файл")]'
    new_file_menu_button = By.XPATH, '//a[contains(text(), "Новый файл")]'
    download_file_menu_button = By.XPATH, '//a[contains(text(), "Загрузить файл")]'
    patch_file_menu_button = By.XPATH, '//a[contains(text(), "Применить патч")]'
    repo_clone_https_button = By.ID, 'repo-clone-https'
    repo_clone_ssh_button = By.ID, 'repo-clone-ssh'
    repo_copy_link = By.ID, 'clipboard-btn'


class RepoCreateFile(RepoBaseLocators):
    file_name_input = By.ID, 'file-name'
    editor_area = By.CSS_SELECTOR, 'div[role="code"]'
    code_input = By.ID, 'edit_area'
    commit_summary_input = By.CSS_SELECTOR, 'input[name="commit_summary"]'
    commit_message_input = By.CSS_SELECTOR, 'textarea[name="commit_message"]'
    signed_off_checkbox = By.CSS_SELECTOR, 'input[name="signoff"]'
    current_branch_radio_button = By.CSS_SELECTOR, 'input[value="direct"]'
    new_branch_radio_button = By.CSS_SELECTOR, 'input[value="commit-to-new-branch"]'
    new_branch_input_field = By.CSS_SELECTOR, 'input[name="new_branch_name"]'
    commit_button = By.ID, 'commit-button'
    cancel_button = By.XPATH, '//a[contains(text(), "Отмена")]'
