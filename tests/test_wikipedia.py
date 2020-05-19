from unittest.mock import Mock

import click
import pytest
from src.x_ae_a_12 import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    """
	It selects the specified Wikipedia language edition.
	:param mock_requests_get:
	:return:
	"""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    """Tests if a page datatype is returned."""
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)


def test_random_page_handles_validation_errors(mock_requests_get: Mock) -> None:
    """Tests if validation errors are handled."""
    mock_requests_get.return_value.__enter__.return_value.json.return_value = None
    with pytest.raises(click.ClickException):
        wikipedia.random_page()


def test_trigger_typeguard(mock_requests_get: Mock) -> None:
    """Tests if typeguard has been triggered."""
    import json

    data = json.loads('{"language": 1}')
    wikipedia.random_page(language=data["language"])
