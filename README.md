# weatherapp

### Install

Prerequisites:

- Poetry

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

Then use the endpoint. Example:

```bash
curl http://127.0.0.1:8000/api/weather/Stockholm
{"temp":0.57,"feels_like":-5.36,"temp_min":-0.65,"temp_max":1.2,"pressure":1009,"humidity":95,"sea_level":1009,"grnd_level":970}%
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
      "args": ["main:app"],
      "jinja": true
    }
  ]
}
```

Run app via vscode's debugger, set breakpoints, interact with the app and inspect via vscode's debugger.

Access Swagger UI at http://127.0.0.1:8000/docs
