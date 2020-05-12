from src.x_ae_a_12 import wikipedia


def test_random_page_uses_given_language(mock_requests_get):
    """
	It selects the specified Wikipedia language edition.
	:param mock_requests_get:
	:return:
	"""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
