from .coordinator import LD2410BLECoordinator as LD2410BLECoordinator
from .models import LD2410BLEConfigEntry as LD2410BLEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from ld2410_ble import LD2410BLE as LD2410BLE

MOVING_TARGET_DISTANCE_DESCRIPTION: Incomplete
STATIC_TARGET_DISTANCE_DESCRIPTION: Incomplete
DETECTION_DISTANCE_DESCRIPTION: Incomplete
MOVING_TARGET_ENERGY_DESCRIPTION: Incomplete
STATIC_TARGET_ENERGY_DESCRIPTION: Incomplete
MAX_MOTION_GATES_DESCRIPTION: Incomplete
MAX_STATIC_GATES_DESCRIPTION: Incomplete
MOTION_ENERGY_GATES: Incomplete
STATIC_ENERGY_GATES: Incomplete
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LD2410BLEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LD2410BLESensor(CoordinatorEntity[LD2410BLECoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _coordinator: Incomplete
    _device: Incomplete
    _key: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, coordinator: LD2410BLECoordinator, device: LD2410BLE, name: str, description: SensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
