from . import AirthingsConfigEntry as AirthingsConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirthingsDataUpdateCoordinator as AirthingsDataUpdateCoordinator
from _typeshed import Incomplete
from airthings import AirthingsDevice as AirthingsDevice
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

SENSORS: dict[str, SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: AirthingsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirthingsDeviceSensor(CoordinatorEntity[AirthingsDataUpdateCoordinator], SensorEntity):
    _attr_state_class: Incomplete
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AirthingsDataUpdateCoordinator, airthings_device: AirthingsDevice, entity_description: SensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def available(self) -> bool: ...
