from .const import DOMAIN as DOMAIN, SIGNAL_EVENTS_CHANGED as SIGNAL_EVENTS_CHANGED
from .entity import Sun as Sun, SunConfigEntry as SunConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

ENTITY_ID_BINARY_SENSOR_FORMAT: Incomplete

@dataclass(kw_only=True, frozen=True)
class SunBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[Sun], bool | None]
    signal: str

BINARY_SENSOR_TYPES: tuple[SunBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SunConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SunBinarySensor(BinarySensorEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_entity_category: Incomplete
    entity_description: SunBinarySensorEntityDescription
    entity_id: Incomplete
    _attr_unique_id: Incomplete
    sun: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, sun: Sun, entity_description: SunBinarySensorEntityDescription, entry_id: str) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_added_to_hass(self) -> None: ...
