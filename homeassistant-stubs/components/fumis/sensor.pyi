from .coordinator import FumisConfigEntry as FumisConfigEntry, FumisDataUpdateCoordinator as FumisDataUpdateCoordinator
from .entity import FumisEntity as FumisEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from fumis import FumisInfo as FumisInfo, StoveAlert, StoveError
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, REVOLUTIONS_PER_MINUTE as REVOLUTIONS_PER_MINUTE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.variance import ignore_variance as ignore_variance
from typing import Any

PARALLEL_UPDATES: int

def _code_to_state(code: StoveAlert | StoveError | None) -> str | None: ...
def _code_to_attr(code: StoveAlert | StoveError | None) -> dict[str, str | None]: ...

@dataclass(frozen=True, kw_only=True)
class FumisSensorEntityDescription(SensorEntityDescription):
    attr_fn: Callable[[FumisInfo], dict[str, Any]] | None = ...
    has_fn: Callable[[FumisInfo], bool] = ...
    value_fn: Callable[[FumisInfo], datetime | float | int | str | None]

SENSORS: tuple[FumisSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: FumisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FumisSensorEntity(FumisEntity, SensorEntity):
    entity_description: FumisSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FumisDataUpdateCoordinator, description: FumisSensorEntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def native_value(self) -> datetime | float | int | str | None: ...
