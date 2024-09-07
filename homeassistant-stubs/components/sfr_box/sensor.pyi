from .const import DOMAIN as DOMAIN
from .coordinator import SFRDataUpdateCoordinator as SFRDataUpdateCoordinator
from .models import DomainData as DomainData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfDataRate as UnitOfDataRate, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from sfrbox_api.models import DslInfo, SystemInfo, WanInfo

@dataclass(frozen=True, kw_only=True)
class SFRBoxSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[_T], StateType]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., value_fn) -> None: ...

DSL_SENSOR_TYPES: tuple[SFRBoxSensorEntityDescription[DslInfo], ...]
SYSTEM_SENSOR_TYPES: tuple[SFRBoxSensorEntityDescription[SystemInfo], ...]
WAN_SENSOR_TYPES: tuple[SFRBoxSensorEntityDescription[WanInfo], ...]

def _value_to_option(value: str | None) -> str | None: ...
def _get_temperature(value: float | None) -> float | None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SFRBoxSensor(CoordinatorEntity[SFRDataUpdateCoordinator[_T]], SensorEntity):
    entity_description: SFRBoxSensorEntityDescription[_T]
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SFRDataUpdateCoordinator[_T], description: SFRBoxSensorEntityDescription, system_info: SystemInfo) -> None: ...
    @property
    def native_value(self) -> StateType: ...
