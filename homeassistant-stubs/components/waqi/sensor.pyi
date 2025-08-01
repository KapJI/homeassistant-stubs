from .const import DOMAIN as DOMAIN
from .coordinator import WAQIConfigEntry as WAQIConfigEntry, WAQIDataUpdateCoordinator as WAQIDataUpdateCoordinator
from _typeshed import Incomplete
from aiowaqi import WAQIAirQuality as WAQIAirQuality
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

@dataclass(frozen=True, kw_only=True)
class WAQISensorEntityDescription(SensorEntityDescription):
    available_fn: Callable[[WAQIAirQuality], bool] = ...
    value_fn: Callable[[WAQIAirQuality], StateType]

SENSORS: list[WAQISensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: WAQIConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WaqiSensor(CoordinatorEntity[WAQIDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: WAQISensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_attribution: Incomplete
    def __init__(self, coordinator: WAQIDataUpdateCoordinator, entity_description: WAQISensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
