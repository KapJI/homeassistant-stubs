from . import NeoPoolConfigEntry as NeoPoolConfigEntry
from .coordinator import NeoPoolCoordinator as NeoPoolCoordinator
from .entity import NeoPoolEntity as NeoPoolEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfRatio as UnitOfRatio, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NeoPoolSensorEntityDescription(SensorEntityDescription):
    supported_fn: Callable[[dict[str, Any]], bool] | None = ...
    value_fn: Callable[[dict[str, Any]], Any] | None = ...
    options_fn: Callable[[dict[str, Any]], list[str]] | None = ...
    unit_fn: Callable[[dict[str, Any]], str | None] | None = ...
    precision_fn: Callable[[dict[str, Any]], int | None] | None = ...

SENSOR_DESCRIPTIONS: dict[str, NeoPoolSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: NeoPoolConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

_PRODUCTION_KEYS_REQUIRING_FILTRATION: Incomplete
_MEASURE_KEYS_REQUIRING_FILTRATION: Incomplete

class NeoPoolSensor(NeoPoolEntity, SensorEntity):
    entity_description: NeoPoolSensorEntityDescription
    _key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: NeoPoolCoordinator, key: str, description: NeoPoolSensorEntityDescription) -> None: ...
    @property
    @override
    def suggested_display_precision(self) -> int | None: ...
    @property
    @override
    def native_unit_of_measurement(self) -> str | None: ...
    def _filtration_off(self) -> bool: ...
    def _is_measurement_suppressed(self) -> bool: ...
    def _is_production_suppressed(self) -> bool: ...
    @property
    @override
    def native_value(self) -> float | int | str | datetime | None: ...
    @property
    @override
    def options(self) -> list[str] | None: ...
