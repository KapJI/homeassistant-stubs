from .const import DOMAIN as DOMAIN, ISY_URL_POSTFIX as ISY_URL_POSTFIX
from .models import IsyConfigEntry as IsyConfigEntry
from homeassistant.components import system_health as system_health
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_register(hass: HomeAssistant, register: system_health.SystemHealthRegistration) -> None: ...
async def system_health_info(hass: HomeAssistant) -> dict[str, Any]: ...
