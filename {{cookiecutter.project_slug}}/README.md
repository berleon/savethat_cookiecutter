{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
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


To install this project, run:

```bash
mkdir {{ cookiecutter.project_slug }}                   # this directory will hold the code, data and venv
cd {{ cookiecutter.project_slug }}
python3 -m venv venv                                    # create and load the virtual environment
source venv/bin/activate
# create the data folder
mkdir data
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install -U pip wheel poetry
poetry install
python -m {{ cookiecutter.project_slug }} nodes         # now you can list the available nodes
make test                                               # or run the tests
```

## Command line interface

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

All failed runs from the last 3 hours can be deleted with:

```
python -m {{ cookiecutter.pkg_name }} rm FitOLS --failed --last 3h
```
The CLI would ask for confirmation before deleting all completed runs in the last 3 hours.
You can use the `--force` flag to skip the confirmation.
See `python -m {{ cookiecutter.pkg_name }} rm  --help ` for more information.

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/berleon/savethat_cookiecutter/) project template.
