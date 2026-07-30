from . import VeluxConfigEntry as VeluxConfigEntry
from .coordinator import VeluxLimitationCoordinator as VeluxLimitationCoordinator
from .entity import VeluxEntity as VeluxEntity, velux_device_info as velux_device_info, velux_unique_id as velux_unique_id, wrap_pyvlx_call_exceptions as wrap_pyvlx_call_exceptions
from _typeshed import Incomplete
from homeassistant.components.number import NumberEntity as NumberEntity, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfRatio as UnitOfRatio
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pyvlx import ExteriorHeating, Position
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: VeluxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VeluxExteriorHeatingNumber(VeluxEntity, NumberEntity):
    _attr_native_min_value: int
    _attr_native_max_value: int
    _attr_native_step: int
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_name: Incomplete
    node: ExteriorHeating
    @property
    @override
    def native_value(self) -> float | None: ...
    @wrap_pyvlx_call_exceptions
    @override
    async def async_set_native_value(self, value: float) -> None: ...

class VeluxPositionLimitNumber(CoordinatorEntity[VeluxLimitationCoordinator], NumberEntity):
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: bool
    _attr_mode: Incomplete
    _attr_native_step: int
    _attr_native_unit_of_measurement: Incomplete
    _attr_has_entity_name: bool
    _limitation_kind: str
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: VeluxLimitationCoordinator, config_entry_id: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @wrap_pyvlx_call_exceptions
    @override
    async def async_set_native_value(self, value: float) -> None: ...
    def _get_pyvlx_limit(self) -> Position | None: ...
    def _updated_pyvlx_limits(self, updated_position: Position, current_min: Position, current_max: Position) -> tuple[Position, Position]: ...
    async def _async_set_pyvlx_limitation(self, position: Position) -> None: ...

class VeluxClosedPositionLimitNumber(VeluxPositionLimitNumber):
    _attr_native_min_value: int
    _limitation_kind: str
    def _sibling_value(self) -> float | None: ...
    @property
    @override
    def native_max_value(self) -> float: ...
    @override
    def _get_pyvlx_limit(self) -> Position | None: ...
    @override
    def _updated_pyvlx_limits(self, updated_position: Position, current_min: Position, current_max: Position) -> tuple[Position, Position]: ...

class VeluxOpenPositionLimitNumber(VeluxPositionLimitNumber):
    _attr_native_max_value: int
    _limitation_kind: str
    def _sibling_value(self) -> float | None: ...
    @property
    @override
    def native_min_value(self) -> float: ...
    @override
    def _get_pyvlx_limit(self) -> Position | None: ...
    @override
    def _updated_pyvlx_limits(self, updated_position: Position, current_min: Position, current_max: Position) -> tuple[Position, Position]: ...
