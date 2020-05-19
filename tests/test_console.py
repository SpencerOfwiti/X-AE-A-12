from unittest.mock import Mock

import click.testing
from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture
import requests
from src.x_ae_a_12 import console


@pytest.fixture
def runner() -> CliRunner:
    """
	Fixture for invoking command-line interfaces.
	:return:
	"""
    return click.testing.CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """
	Fixture for mocking wikipedia.random_page.
	:param mocker:
	:return:
	"""
    return mocker.patch("src.x_ae_a_12.wikipedia.random_page")


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """
	Test it exits with a status code of 0.
	:param runner:
	:param mock_requests_get:
	:return:
	"""
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_title(runner: CliRunner, mock_requests_get: Mock) -> None:
    """
	Test it prints the title of the wikipedia page.
	:param runner:
	:param mock_requests_get:
	:return:
	"""
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output


def test_main_invokes_request_get(runner: CliRunner, mock_requests_get: Mock) -> None:
    """
	Test it invokes requests.get.
	:param runner:
	:param mock_requests_get:
	:return:
	"""
    runner.invoke(console.main)
    assert mock_requests_get.called


def test_main_uses_en_wikipedia_org(runner: CliRunner, mock_requests_get: Mock) -> None:
    """
	Test it uses English Wikipedia by default.
	:param runner:
	:param mock_requests_get:
	:return:
	"""
    runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """
	Test it exits with a non-zero status code if the request fails.
	:param runner:
	:param mock_requests_get:
	:return:
	"""
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(console.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """
	Test it prints an error message if the request fails.
	:param runner:
	:param mock_requests_get:
	:return:
	"""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


def test_main_uses_specified_language(
    runner: CliRunner, mock_wikipedia_random_page: Mock
) -> None:
    """
	Test it uses the specified edition of Wikipedia.
	:param runner:
	:param mock_wikipedia_random_page:
	:return:
	"""
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")


@pytest.mark.e2e
def test_main_succeeds_in_production_env(runner: CliRunner) -> None:
    """
	Test it exits with a status code of zero (end-to-end)
	:param runner:
	:return:
	"""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
