from .const import DOMAIN as DOMAIN, VOLUME_BECQUEREL as VOLUME_BECQUEREL, VOLUME_PICOCURIE as VOLUME_PICOCURIE
from _typeshed import Incomplete
from airthings_ble import AirthingsDevice
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, Platform as Platform, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_entries_for_device as async_entries_for_device
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM

_LOGGER: Incomplete
SENSORS_MAPPING_TEMPLATE: dict[str, SensorEntityDescription]

def async_migrate(hass: HomeAssistant, address: str, sensor_name: str) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirthingsSensor(CoordinatorEntity[DataUpdateCoordinator[AirthingsDevice]], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[AirthingsDevice], airthings_device: AirthingsDevice, entity_description: SensorEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
