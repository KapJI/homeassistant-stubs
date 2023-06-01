from .client import CloudClient as CloudClient
from .const import DOMAIN as DOMAIN
from hass_nabucasa import Cloud as Cloud
from homeassistant.components import system_health as system_health
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

def async_register(hass: HomeAssistant, register: system_health.SystemHealthRegistration) -> None: ...
async def system_health_info(hass: HomeAssistant) -> dict[str, Any]: ...
