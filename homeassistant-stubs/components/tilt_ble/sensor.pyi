from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothEntityKey as PassiveBluetoothEntityKey, PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tilt_ble import DeviceKey as DeviceKey, SensorDeviceInfo as SensorDeviceInfo, SensorUpdate as SensorUpdate
from typing import Optional, Union

SENSOR_DESCRIPTIONS: Incomplete

def _device_key_to_bluetooth_entity_key(device_key: DeviceKey) -> PassiveBluetoothEntityKey: ...
def _sensor_device_info_to_hass(sensor_device_info: SensorDeviceInfo) -> DeviceInfo: ...
def sensor_update_to_bluetooth_data_update(sensor_update: SensorUpdate) -> PassiveBluetoothDataUpdate: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TiltBluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[Optional[Union[float, int]]]], SensorEntity):
    @property
    def native_value(self) -> Union[int, float, None]: ...
