from . import NoboHubConfigEntry as NoboHubConfigEntry
from .const import ATTR_SERIAL as ATTR_SERIAL, ATTR_ZONE_ID as ATTR_ZONE_ID, DOMAIN as DOMAIN, NOBO_MANUFACTURER as NOBO_MANUFACTURER
from .entity import NoboBaseEntity as NoboBaseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pynobo import nobo as nobo
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: NoboHubConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NoboTemperatureSensor(NoboBaseEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_suggested_display_precision: int
    _temperature: StateType
    _id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, hass: HomeAssistant, serial: str, hub: nobo, entry_id: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    @callback
    @override
    def _read_state(self) -> None: ...
