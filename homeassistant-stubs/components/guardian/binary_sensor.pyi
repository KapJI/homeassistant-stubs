from . import PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity
from .const import API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, CONF_UID as CONF_UID, DATA_COORDINATOR as DATA_COORDINATOR, DATA_COORDINATOR_PAIRED_SENSOR as DATA_COORDINATOR_PAIRED_SENSOR, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOVING as DEVICE_CLASS_MOVING
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_CONNECTED_CLIENTS: str
SENSOR_KIND_AP_INFO: str
SENSOR_KIND_LEAK_DETECTED: str
SENSOR_KIND_MOVED: str
SENSOR_DESCRIPTION_AP_ENABLED: Any
SENSOR_DESCRIPTION_LEAK_DETECTED: Any
SENSOR_DESCRIPTION_MOVED: Any
PAIRED_SENSOR_DESCRIPTIONS: Any
VALVE_CONTROLLER_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorBinarySensor(PairedSensorEntity, BinarySensorEntity):
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...

class ValveControllerBinarySensor(ValveControllerEntity, BinarySensorEntity):
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, DataUpdateCoordinator], description: BinarySensorEntityDescription) -> None: ...
    async def _async_continue_entity_setup(self) -> None: ...
    _attr_available: Any
    def _async_update_from_latest_data(self) -> None: ...
