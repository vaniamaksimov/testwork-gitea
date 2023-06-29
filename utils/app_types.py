from typing import TypeAlias, TypeVar

from selenium.webdriver.remote.webdriver import WebDriver

Driver = TypeVar("Driver", bound=WebDriver)
HttpPort: TypeAlias = int
SSHPort: TypeAlias = int
