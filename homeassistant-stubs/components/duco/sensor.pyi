from .const import BOX_NODE_ID as BOX_NODE_ID, DOMAIN as DOMAIN
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from .entity import DucoEntity as DucoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from duco_connectivity.models import Node as Node, NodeType
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class DucoSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Node], datetime | int | float | str | None]
    node_types: tuple[NodeType, ...]

@dataclass(frozen=True, kw_only=True)
class DucoBoxSensorEntityDescription(SensorEntityDescription):
    supported_fn: Callable[[DucoCoordinator], bool] = ...
    value_fn: Callable[[DucoCoordinator], int | float | None]

SENSOR_DESCRIPTIONS: tuple[DucoSensorEntityDescription, ...]
BOX_SENSOR_DESCRIPTIONS: tuple[DucoBoxSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DucoSensorEntity(DucoEntity, SensorEntity):
    entity_description: DucoSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node, description: DucoSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> datetime | int | float | str | None: ...

class DucoBoxSensorEntity(DucoEntity, SensorEntity):
    entity_description: DucoBoxSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node, description: DucoBoxSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> int | float | None: ...
