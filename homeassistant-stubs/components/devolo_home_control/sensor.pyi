from .const import DOMAIN as DOMAIN
from .devolo_device import DevoloDeviceEntity as DevoloDeviceEntity
from devolo_home_control_api.devices.zwave import Zwave as Zwave
from devolo_home_control_api.homecontrol import HomeControl as HomeControl
from homeassistant.components.sensor import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_ILLUMINANCE as DEVICE_CLASS_ILLUMINANCE, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLTAGE as DEVICE_CLASS_VOLTAGE, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DEVICE_CLASS_MAPPING: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloMultiLevelDeviceEntity(DevoloDeviceEntity, SensorEntity):
    @property
    def state(self) -> int: ...

class DevoloGenericMultiLevelDeviceEntity(DevoloMultiLevelDeviceEntity):
    _multi_level_sensor_property: Any
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    _value: Any
    _attr_entity_registry_enabled_default: bool
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...

class DevoloBatteryEntity(DevoloMultiLevelDeviceEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    _value: Any
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str) -> None: ...

class DevoloConsumptionEntity(DevoloMultiLevelDeviceEntity):
    _sensor_type: Any
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    _attr_state_class: Any
    _attr_last_reset: Any
    _value: Any
    def __init__(self, homecontrol: HomeControl, device_instance: Zwave, element_uid: str, consumption: str) -> None: ...
    @property
    def unique_id(self) -> str: ...
    def _sync(self, message: tuple) -> None: ...
