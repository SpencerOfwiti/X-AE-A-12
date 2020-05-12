import click
import requests

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language="en"):
    """
	Return a random page.
	Perform a GET request to the /page/random/summary endpoint.
	:param language: The Wikipedia language edition.
	By default, the English Wikipedia is used ("en").
	:return: A page resource
	:raises ClickException:
	The HTTP request failed or the HTTP response contained an invalid body.
	"""
    url = API_URL.format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message)
