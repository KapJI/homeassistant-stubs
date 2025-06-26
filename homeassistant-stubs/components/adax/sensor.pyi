from . import AdaxConfigEntry as AdaxConfigEntry
from .const import CONNECTION_TYPE as CONNECTION_TYPE, DOMAIN as DOMAIN, LOCAL as LOCAL
from .coordinator import AdaxCloudCoordinator as AdaxCloudCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfEnergy as UnitOfEnergy
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, entry: AdaxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AdaxEnergySensor(CoordinatorEntity[AdaxCloudCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_suggested_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_suggested_display_precision: int
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AdaxCloudCoordinator, device_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> int: ...
