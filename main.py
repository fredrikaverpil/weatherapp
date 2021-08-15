import fastapi
import uvicorn

from starlette.staticfiles import StaticFiles

from views import home
from api import weather_api

app = fastapi.FastAPI()


def configure_routing():
    app.mount("/static/", StaticFiles(directory="static"), name="static")
    app.include_router(home.router)
    app.include_router(weather_api.router)


def configure():
    configure_routing()


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    # production use, for running using command
    # $ uvicorn main:app
    configure()
