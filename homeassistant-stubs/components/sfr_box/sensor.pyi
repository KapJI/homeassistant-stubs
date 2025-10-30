from .coordinator import SFRConfigEntry as SFRConfigEntry
from .entity import SFRCoordinatorEntity as SFRCoordinatorEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfDataRate as UnitOfDataRate, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from sfrbox_api.models import DslInfo, SystemInfo, WanInfo

@dataclass(frozen=True, kw_only=True)
class SFRBoxSensorEntityDescription[_T](SensorEntityDescription):
    value_fn: Callable[[_T], StateType]

DSL_SENSOR_TYPES: tuple[SFRBoxSensorEntityDescription[DslInfo], ...]
SYSTEM_SENSOR_TYPES: tuple[SFRBoxSensorEntityDescription[SystemInfo], ...]
WAN_SENSOR_TYPES: tuple[SFRBoxSensorEntityDescription[WanInfo], ...]

def _value_to_option(value: str | None) -> str | None: ...
def _get_temperature(value: float | None) -> float | None: ...
async def async_setup_entry(hass: HomeAssistant, entry: SFRConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SFRBoxSensor[_T](SFRCoordinatorEntity[_T], SensorEntity):
    entity_description: SFRBoxSensorEntityDescription[_T]
    @property
    def native_value(self) -> StateType: ...
