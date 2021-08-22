import json
from pathlib import Path

from loguru import logger
from starlette.staticfiles import StaticFiles
import fastapi
import uvicorn

from api import weather_api
from custom_logging.logger import init_logging
from services import openweather_service
from views import home


class APIKeyError(Exception):
    def __init__(self, message: str):
        logger.error(message)
        super().__init__(message)


app = fastapi.FastAPI()

init_logging()


def configure_api_key():
    key_file = Path("settings.json").absolute()
    if not key_file.exists():
        raise APIKeyError(
            f"{key_file} file not found, you cannot continue, "
            "please see settings_template.json"
        )

    with open(key_file) as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get("api_key")


def configure_routing():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(weather_api.router)


def configure():
    configure_routing()
    configure_api_key()


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    # production use, for running using command
    # $ uvicorn main:app
    configure()
