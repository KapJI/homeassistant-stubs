from .coordinator import SofarConfigEntry as SofarConfigEntry
from .entity import SofarEntity as SofarEntity, SofarEntityDescription as SofarEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import IntFlag
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from sofar_modbus.modern.device import SofarInverter as SofarInverter
from sofar_modbus.modern.faults import FaultCategory
from typing import override

PARALLEL_UPDATES: int
_DISABLED_BY_DEFAULT: Incomplete

@dataclass(frozen=True, kw_only=True)
class SofarFaultBinarySensorDescription(SofarEntityDescription, BinarySensorEntityDescription):
    category: FaultCategory

FAULT_SENSOR_DESCRIPTIONS: tuple[SofarFaultBinarySensorDescription, ...]

@dataclass(frozen=True, kw_only=True)
class SofarFlagBinarySensorDescription(SofarEntityDescription, BinarySensorEntityDescription):
    flags_fn: Callable[[SofarInverter], IntFlag | None]
    flag: IntFlag

FLAG_SENSOR_DESCRIPTIONS: tuple[SofarFlagBinarySensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: SofarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SofarFaultBinarySensor(SofarEntity, BinarySensorEntity):
    entity_description: SofarFaultBinarySensorDescription
    @property
    @override
    def is_on(self) -> bool: ...

class SofarFlagBinarySensor(SofarEntity, BinarySensorEntity):
    entity_description: SofarFlagBinarySensorDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
