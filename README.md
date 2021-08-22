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

### Debug

In vscode, create a `.vscode/launch.json` file for Python/FastAPI via its wizard, e.g:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app"
            ],
            "jinja": true
        }
    ]
}
```

Run app via vscode's debugger, set breakpoints, interact with the app and inspect via vscode's debugger.