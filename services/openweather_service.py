from typing import Optional

import httpx
from loguru import logger

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
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    forecast = data["main"]

    return forecast
