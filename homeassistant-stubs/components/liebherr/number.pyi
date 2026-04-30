from .const import DOMAIN as DOMAIN
from .coordinator import LiebherrConfigEntry as LiebherrConfigEntry, LiebherrCoordinator as LiebherrCoordinator
from .entity import LiebherrZoneEntity as LiebherrZoneEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import DEFAULT_MAX_VALUE as DEFAULT_MAX_VALUE, DEFAULT_MIN_VALUE as DEFAULT_MIN_VALUE, NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyliebherrhomeapi import TemperatureControl as TemperatureControl

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class LiebherrNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[TemperatureControl], float | None]
    min_fn: Callable[[TemperatureControl], float | None]
    max_fn: Callable[[TemperatureControl], float | None]
    unit_fn: Callable[[TemperatureControl], str]

NUMBER_TYPES: tuple[LiebherrNumberEntityDescription, ...]

def _create_number_entities(coordinators: list[LiebherrCoordinator]) -> list[LiebherrNumber]: ...
async def async_setup_entry(hass: HomeAssistant, entry: LiebherrConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LiebherrNumber(LiebherrZoneEntity, NumberEntity):
    entity_description: LiebherrNumberEntityDescription
    _attr_unique_id: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: LiebherrCoordinator, zone_id: int, description: LiebherrNumberEntityDescription) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> float | None: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def available(self) -> bool: ...
    async def async_set_native_value(self, value: float) -> None: ...
