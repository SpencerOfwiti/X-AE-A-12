from dataclasses import dataclass

import click
import desert
import marshmallow
import requests

API_URL: str = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


@dataclass
class Page:
    title: str
    extract: str


schema = desert.schema(Page, meta={"unknown": marshmallow.EXCLUDE})


def random_page(language: str = "en") -> Page:
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
            data = response.json()
            return schema.load(data)
    except (requests.RequestException, marshmallow.ValidationError) as error:
        message = str(error)
        raise click.ClickException(message)
