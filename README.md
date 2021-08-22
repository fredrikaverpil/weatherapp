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

In vscode, add a `.vscode/launch.json` file for Python/FastAPI:

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
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