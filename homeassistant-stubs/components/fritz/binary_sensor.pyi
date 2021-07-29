from .common import FritzBoxBaseEntity as FritzBoxBaseEntity, FritzBoxTools as FritzBoxTools
from .const import DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxConnectivitySensor(FritzBoxBaseEntity, BinarySensorEntity):
    _unique_id: Any
    _name: Any
    _is_on: bool
    _is_available: bool
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def device_class(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    def update(self) -> None: ...
