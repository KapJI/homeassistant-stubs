from .coordinator import PTDevicesConfigEntry as PTDevicesConfigEntry, PTDevicesCoordinator as PTDevicesCoordinator
from .entity import PTDevicesEntity as PTDevicesEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

class PTDevicesSensors(StrEnum):
    LEVEL_PERCENT = 'percent_level'
    LEVEL_VOLUME = 'volume_level'
    LEVEL_DEPTH = 'depth_level'
    PROBE_TEMPERATURE = 'probe_temperature'
    DEVICE_STATUS = 'status'
    DEVICE_WIFI_STRENGTH = 'wifi_signal'
    DEVICE_BATTERY_VOLTAGE = 'battery_voltage'
    TX_SIGNAL_STRENGTH = 'tx_signal'

@dataclass(kw_only=True, frozen=True)
class PTDevicesSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, str | int | float | None]], str | int | float | None]

SENSOR_DESCRIPTIONS: tuple[PTDevicesSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PTDevicesConfigEntry, async_add_entity: AddConfigEntryEntitiesCallback) -> None: ...

class PTDevicesSensorEntity(PTDevicesEntity, SensorEntity):
    entity_description: PTDevicesSensorEntityDescription
    def __init__(self, coordinator: PTDevicesCoordinator, description: PTDevicesSensorEntityDescription, device_id: str) -> None: ...
    @property
    @override
    def native_value(self) -> float | int | str | None: ...
