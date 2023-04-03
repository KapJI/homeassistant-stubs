from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Protocol, TypedDict

class SolarForecastType(TypedDict):
    wh_hours: dict[str, float | int]

GetSolarForecastType: Incomplete

class EnergyPlatform(Protocol):
    @staticmethod
    async def async_get_solar_forecast(hass: HomeAssistant, config_entry_id: str) -> SolarForecastType | None: ...
