from .const import LOVELACE_DATA as LOVELACE_DATA, MODE_AUTO as MODE_AUTO, MODE_STORAGE as MODE_STORAGE, MODE_YAML as MODE_YAML
from homeassistant.components import system_health as system_health
from homeassistant.const import CONF_MODE as CONF_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

@callback
def async_register(hass: HomeAssistant, register: system_health.SystemHealthRegistration) -> None: ...
async def system_health_info(hass: HomeAssistant) -> dict[str, Any]: ...
