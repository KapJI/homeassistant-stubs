from .const import DOMAIN as DOMAIN
from .coordinator import GuntamaticConfigEntry as GuntamaticConfigEntry, GuntamaticCoordinator as GuntamaticCoordinator
from _typeshed import Incomplete
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import ChildDeviceInfo as ChildDeviceInfo, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int
HEATING_CIRCUIT_REGEX: Incomplete
GUNTAMATIC_SENSORS: list[SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: GuntamaticConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GuntamaticSensor(CoordinatorEntity[GuntamaticCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GuntamaticCoordinator, entity_description: SensorEntityDescription, device_info: DeviceInfo | ChildDeviceInfo) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> StateType | date: ...
