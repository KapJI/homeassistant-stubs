from .common import FritzBoxBaseEntity as FritzBoxBaseEntity, FritzBoxTools as FritzBoxTools
from .const import DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_PLUG as DEVICE_CLASS_PLUG, DEVICE_CLASS_UPDATE as DEVICE_CLASS_UPDATE
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBinarySensor(FritzBoxBaseEntity, BinarySensorEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, description: BinarySensorEntityDescription) -> None: ...
    _attr_is_on: Any
    _attr_extra_state_attributes: Any
    def update(self) -> None: ...
