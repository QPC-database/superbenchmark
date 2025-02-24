---
id: development
---

# Development

If you want to develop new feature, please follow below steps to set up development environment.

## Check Environment

Follow [System Requirements](../getting-started/installation.md).

## Set Up

```bash
git clone https://github.com/microsoft/superbenchmark
cd superbenchmark

python3 -m pip install -e .[dev,test]
```

## Lint and Test

Format code using yapf.
```bash
python3 setup.py format
```

Check code style with mypy and flake8
```bash
python3 setup.py lint
```

Run unit tests.
```bash
python3 setup.py test
```

## Submit a Pull Request

Please install `pre-commit` before `git commit` to run all pre-checks.

```bash
pre-commit install
```

Open a pull request to main branch on GitHub.
