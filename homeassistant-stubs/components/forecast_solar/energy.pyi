from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant

async def async_get_solar_forecast(hass: HomeAssistant, config_entry_id: str) -> Union[dict[str, dict[str, Union[float, int]]], None]: ...
