from typing import Callable

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.app_types import Driver


def get_chrome_driver() -> webdriver.Chrome:
    """Конфигурация Chrome браузера."""
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--ignore-ssl-errors")
    options.add_argument('--disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    return browser


BROWSERS: dict[str, Callable[[], Driver]] = {
    "chrome": get_chrome_driver,
}
