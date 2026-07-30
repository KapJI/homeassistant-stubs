from .const import DOMAIN as DOMAIN
from .coordinator import AirthingsBLEConfigEntry as AirthingsBLEConfigEntry, AirthingsBLEDataUpdateCoordinator as AirthingsBLEDataUpdateCoordinator
from _typeshed import Incomplete
from airthings_ble import AirthingsDevice as AirthingsDevice
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, Platform as Platform, UnitOfPressure as UnitOfPressure, UnitOfRadiationConcentration as UnitOfRadiationConcentration, UnitOfRatio as UnitOfRatio, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_entries_for_device as async_entries_for_device
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import override

_LOGGER: Incomplete
CONNECTIVITY_MODE_MAP: Incomplete

def get_connectivity_mode(value: str | float | None) -> str | None: ...

@dataclass(frozen=True, kw_only=True)
class AirthingsBLESensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[str | float | None], str | float | None] = ...

SENSORS_MAPPING_TEMPLATE: dict[str, AirthingsBLESensorEntityDescription]
PARALLEL_UPDATES: int

@callback
def async_migrate(hass: HomeAssistant, entry_id: str, address: str, sensor_name: str) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: AirthingsBLEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirthingsSensor(CoordinatorEntity[AirthingsBLEDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: AirthingsBLESensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirthingsBLEDataUpdateCoordinator, airthings_device: AirthingsDevice, entity_description: AirthingsBLESensorEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> StateType: ...
