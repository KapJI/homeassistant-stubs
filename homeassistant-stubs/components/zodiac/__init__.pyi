from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
