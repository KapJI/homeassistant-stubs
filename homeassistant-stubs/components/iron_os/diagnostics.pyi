from . import IronOSConfigEntry as IronOSConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: IronOSConfigEntry) -> dict[str, Any]: ...
