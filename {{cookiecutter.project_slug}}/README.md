{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{% else %}
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Documentation: <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}>
* GitHub: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
* PyPI: <https://pypi.org/project/{{ cookiecutter.project_slug }}/>
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}


## Setup


### Get it running

The preferred setup is that you have a directory named `{{ cookiecutter.project_slug }}` and inside that directory you have a `data` folder, the virtual environment and this repository.
Just follow these steps:


```bash
mkdir {{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
# create and load the virtual environment
python3 -m venv venv
source venv/bin/activate
# create the data folder
mkdir data
# clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
# Get poetry and update pip
pip install -U pip wheel poetry
poetry install
# now you can list the available nodes
python -m {{ cookiecutter.project_slug }} nodes
# or run the tests
make test
```

## Comand line interface

Make sure you have successfully run `poetry install` in the project directory.
You then can list and run the project nodes and also list previously runs.

### List nodes

To list all available nodes execute the following command:
```bash
python -m {{ cookiecutter.pkg_name }} nodes
```


### Run a node

The following command will run the FitOLS node:
```
python -m {{ cookiecutter.pkg_name }} run {{ cookiecutter.pkg_name }}.fit_ols.FitOLS \
    --dataset california_housing --target MedHouseVal
```

### List runs

This will list all runs:
```
python -m {{ cookiecutter.pkg_name }} ls
```

To list only runs starting with "FitOLS":
```
python -m {{ cookiecutter.pkg_name }} ls FitOLS
```

You can also select to list only runs completed in the last 3 hours:
```
python -m {{ cookiecutter.pkg_name }} ls FitOLS --completed --last 3h
```

### Delete runs

The cli to delete runs is similar to the one to list runs:

```
python -m {{ cookiecutter.pkg_name }} rm FitOLS --failed --last 3h
```
Would ask for confirmation before deleting all completed runs in the last 3 hours.
You can use the `--force` flag to skip the confirmation.

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/berleon/savethat_cookiecutter/) project template.
