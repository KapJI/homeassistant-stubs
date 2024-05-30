from .const import ARANET_MANUFACTURER_NAME as ARANET_MANUFACTURER_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aranet4.client import Aranet4Advertisement
from bleak.backends.device import BLEDevice as BLEDevice
from dataclasses import dataclass
from homeassistant import config_entries as config_entries
from homeassistant.components.bluetooth.passive_update_processor import PassiveBluetoothDataProcessor as PassiveBluetoothDataProcessor, PassiveBluetoothDataUpdate as PassiveBluetoothDataUpdate, PassiveBluetoothEntityKey as PassiveBluetoothEntityKey, PassiveBluetoothProcessorCoordinator as PassiveBluetoothProcessorCoordinator, PassiveBluetoothProcessorEntity as PassiveBluetoothProcessorEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_NAME as ATTR_NAME, ATTR_SW_VERSION as ATTR_SW_VERSION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfPressure as UnitOfPressure, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True)
class AranetSensorEntityDescription(SensorEntityDescription):
    name: str | None = ...
    scale: float | int = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, scale) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

def _device_key_to_bluetooth_entity_key(device: BLEDevice, key: str) -> PassiveBluetoothEntityKey: ...
def _sensor_device_info_to_hass(adv: Aranet4Advertisement) -> DeviceInfo: ...
def sensor_update_to_bluetooth_data_update(adv: Aranet4Advertisement) -> PassiveBluetoothDataUpdate[Any]: ...
async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class Aranet4BluetoothSensorEntity(PassiveBluetoothProcessorEntity[PassiveBluetoothDataProcessor[float | int | None, Aranet4Advertisement]], SensorEntity):
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> int | float | None: ...
