from . import BesenConfigEntry as BesenConfigEntry
from .coordinator import BesenCoordinator as BesenCoordinator
from .entity import BesenEntity as BesenEntity
from _typeshed import Incomplete
from besen.const import MIN_CHARGE_AMPS
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: BesenConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BesenChargingCurrentNumber(BesenEntity, NumberEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_mode: Incomplete
    _attr_native_min_value = MIN_CHARGE_AMPS
    _attr_native_step: int
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: BesenCoordinator) -> None: ...
    @property
    @override
    def native_max_value(self) -> float: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
