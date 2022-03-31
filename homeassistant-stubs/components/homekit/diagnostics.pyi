from . import HomeKit as HomeKit
from .const import DOMAIN as DOMAIN, HOMEKIT as HOMEKIT
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from pyhap.accessory_driver import AccessoryDriver as AccessoryDriver
from pyhap.state import State as State
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, entry: ConfigEntry) -> dict[str, Any]: ...
