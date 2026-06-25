from .const import DOMAIN as DOMAIN
from .coordinator import GuntamaticConfigEntry as GuntamaticConfigEntry, GuntamaticCoordinator as GuntamaticCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

PARALLEL_UPDATES: int
GUNTAMATIC_SENSORS: list[SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: GuntamaticConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GuntamaticSensor(CoordinatorEntity[GuntamaticCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GuntamaticCoordinator, entity_description: SensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
