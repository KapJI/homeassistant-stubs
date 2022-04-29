from . import PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity
from .const import API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, CONF_UID as CONF_UID, DATA_COORDINATOR as DATA_COORDINATOR, DATA_COORDINATOR_PAIRED_SENSOR as DATA_COORDINATOR_PAIRED_SENSOR, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

ATTR_CONNECTED_CLIENTS: str
SENSOR_KIND_AP_INFO: str
SENSOR_KIND_LEAK_DETECTED: str
SENSOR_KIND_MOVED: str
SENSOR_DESCRIPTION_AP_ENABLED: Incomplete
SENSOR_DESCRIPTION_LEAK_DETECTED: Incomplete
SENSOR_DESCRIPTION_MOVED: Incomplete
PAIRED_SENSOR_DESCRIPTIONS: Incomplete
VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorBinarySensor(PairedSensorEntity, BinarySensorEntity):
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...

class ValveControllerBinarySensor(ValveControllerEntity, BinarySensorEntity):
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, DataUpdateCoordinator], description: BinarySensorEntityDescription) -> None: ...
    async def _async_continue_entity_setup(self) -> None: ...
    _attr_available: Incomplete
    def _async_update_from_latest_data(self) -> None: ...
