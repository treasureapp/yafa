# Yafa

Yet another finance app.

## Setup

1. Clone repo
    1. `git clone https://github.com/grahamcrowell/yafa`
    1. `cd yafa`
 1. Create and activate a new virtual environment
    - with built in [`venv` library](https://docs.python.org/3/library/venv.html):
        - create virtual environment in folder: `env`
        - `python3 -m venv env`
        - `source activate env/bin/activate`
        - terminal prompt now starts with `(env)`
    - with [Conda](https://conda.io/docs/user-guide/install/index.html):
        - create virtual environment named: `yafa`
        - `conda create --name yafa python=3`
        - `conda activate yafa`
        - terminal prompt now starts with `(yafa)`
1. Install Yafa into virtual environment
    - `pip install `[`--editable`](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)` .`
1. run tests
    - [`tox`](https://tox.readthedocs.io/en/latest/)
1. use library from Jupyter notebook
    - `jupyter notebook`
    - open `jupyter_bootbooks/main.ipynb`




