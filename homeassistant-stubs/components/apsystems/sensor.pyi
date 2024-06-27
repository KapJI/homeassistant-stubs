from . import ApSystemsConfigEntry as ApSystemsConfigEntry, ApSystemsData as ApSystemsData
from .coordinator import ApSystemsDataCoordinator as ApSystemsDataCoordinator
from .entity import ApSystemsEntity as ApSystemsEntity
from APsystemsEZ1 import ReturnOutputData as ReturnOutputData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class ApsystemsLocalApiSensorDescription(SensorEntityDescription):
    value_fn: Callable[[ReturnOutputData], float | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSORS: tuple[ApsystemsLocalApiSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ApSystemsConfigEntry, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ApSystemsSensorWithDescription(CoordinatorEntity[ApSystemsDataCoordinator], ApSystemsEntity, SensorEntity):
    entity_description: ApsystemsLocalApiSensorDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, data: ApSystemsData, entity_description: ApsystemsLocalApiSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
