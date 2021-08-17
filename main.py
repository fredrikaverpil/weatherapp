import json
from pathlib import Path

import fastapi
import uvicorn

from loguru import logger
from starlette.staticfiles import StaticFiles

from views import home
from api import weather_api
from services import openweather_service

app = fastapi.FastAPI()


def configure_api_keys():
    file = Path("settings.json").absolute()
    if not file.exists():
        logger.warning(
            f"WARNING: {file} file not found, you cannot continue, please see settings_template.json"
        )
        raise Exception(
            "settings.json file not found, you cannot continue, please see settings_template.json"
        )

    with open("settings.json") as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get("api_key")


def configure_routing():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(weather_api.router)


def configure():
    configure_routing()
    configure_api_keys()


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    # production use, for running using command
    # $ uvicorn main:app
    configure()
