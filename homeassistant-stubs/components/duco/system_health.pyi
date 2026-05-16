from .const import DOMAIN as DOMAIN
from .coordinator import DucoConfigEntry as DucoConfigEntry
from homeassistant.components import system_health as system_health
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_register(hass: HomeAssistant, register: system_health.SystemHealthRegistration) -> None: ...
async def _async_get_write_requests_remaining(config_entry: DucoConfigEntry) -> int | dict[str, str]: ...
async def system_health_info(hass: HomeAssistant) -> dict[str, Any]: ...
