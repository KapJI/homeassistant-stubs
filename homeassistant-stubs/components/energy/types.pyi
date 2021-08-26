from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any, TypedDict

class SolarForecastType(TypedDict):
    wh_hours: dict[str, Union[float, int]]

GetSolarForecastType: Any

class EnergyPlatform:
    @staticmethod
    async def async_get_solar_forecast(hass: HomeAssistant, config_entry_id: str) -> Union[SolarForecastType, None]: ...
