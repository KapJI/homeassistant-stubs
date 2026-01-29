from . import PooldoseConfigEntry as PooldoseConfigEntry
from .coordinator import PooldoseCoordinator as PooldoseCoordinator
from .entity import PooldoseEntity as PooldoseEntity
from _typeshed import Incomplete
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
NUMBER_DESCRIPTIONS: tuple[NumberEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PooldoseConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PooldoseNumber(PooldoseEntity, NumberEntity):
    def __init__(self, coordinator: PooldoseCoordinator, serial_number: str, device_info: Any, description: NumberEntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
