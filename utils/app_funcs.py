from http import HTTPStatus
from time import sleep

import requests


def healtcheck_gitea(http_port: int) -> None:
    """Health - check контейнера для ожидания полного запуска."""
    timeout = 0.001
    for i in range(100):
        try:
            response = requests.get(f'http://127.0.0.1:{http_port}/')
            if response.status_code == HTTPStatus.OK:
                return
            sleep(timeout)
            timeout *= 2
        except requests.exceptions.ConnectionError:
            sleep(timeout)
            timeout *= 2
    raise ConnectionError('docker container did not establish a connection')