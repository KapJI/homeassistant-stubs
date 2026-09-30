from .const import BOX_NODE_ID as BOX_NODE_ID
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from .entity import DucoEntity as DucoEntity
from _typeshed import Incomplete
from duco_connectivity.models import Node as Node
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
DIAGNOSTIC_STATUS_TO_PROBLEM: Incomplete
DIAGNOSTIC_BINARY_SENSOR_DESCRIPTIONS: dict[str, BinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DucoDiagnosticBinarySensorEntity(DucoEntity, BinarySensorEntity):
    entity_description: Incomplete
    _component: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node, component: str, description: BinarySensorEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
