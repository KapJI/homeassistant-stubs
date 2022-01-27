from . import PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity
from .const import API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, CONF_UID as CONF_UID, DATA_COORDINATOR as DATA_COORDINATOR, DATA_COORDINATOR_PAIRED_SENSOR as DATA_COORDINATOR_PAIRED_SENSOR, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TIME_MINUTES as TIME_MINUTES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SENSOR_KIND_BATTERY: str
SENSOR_KIND_TEMPERATURE: str
SENSOR_KIND_UPTIME: str
SENSOR_DESCRIPTION_BATTERY: Any
SENSOR_DESCRIPTION_TEMPERATURE: Any
SENSOR_DESCRIPTION_UPTIME: Any
PAIRED_SENSOR_DESCRIPTIONS: Any
VALVE_CONTROLLER_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorSensor(PairedSensorEntity, SensorEntity):
    _attr_native_value: Any
    def _async_update_from_latest_data(self) -> None: ...

class ValveControllerSensor(ValveControllerEntity, SensorEntity):
    async def _async_continue_entity_setup(self) -> None: ...
    _attr_available: Any
    _attr_native_value: Any
    def _async_update_from_latest_data(self) -> None: ...
