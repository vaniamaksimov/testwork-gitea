import docker as dockerlib
import pytest
from _pytest.fixtures import SubRequest
from docker.models.containers import Container

from utils.app_browsers import BROWSERS
from utils.app_functions import healtcheck_gitea
from utils.app_types import Driver, HttpPort, SSHPort

_test_failed_incremental: dict[str, dict[tuple[int, ...], str]] = {}


pytest_plugins = [
    'tests.fixtures.docker_fixtures',
]


def pytest_addoption(parser: pytest.Parser):
    """Добавляем CLI опцию для запуска тестов на другом браузере."""
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser')


def pytest_runtest_makereport(item: pytest.Function, call: pytest.CallInfo):
    """
    Хук для вывода информации в консоль причины Xfail
    для тестов промаркированных test_case маркой.
    """
    if "test_case" in item.keywords:
        if call.excinfo is not None:
            cls_name = str(item.cls)
            parametrize_index = (
                tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
            )
            test_name = item.originalname or item.name
            _test_failed_incremental.setdefault(cls_name, {}).setdefault(
                parametrize_index, test_name
            )


def pytest_runtest_setup(item: pytest.Function):
    """Хук для маркировки test_case тестов маркой XFail в случае провала"""
    if "test_case" in item.keywords:
        cls_name = str(item.cls)
        if cls_name in _test_failed_incremental:
            parametrize_index = (
                tuple(item.callspec.indices.values()) if hasattr(item, "callspec") else ()
            )
            test_name = _test_failed_incremental[cls_name].get(parametrize_index, None)
            if test_name is not None:
                pytest.xfail(f"XFAIL / причина: {test_name} завершился ошибкой.")


@pytest.fixture(scope='session')
def gitea_ports(unused_port) -> tuple[HttpPort, SSHPort]:
    """Свободные порты для контейнера."""
    http_port = unused_port()
    ssh_port = unused_port()
    return http_port, ssh_port


@pytest.fixture(scope='session', autouse=True)
def create_gitea_container(
    docker: dockerlib.DockerClient, gitea_ports: tuple[HttpPort, SSHPort], session_id: str
) -> None:
    """Запускает локальный контейнер Gitea."""
    http_port, ssh_port = gitea_ports
    docker.images.pull('gitea/gitea', tag='latest')
    container: Container = docker.containers.run(
        name=f'gitea_{session_id}',
        image='gitea/gitea:latest',
        environment=['USER_UID=1000', 'USER_GID=1000', 'GITEA__security__INSTALL_LOCK=true'],
        ports={'3000/tcp': ('127.0.0.1', http_port), '22/tcp': ('127.0.0.1', ssh_port)},
        detach=True,
    )
    healtcheck_gitea(http_port)
    container.exec_run(
        (
            'su -c "gitea admin user create --username gitea_admin --password '
            'gitea_admin --email gitea_admin@gitea.com --admin --must-change-password=false" git'
        ),
        detach=True,
    )
    container.exec_run(
        (
            'su -c "gitea admin user create --username gitea_user --password '
            'gitea_user --email gitea_user@gitea.com --must-change-password=false" git'
        ),
        detach=True,
    )
    yield container
    container.kill()
    container.remove()
    docker.volumes.prune()


@pytest.fixture(scope='session')
def main_page_url(gitea_ports: tuple[HttpPort, SSHPort]) -> str:
    """Main page страницы с указанием назначенного HTTP порта Docker."""
    http_port, ssh_port = gitea_ports
    return f'http://127.0.0.1:{http_port}/'


@pytest.fixture
def driver(request: SubRequest) -> Driver:
    """yield фикстура вовращающая selenium драйвер."""
    browser_name = request.config.getoption('browser')
    if browser_name in BROWSERS:
        driver = BROWSERS.get(browser_name)()
    else:
        raise pytest.UsageError('Выбран не поддерживаемый драйвер')
    yield driver
    driver.quit()
