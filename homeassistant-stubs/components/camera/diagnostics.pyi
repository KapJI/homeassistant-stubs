from . import _get_camera_from_entity_id as _get_camera_from_entity_id
from .const import DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> dict[str, Any]: ...
