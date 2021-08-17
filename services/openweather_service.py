from typing import Optional

import httpx
from httpx import Response
from loguru import logger

from models.validation_error import ValidationError


api_key: Optional[str] = None


async def get_report(
    city: str, state: Optional[str], country: Optional[str], units: Optional[str]
) -> dict:

    logger.debug("Add caching here...")

    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"

    # https://openweathermap.org/current
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"

    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.json(), status_code=resp.status_code)

    data = resp.json()
    forecast = data["main"]

    return forecast
