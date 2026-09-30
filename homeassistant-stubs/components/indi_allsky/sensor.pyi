from .coordinator import IndiAllSkyConfigEntry as IndiAllSkyConfigEntry, IndiAllSkyData as IndiAllSkyData, IndiAllSkyDataUpdateCoordinator as IndiAllSkyDataUpdateCoordinator
from .entity import IndiAllSkyEntity as IndiAllSkyEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import DEVICE_CLASS_UNITS as DEVICE_CLASS_UNITS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, override

PARALLEL_UPDATES: int

def _parse_timestamp(data: IndiAllSkyData) -> datetime | None: ...

@dataclass(frozen=True, kw_only=True)
class IndiAllSkySensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[IndiAllSkyData], StateType | datetime]

PREDEFINED_SENSOR_DESCRIPTIONS: tuple[IndiAllSkySensorEntityDescription, ...]
IGNORED_DYNAMIC_KEYS: set[str]
DEVICE_CLASS_KEYWORDS: tuple[tuple[tuple[str, ...], SensorDeviceClass], ...]
KNOWN_TRANSLATION_KEYS: set[str]

def _infer_sensor_metadata(key: str, raw_name: str | None, raw_device_class: str | None, raw_unit: str | None) -> tuple[str, SensorDeviceClass | None, str | None, SensorStateClass | None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: IndiAllSkyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndiAllSkySensor(IndiAllSkyEntity, SensorEntity):
    entity_description: IndiAllSkySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndiAllSkyDataUpdateCoordinator, entry: IndiAllSkyConfigEntry, description: IndiAllSkySensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType | datetime: ...

class IndiAllSkyDynamicHardwareSensor(IndiAllSkyEntity, SensorEntity):
    _sensor_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndiAllSkyDataUpdateCoordinator, entry: IndiAllSkyConfigEntry, sensor_key: str) -> None: ...
    def _get_sensor_item(self) -> Any: ...
    _attr_translation_key: Incomplete
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    def _update_attributes(self) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
