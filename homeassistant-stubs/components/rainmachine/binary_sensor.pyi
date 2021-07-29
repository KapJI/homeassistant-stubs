from . import RainMachineEntity as RainMachineEntity
from .const import DATA_CONTROLLER as DATA_CONTROLLER, DATA_COORDINATOR as DATA_COORDINATOR, DATA_PROVISION_SETTINGS as DATA_PROVISION_SETTINGS, DATA_RESTRICTIONS_CURRENT as DATA_RESTRICTIONS_CURRENT, DATA_RESTRICTIONS_UNIVERSAL as DATA_RESTRICTIONS_UNIVERSAL, DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from regenmaschine.controller import Controller as Controller
from typing import Any

TYPE_FLOW_SENSOR: str
TYPE_FREEZE: str
TYPE_FREEZE_PROTECTION: str
TYPE_HOT_DAYS: str
TYPE_HOURLY: str
TYPE_MONTH: str
TYPE_RAINDELAY: str
TYPE_RAINSENSOR: str
TYPE_WEEKDAY: str
BINARY_SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RainMachineBinarySensor(RainMachineEntity, BinarySensorEntity):
    _attr_entity_registry_enabled_default: Any
    _attr_icon: Any
    _attr_name: Any
    def __init__(self, coordinator: DataUpdateCoordinator, controller: Controller, sensor_type: str, name: str, icon: str, enabled_by_default: bool) -> None: ...

class CurrentRestrictionsBinarySensor(RainMachineBinarySensor):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...

class ProvisionSettingsBinarySensor(RainMachineBinarySensor):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...

class UniversalRestrictionsBinarySensor(RainMachineBinarySensor):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...
