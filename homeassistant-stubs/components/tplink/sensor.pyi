from . import legacy_device_id as legacy_device_id
from .const import ATTR_CURRENT_A as ATTR_CURRENT_A, ATTR_CURRENT_POWER_W as ATTR_CURRENT_POWER_W, ATTR_TODAY_ENERGY_KWH as ATTR_TODAY_ENERGY_KWH, ATTR_TOTAL_ENERGY_KWH as ATTR_TOTAL_ENERGY_KWH, DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkEntity as CoordinatedTPLinkEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_VOLTAGE as ATTR_VOLTAGE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from kasa import SmartDevice as SmartDevice
from typing import Any

class TPLinkSensorEntityDescription(SensorEntityDescription):
    emeter_attr: Union[str, None]
    precision: Union[int, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, emeter_attr, precision) -> None: ...

ENERGY_SENSORS: tuple[TPLinkSensorEntityDescription, ...]

def async_emeter_from_device(device: SmartDevice, description: TPLinkSensorEntityDescription) -> Union[float, None]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SmartPlugSensor(CoordinatedTPLinkEntity, SensorEntity):
    coordinator: TPLinkDataUpdateCoordinator
    entity_description: TPLinkSensorEntityDescription
    _attr_unique_id: Any
    def __init__(self, device: SmartDevice, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkSensorEntityDescription) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> Union[float, None]: ...
