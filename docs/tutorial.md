# Tutorial

??? Note
    Did you find this article confusing? [Edit this file] and pull a request!

To start with, you will need [GitHub], [PyPI], [TestPyPI] and [Codecov] account. If
you don't have one, please follow the links to apply one before you get started on this
tutorial.

If you are new to Git and GitHub, you should probably spend a few minutes on
some tutorials at the top of the page at [GitHub Help].

## Step 1: Create directory structure

We will create a directory structure like this:
```
my_project
├── my_project      # the source code
├── data_storage    # the run's data will be stored here
└── venv            # the virtual environment
```

Let's first create the top-level directory and the data_storage
```bash
mkdir my_project
cd my_project
mkdir data_storage
```
Next, we create the virtual environment inside of the `my_project` folder.
```bash
python3 -m venv venv
```
Let's update pip and install cookiecutter.
```
source venv/bin/activate
pip install -U pip wheel cookiecutter
```

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Run the following command and feed with answers, If you don’t know what to enter, stick with the defaults:

```bash
cookiecutter https://github.com/waynerv/cookiecutter-pypackage.git
```

Finally, a new folder will be created under current folder, the name is the answer you
provided to `project_slug`.

Go to this generated folder, the project layout should look like:

```
my_project
├── docs
│   ├── api.md
│   ├── changelog.md
│   ├── contributing.md
│   ├── index.md
│   ├── installation.md
│   └── usage.md
├── my_package
│   ├── fit_ols.py
│   ├── __init__.py
│   └── __main__.py
├── .github
│   ├── ISSUE_TEMPLATE.md
│   └── workflows
│       ├── dev.yml
│       ├── preview.yml
│       └── release.yml
├──── tests
│   ├── conftest.py
│   ├── __init__.py
│   └── test_fit_ols.py
├── .editorconfig
├── .bumpversion.cfg
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── makefile
├── mkdocs.yml
├── pyproject.toml
├── README.md
└── setup.cfg
```

Here the project_slug is `my_package`, when you generate yours, it could have another name.

Also be noticed that there's `pyproject.toml` in this folder. This is the main configuration file of our project.

## Step 3: Install Poetry

In this step we will install Poetry if you are not using it, since the whole project is managed by it.

```bash
pip install poetry
```

## Step 4: Install Requirements

You should still be in the folder named as `project_slug`, which containing the
 `pyproject.toml` file.

Install the new project's local development requirements with `poetry install`:

``` bash
poetry install
poetry run tox
```

Poetry will create its own virtualenv isolated from your system and install the dependencies in it.

We also launch a smoke test here by running `poetry run tox`. This will run
`tox` within created virtual environment, give you a test report and lint
report. You should see no errors except some lint warnings.

You can also activate the virtual environment manually with `poetry shell`, this will create a new shell.

??? Tips

    if you found erros like the following during tox run:
    ```
    ERROR: InterpreterNotFound: python3.9
    ```
    don't be panic, this is just because python3.x is not found on your machine. If you
    decide to support that version of Python in your package, please install it on your
    machine. Otherwise, remove it from tox.ini and pyproject.toml (search python3.x then
    remove it).

## Step 5: Setup Backblaze

If you do not have an account you have to [sign up at Backblaze] first.
Then you can create a new bucket under `B2 Cloud Storage` -> `Buckets`
and generate and application key for it under `Account` -> `App Keys`.

When you have them at hand, run:
```bash
python -m my_package setup_b2
```
You will ask you for your key information and bucket name.


## Step 6: Run a first Node

The generated project includes an exemplary node. You can run it with:

```bash
python -m my_package run FitOLS --dataset california_housing --target MedHouseVal
```
See the generated `README.md` for more information about the CLI.
The saved output is in the `data_storage` folder.

## Step 7: Create a GitHub Repo

Go to your GitHub account and create a new repo named `my_package`, where
`my_package` matches the `project_slug` from your answers to running
cookiecutter.

Then go to repo > settings > secrets, click on 'New repository secret', add the following
 secrets:

- TEST_PYPI_API_TOKEN, see [How to apply TestPyPI token]
- PYPI_API_TOKEN, see [How to apply pypi token]
- PERSONAL_TOKEN, see [How to apply personal token]

## Step 8: Set Up codecov integration

???+ Tips

    If you have already setup codecov integration and configured access for all your
    repositories, you can skip this step.

In your browser, visit [install codecov app], you'll be landed at this page:

![](http://images.jieyu.ai/images/202104/20210419175222.png)

Click on the green `install` button at top right, choose `all repositories` then click
on `install` button, following directions until all set.

If the repo you created is a private repo, you need to set the following additional secrets,
which is not required for public repos:

- CODECOV_TOKEN, see [Codecov GitHub Action - Usage](https://github.com/marketplace/actions/codecov?version=v1.5.2#usage)

## Step 9: Upload code to GitHub

Back to your develop environment, find the folder named after the `project_slug`.
Move into this folder, and then setup git to use your GitHub repo and upload the
code:

``` bash
cd my_package

git add .
git commit -m "Initial commit."
git branch -M main
git remote add origin git@github.com:myusername/my_package.git
git push -u origin main
```

Where `myusername` and `my_package` are adjusted for your username and
repo name.

You'll need a ssh key to push the repo. You can [Generate] a key or
[Add] an existing one.

???+ Warning

    if you answered 'yes' to the question if install pre-commit hooks at last step,
    then you should find pre-commit be invoked when you run `git commit`, and some files
     may be modified by hooks. If so, please add these files and **commit again**.

### Check result

After pushing your code to GitHub, goto GitHub web page, navigate to your repo, then
click on actions link, you should find screen like this:

![](http://images.jieyu.ai/images/202104/20210419170304.png)

There should be some workflows running. After they finished, go to [TestPyPI], check if a
new artifact is published under the name `project_slug`.

## Step 10. Check documentation

Documentation will be published and available at *https://{your_github_account}.github.io/{your_repo}* once:

1. the commit is tagged, and the tag name is started with 'v' (lower case)
2. build/testing executed by GitHub CI passed

If you'd like to see what it's look like now, you could run the following command:

```
poetry run mkdocs serve
```

This will run the builtin development server for you to preview.

## Step 11. Make release to PyPI(optional)

The Github Actions can be used to make official release to PyPI. You have to uncomment the
PyPI action in the `.github/workflows/{preview.yml,release.yml}`] files.



[Edit this file]: https://github.com/waynerv/cookiecutter-pypackage/blob/master/docs/tutorial.md
[Codecov]: https://codecov.io/
[PYPI]: https://pypi.org
[GitHub]: https://github.com/
[TestPyPI]: https://test.pypi.org/
[GitHub Help]: https://help.github.com/
[Generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
[Add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[How to apply testpypi token]: https://test.pypi.org/manage/account/
[How to apply pypi token]: https://pypi.org/manage/account/
[How to apply personal token]: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
[install codecov app]: https://github.com/apps/codecov

[sign up at Backblaze]: https://www.backblaze.com/b2/sign-up.html?referrer=nopref
