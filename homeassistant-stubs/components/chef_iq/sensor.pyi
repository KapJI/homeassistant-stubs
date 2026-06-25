from . import ChefIqConfigEntry as ChefIqConfigEntry
from .device import device_key_to_bluetooth_entity_key as device_key_to_bluetooth_entity_key
from chefiq_ble import ChefIqSensor, SensorUpdate
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.sensor import sensor_device_info_to_hass_device_info as sensor_device_info_to_hass_device_info
from typing import override

PARALLEL_UPDATES: int

def _temperature_description(sensor: ChefIqSensor, *, enabled_default: bool = True) -> SensorEntityDescription: ...

SENSOR_DESCRIPTIONS: dict[str, SensorEntityDescription]

def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate: ...
async def async_setup_entry(hass: HomeAssistant, entry: ChefIqConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ChefIqBluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[float | int | None, SensorUpdate]], SensorEntity):
    @property
    @override
    def native_value(self) -> float | int | None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def assumed_state(self) -> bool: ...
