# X-AE-A-12

[![Tests](https://github.com/SpencerOfwiti/X-AE-A-12/workflows/Tests/badge.svg)](https://github.com/SpencerOfwiti/X-AE-A-12/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/SpencerOfwiti/X-AE-A-12/branch/master/graph/badge.svg)](https://codecov.io/gh/SpencerOfwiti/X-AE-A-12)
[![PyPI](https://img.shields.io/pypi/v/x-ae-a-12.svg)](https://pypi.org/project/x-ae-a-12/)
[![Read the Docs](https://readthedocs.org/projects/x-ae-a-12/badge/)](https://x-ae-a-12.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![GitHub repo size](https://img.shields.io/github/repo-size/SpencerOfwiti/X-AE-A-12.svg)
![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![contributors](https://img.shields.io/github/contributors/SpencerOfwiti/X-AE-A-12.svg)](https://github.com/SpencerOfwiti/X-AE-A-12/contributors)

Command line application for displaying random facts from wikipedia on the console.
Available as a python package on PyPI:
```
pip install x-ae-a-12
```
Documentation available at: [X-AE-A-12 docs](https://x-ae-a-12.readthedocs.io/en/latest/)

## Table of contents
* [Built With](#built-with)
* [Features](#features)
* [Code Example](#code-example)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Tests](#tests)
* [Deployment](#deployment)
* [Contributions](#contributions)
* [Bug / Feature Request](#bug--feature-request)
* [Authors](#authors)
* [License](#license)

## Built With
* [Python 3.8](https://www.python.org/) - The programming language used.
* [Poetry](https://python-poetry.org/) - The dependency manager used.
* [Nox](https://nox.thea.codes/en/stable/) - The automation tool used.
* [Pytest](https://docs.pytest.org/en/latest/) - The testing framework used.
* [Flake8](https://flake8.pycqa.org/en/latest/) - The linting tool used.
* [Sphinx](https://www.sphinx-doc.org/en/master/) - The documentation generator used.
* [GitHub Actions](https://github.com/actions) - CI-CD tool used.

## Features

- Display random facts from Wikipedia.
- Select Wikipedia language edition to be used.

## Code Example

```python
def main(language: str) -> None:
    """The X-AE-A-12 Python project."""
    page = wikipedia.random_page(language=language)

    click.secho(page.title, fg="green")
    click.echo(textwrap.fill(page.extract))
```

## Prerequisites

What things you need to install the software and how to install them

* **python 3.8**

Linux:
```
sudo apt-get install python3.8
```

Windows:

Download from [python.org](https://www.python.org/downloads/windows/)

Mac OS:
```
brew install python3
```

* **pip**

Linux and Mac OS:
```
pip install -U pip
```

Windows:
```
python -m pip install -U pip
```

* **poetry**
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

* **nox**
```
pip install --user --upgrade nox
```

## Installation

Clone this repository:
```
git clone https://github.com/SpencerOfwiti/X-AE-A-12
```

To set up virtual environment and install dependencies:
```
poetry install
```

To run application:
```
poetry run x-ae-a-12
```

## Tests

This system uses pytest to run automated tests.

To run automated tests:
```
nox -s tests
```

## Deployment

To deploy application on PyPI(Python Package Index):
```
poetry build
```

```
poetry publish
```

## Contributions

To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/SpencerOfwiti/X-AE-A-12/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/SpencerOfwiti/X-AE-A-12/issues/new). Please include sample queries and their corresponding results.

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work*

[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

See also the list of [contributors](https://github.com/SpencerOfwiti/X-AE-A-12/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
