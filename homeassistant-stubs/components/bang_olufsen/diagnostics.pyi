from . import BangOlufsenConfigEntry as BangOlufsenConfigEntry
from .const import DOMAIN as DOMAIN
from .util import get_device_buttons as get_device_buttons
from homeassistant.const import CONF_MODEL as CONF_MODEL
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: BangOlufsenConfigEntry) -> dict[str, Any]: ...
