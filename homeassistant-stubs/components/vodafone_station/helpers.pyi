from .const import _LOGGER as _LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_registry as er
from typing import Any

async def cleanup_device_tracker(hass: HomeAssistant, config_entry: ConfigEntry, devices: dict[str, Any]) -> None: ...
def _async_remove_empty_devices(hass: HomeAssistant, entity_reg: er.EntityRegistry, config_entry: ConfigEntry) -> None: ...
