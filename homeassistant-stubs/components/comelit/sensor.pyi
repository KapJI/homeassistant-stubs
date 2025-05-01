from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge, ComelitVedoSystem as ComelitVedoSystem
from .entity import ComelitBridgeBaseEntity as ComelitBridgeBaseEntity
from _typeshed import Incomplete
from aiocomelit import ComelitSerialBridgeObject as ComelitSerialBridgeObject, ComelitVedoZoneObject as ComelitVedoZoneObject
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.const import CONF_TYPE as CONF_TYPE, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

PARALLEL_UPDATES: int
SENSOR_BRIDGE_TYPES: Final[Incomplete]
SENSOR_VEDO_TYPES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
async def async_setup_bridge_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
async def async_setup_vedo_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitBridgeSensorEntity(ComelitBridgeBaseEntity, SensorEntity):
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: ComelitSerialBridge, device: ComelitSerialBridgeObject, config_entry_entry_id: str, description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...

class ComelitVedoSensorEntity(CoordinatorEntity[ComelitVedoSystem], SensorEntity):
    _attr_has_entity_name: bool
    _zone_index: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: ComelitVedoSystem, zone: ComelitVedoZoneObject, config_entry_entry_id: str, description: SensorEntityDescription) -> None: ...
    @property
    def _zone_object(self) -> ComelitVedoZoneObject: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
