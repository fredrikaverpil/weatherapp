import json
from typing import Optional

import fastapi
from fastapi import Depends

from models.location import Location
from models.validation_error import ValidationError
from services import openweather_service


router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(
    loc: Location = Depends(),
    units: Optional[str] = "metric",
):
    try:
        report = await openweather_service.get_report(
            loc.city, loc.state, loc.country, units
        )
        return report
    except ValidationError as e:
        # return fastapi.Response(status_code=e.status_code, content=e.error_msg)
        raise fastapi.HTTPException(
            status_code=e.status_code,
            detail=e.error_msg,
        )
