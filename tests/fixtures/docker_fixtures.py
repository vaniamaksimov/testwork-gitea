import socket
from typing import Any, Callable
import uuid
import docker as dockerlib
import pytest


@pytest.fixture(scope='session')
def session_id() -> str:
    return str(uuid.uuid4())


@pytest.fixture(scope='session')
def unused_port() -> Callable[[], Any]:
    def factory():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
            sckt.bind(('127.0.0.1', 0))
            return sckt.getsockname()[1]
    return factory


@pytest.fixture(scope='session')
def docker() -> dockerlib.DockerClient:
    return dockerlib.DockerClient(version='auto')
