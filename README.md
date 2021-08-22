# weatherapp

### Install

Prerequisites:

* Poetry

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ poetry install
```

### Configure

Add your API key from openweather.org into a `settings.json` file in the root of this repo.

### Run

```bash
$ uvicorn main:app
```