from .coordinator import OpenEVSEConfigEntry as OpenEVSEConfigEntry
from .entity import OpenEVSEEntity as OpenEVSEEntity
from .helpers import openevse_exception_handler as openevse_exception_handler
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricCurrent as UnitOfElectricCurrent
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from openevsehttp import OpenEVSE as OpenEVSE
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OpenEVSENumberDescription(NumberEntityDescription):
    value_fn: Callable[[OpenEVSE], float]
    min_value_fn: Callable[[OpenEVSE], float]
    max_value_fn: Callable[[OpenEVSE], float]
    set_value_fn: Callable[[OpenEVSE, float], Awaitable[Any]]

NUMBER_TYPES: tuple[OpenEVSENumberDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OpenEVSEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenEVSENumber(OpenEVSEEntity, NumberEntity):
    entity_description: OpenEVSENumberDescription
    @property
    @override
    def native_value(self) -> float: ...
    @property
    @override
    def native_min_value(self) -> float: ...
    @property
    @override
    def native_max_value(self) -> float: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
