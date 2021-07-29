from . import OpenUV as OpenUV, OpenUvEntity as OpenUvEntity
from .const import DATA_CLIENT as DATA_CLIENT, DATA_PROTECTION_WINDOW as DATA_PROTECTION_WINDOW, DOMAIN as DOMAIN, LOGGER as LOGGER, TYPE_PROTECTION_WINDOW as TYPE_PROTECTION_WINDOW
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.dt import as_local as as_local, parse_datetime as parse_datetime, utcnow as utcnow
from typing import Any

ATTR_PROTECTION_WINDOW_ENDING_TIME: str
ATTR_PROTECTION_WINDOW_ENDING_UV: str
ATTR_PROTECTION_WINDOW_STARTING_TIME: str
ATTR_PROTECTION_WINDOW_STARTING_UV: str
BINARY_SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenUvBinarySensor(OpenUvEntity, BinarySensorEntity):
    _attr_icon: Any
    _attr_name: Any
    def __init__(self, openuv: OpenUV, sensor_type: str, name: str, icon: str) -> None: ...
    _attr_available: bool
    _attr_is_on: bool
    def update_from_latest_data(self) -> None: ...
