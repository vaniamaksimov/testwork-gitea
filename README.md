# Тестовое задание на позицию "Инженер по автоматизации тестирования"

## Задача:

На примере сервиса Gitea https://github.com/go-gitea/gitea реализовать следующий тестовый сценарий:
- развернуть gitea локально в Docker с помощью pytest;
- дождаться пока контейнер запустится и убедиться что web-страница сервиса Gitea на целевом выбранном порту доступна и в ней находятся 3-5 эталонных CSS селектора и эталонный текст с помощью pytest/requests;
- произвести регистрацию нового пользователя с помощью Selenium;
- создать новый репозиторий с произвольным именем с помощью Selenium;
- создать коммит файла с произвольным именем и содержанием с помощью Selenium;
- открыть файл в браузере с помощью Selenium, убедиться что текст в файле соответствует оригинальному тексту;
- погасить контейнер;
- вывести отчёт о проведённых тестах в консоль.

Готовые тесты оформить в виде репозитория на Github/Gitlab с инструкцией по запуску теста.

## Установка и запуск проекта

### Для запуска проекта необходимо:
- для запуска проекта требуется python версии 3.10+
- склонировать репозиторий консольной командой `git clone git@github.com:vaniamaksimov/testwork-gitea.git`
- перейти в папку с проектом командой `cd testwork-gitea`
- установить зависимости с помощью poetry https://python-poetry.org/docs/basic-usage/ или воспользоваться пакетным менеджером pip, для этого:
    - устанавливаем виртуальное окружение командой `python -m venv venv` или `python3 -m venv venv` на unix системах
    - активируем виртуальное окружение командой `source venv/scripts/activate` или `source venv/bin/activate` на unix системах
    - устанавливаем зависимости командой `pip install -r requirements.txt`
- установить chromedriver по инструкции https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
- установить и запустить docker https://docs.docker.com/engine/install/

### Запуск тестов производится командами:
- Для запуска тестов описанных тест-кейсами использовать команду `pytest -m test_case`
- Для запуска ui тестов использовать команду `pytest -m ui`
- Для запуска всех тестов использовать команду `pytest`
