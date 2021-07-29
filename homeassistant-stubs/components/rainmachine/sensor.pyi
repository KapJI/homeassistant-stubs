from . import RainMachineEntity as RainMachineEntity
from .const import DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from regenmaschine.controller import Controller as Controller
from typing import Any

TYPE_FLOW_SENSOR_CLICK_M3: str
TYPE_FLOW_SENSOR_CONSUMED_LITERS: str
TYPE_FLOW_SENSOR_START_INDEX: str
TYPE_FLOW_SENSOR_WATERING_CLICKS: str
TYPE_FREEZE_TEMP: str
SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineSensor(RainMachineEntity, SensorEntity):
    _attr_device_class: Any
    _attr_entity_registry_enabled_default: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_unit_of_measurement: Any
    def __init__(self, coordinator: DataUpdateCoordinator, controller: Controller, sensor_type: str, name: str, icon: str, unit: str, device_class: str, enabled_by_default: bool) -> None: ...

class ProvisionSettingsSensor(RainMachineSensor):
    _attr_state: Any
    def update_from_latest_data(self) -> None: ...

class UniversalRestrictionsSensor(RainMachineSensor):
    _attr_state: Any
    def update_from_latest_data(self) -> None: ...
