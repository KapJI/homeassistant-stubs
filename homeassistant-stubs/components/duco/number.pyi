from .const import BOX_NODE_ID as BOX_NODE_ID, DOMAIN as DOMAIN
from .coordinator import DucoConfigEntry as DucoConfigEntry, DucoCoordinator as DucoCoordinator
from .entity import DucoEntity as DucoEntity
from _typeshed import Incomplete
from duco_connectivity.models import Node as Node
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
NUMBER_DESCRIPTIONS: tuple[NumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: DucoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DucoBypassSupplyTemperatureTargetNumber(DucoEntity, NumberEntity):
    entity_description: Incomplete
    _zone_id: Incomplete
    _attr_translation_placeholders: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    def __init__(self, coordinator: DucoCoordinator, node: Node, description: NumberEntityDescription, zone_id: int, minimum: float, maximum: float, increment: float) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
