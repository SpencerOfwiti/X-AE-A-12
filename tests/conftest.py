import pytest


def pytest_configure(config):
    """
	Pytest configuration hook.
	:param config:
	:return:
	"""
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def mock_requests_get(mocker):
    """
	Fixture for mocking requests.get.
	:param mocker:
	:return:
	"""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock
