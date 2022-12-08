import pytest

@pytest.fixture()          #1.setup module.


def design():
    print("#### hi ###")


def test_spam(design):
    print("hello")


def test_display(design):
    print("Welcome for learning")