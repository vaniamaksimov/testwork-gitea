import socket
import uuid
from typing import Callable

import docker as dockerlib
import pytest


@pytest.fixture(scope='session')
def session_id() -> str:
    """Фикстура для определения id сессии тестирования."""
    return str(uuid.uuid4())


@pytest.fixture(scope='session')
def unused_port() -> Callable[[], int]:
    """Фикстура определяющая свободный порт."""
    def factory():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
            sckt.bind(('127.0.0.1', 0))
            return sckt.getsockname()[1]
    return factory


@pytest.fixture(scope='session')
def docker() -> dockerlib.DockerClient:
    """Клиент Docker для создания и работы с контейнерами."""
    return dockerlib.DockerClient(version='auto')
