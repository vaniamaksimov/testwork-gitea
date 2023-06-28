import pytest

from locators.create_repo import CreateRepoLocators
from locators.file import FileLocators
from locators.header import UnloggedHeaderLocators
from locators.main import LoggedInMainLocators
from locators.register import RegisterLocators
from locators.repo import InitRepoCodeLocators, RepoCreateFile
from pages.file_page import FilePage
from pages.main_page import MainPage
from pages.repo_page import RepoPage
from tests.conftest import DriverType


@pytest.mark.test_case
class TestCase1:
    """
    Произвести регистрацию нового пользователя с помощью Selenium;

    Создать новый репозиторий с произвольным именем с помощью Selenium;

    Создать коммит файла с произвольным именем и содержанием с помощью Selenium;

    Открыть файл в браузере с помощью Selenium, убедиться что текст в файле
    соответствует оригинальному тексту;
    """

    @pytest.fixture(autouse=True)
    def _driver(self, driver: DriverType):
        self.driver = driver

    def test_register(self, main_page_url: str):
        page = MainPage(self.driver, main_page_url)
        page.open()
        register_link = self.driver.find_element(*UnloggedHeaderLocators.register_link)
        register_link.click()
        user_name_input = self.driver.find_element(*RegisterLocators.user_name_input)
        user_name_input.send_keys('AnotherUsername')
        email_input = self.driver.find_element(*RegisterLocators.email_input)
        email_input.send_keys('AnotherUsername@mail.com')
        password_input = self.driver.find_element(*RegisterLocators.password_input)
        password_input.send_keys('AnotherUserPassword')
        retype_password_input = self.driver.find_element(*RegisterLocators.retype_password_input)
        retype_password_input.send_keys('AnotherUserPassword')
        self.driver.find_element(*RegisterLocators.enter_button).click()
        assert page.element_visable(*RegisterLocators.successfull_message)
        message_text = self.driver.find_element(*RegisterLocators.successfull_message)
        assert message_text.text == 'Учётная запись была успешно создана.'

    def test_create_repo(self, main_page_url: str):
        page = MainPage(self.driver, main_page_url)
        page.open()
        page.login('AnotherUsername', 'AnotherUserPassword')
        self.driver.find_element(*LoggedInMainLocators.create_dropdown_menu).click()
        self.driver.find_element(*LoggedInMainLocators.new_repo_dropdown_link).click()
        repo_name_input = self.driver.find_element(*CreateRepoLocators.repo_name_input)
        repo_name_input.send_keys('AnotherUsernameRepo')
        self.driver.find_element(*CreateRepoLocators.init_repo_checkbox).click()
        self.driver.find_element(*CreateRepoLocators.create_repo_button).click()
        current_url = self.driver.current_url
        expected_url = main_page_url + 'AnotherUsername/AnotherUsernameRepo'
        assert current_url == expected_url

    def test_commit_file(self, main_page_url: str):
        page = RepoPage(self.driver, main_page_url + 'AnotherUsername/AnotherUsernameRepo')
        page.open()
        page.login('AnotherUsername', 'AnotherUserPassword')
        self.driver.find_element(*InitRepoCodeLocators.add_file_dropdown_menu).click()
        self.driver.find_element(*InitRepoCodeLocators.new_file_menu_button).click()
        filename_input = self.driver.find_element(*RepoCreateFile.file_name_input)
        filename_input.send_keys('AnotherUserFile')
        self.driver.find_element(*RepoCreateFile.editor_area).click()
        self.driver.switch_to.active_element.send_keys('AnotherUserCode')
        self.driver.find_element(*RepoCreateFile.commit_button).click()
        current_url = self.driver.current_url
        expected_url = main_page_url + 'AnotherUsername/AnotherUsernameRepo/src/branch/main/AnotherUserFile'
        assert current_url == expected_url

    def test_text_file(self, main_page_url: str):
        page = FilePage(self.driver, main_page_url + 'AnotherUsername/AnotherUsernameRepo/src/branch/main/AnotherUserFile')
        page.open()
        page.login('AnotherUsername', 'AnotherUserPassword')
        code = self.driver.find_element(*FileLocators.code).text
        assert code == 'AnotherUserCode'
