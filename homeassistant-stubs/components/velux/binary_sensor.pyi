from . import VeluxConfigEntry as VeluxConfigEntry
from .const import LOGGER as LOGGER
from .entity import VeluxEntity as VeluxEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyvlx import OpeningDevice as OpeningDevice, Position as Position, Window

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxRainSensor(VeluxEntity, BinarySensorEntity):
    node: Window
    _attr_should_poll: bool
    _attr_entity_registry_enabled_default: bool
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _unavailable_logged: bool
    _attr_unique_id: Incomplete
    def __init__(self, node: OpeningDevice, config_entry_id: str) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    async def async_update(self) -> None: ...
