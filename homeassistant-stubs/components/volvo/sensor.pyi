from .const import API_NONE_VALUE as API_NONE_VALUE, DATA_BATTERY_CAPACITY as DATA_BATTERY_CAPACITY
from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from .entity import VolvoEntity as VolvoEntity, VolvoEntityDescription as VolvoEntityDescription, value_to_translation_key as value_to_translation_key
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfEnergy as UnitOfEnergy, UnitOfEnergyDistance as UnitOfEnergyDistance, UnitOfLength as UnitOfLength, UnitOfPower as UnitOfPower, UnitOfSpeed as UnitOfSpeed, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from volvocarsapi.models import VolvoCarsApiBaseModel as VolvoCarsApiBaseModel, VolvoCarsValue

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class VolvoSensorDescription(VolvoEntityDescription, SensorEntityDescription):
    value_fn: Callable[[VolvoCarsValue], Any] | None = ...

def _availability_status(field: VolvoCarsValue) -> str: ...
def _calculate_time_to_service(field: VolvoCarsValue) -> int: ...
def _charging_power_value(field: VolvoCarsValue) -> int: ...
def _charging_power_status_value(field: VolvoCarsValue) -> str | None: ...

_CHARGING_POWER_STATUS_OPTIONS: Incomplete
_DESCRIPTIONS: tuple[VolvoSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VolvoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VolvoSensor(VolvoEntity, SensorEntity):
    entity_description: VolvoSensorDescription
    _attr_native_value: Incomplete
    def _update_state(self, api_field: VolvoCarsApiBaseModel | None) -> None: ...
