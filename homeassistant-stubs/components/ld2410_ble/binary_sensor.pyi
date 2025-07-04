from . import LD2410BLE as LD2410BLE, LD2410BLECoordinator as LD2410BLECoordinator
from .models import LD2410BLEConfigEntry as LD2410BLEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

ENTITY_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LD2410BLEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LD2410BLEBinarySensor(CoordinatorEntity[LD2410BLECoordinator], BinarySensorEntity):
    _attr_has_entity_name: bool
    _coordinator: Incomplete
    _key: Incomplete
    _device: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_is_on: Incomplete
    def __init__(self, coordinator: LD2410BLECoordinator, device: LD2410BLE, name: str, description: BinarySensorEntityDescription) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    @property
    def available(self) -> bool: ...
