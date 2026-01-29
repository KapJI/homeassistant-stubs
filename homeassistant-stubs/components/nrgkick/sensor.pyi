from .const import CELLULAR_MODE_MAP as CELLULAR_MODE_MAP, CONNECTOR_TYPE_MAP as CONNECTOR_TYPE_MAP, ERROR_CODE_MAP as ERROR_CODE_MAP, RCD_TRIGGER_MAP as RCD_TRIGGER_MAP, STATUS_MAP as STATUS_MAP, WARNING_CODE_MAP as WARNING_CODE_MAP
from .coordinator import NRGkickConfigEntry as NRGkickConfigEntry, NRGkickData as NRGkickData, NRGkickDataUpdateCoordinator as NRGkickDataUpdateCoordinator
from .entity import NRGkickEntity as NRGkickEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfReactivePower as UnitOfReactivePower, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.variance import ignore_variance as ignore_variance
from typing import Any

PARALLEL_UPDATES: int

def _get_nested_dict_value(data: Any, *keys: str) -> Any: ...

@dataclass(frozen=True, kw_only=True)
class NRGkickSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[NRGkickData], StateType | datetime | None]
    requires_sim_module: bool = ...

def _seconds_to_datetime(value: int) -> datetime: ...

_seconds_to_stable_datetime: Incomplete

def _seconds_to_stable_timestamp(value: StateType) -> datetime | None: ...
def _map_code_to_translation_key(value: StateType, mapping: Mapping[int, str | None]) -> StateType: ...
def _enum_options_from_mapping(mapping: Mapping[int, str | None]) -> list[str]: ...
async def async_setup_entry(_hass: HomeAssistant, entry: NRGkickConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

SENSORS: tuple[NRGkickSensorEntityDescription, ...]

class NRGkickSensor(NRGkickEntity, SensorEntity):
    entity_description: NRGkickSensorEntityDescription
    def __init__(self, coordinator: NRGkickDataUpdateCoordinator, entity_description: NRGkickSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime: ...
