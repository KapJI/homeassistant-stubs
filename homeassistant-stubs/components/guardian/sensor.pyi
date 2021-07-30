from . import PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity
from .const import API_SYSTEM_DIAGNOSTICS as API_SYSTEM_DIAGNOSTICS, API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, CONF_UID as CONF_UID, DATA_COORDINATOR as DATA_COORDINATOR, DATA_COORDINATOR_PAIRED_SENSOR as DATA_COORDINATOR_PAIRED_SENSOR, DATA_UNSUB_DISPATCHER_CONNECT as DATA_UNSUB_DISPATCHER_CONNECT, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, PERCENTAGE as PERCENTAGE, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TIME_MINUTES as TIME_MINUTES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSOR_KIND_BATTERY: str
SENSOR_KIND_TEMPERATURE: str
SENSOR_KIND_UPTIME: str
SENSOR_ATTRS_MAP: Any
PAIRED_SENSOR_SENSORS: Any
VALVE_CONTROLLER_SENSORS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorSensor(PairedSensorEntity, SensorEntity):
    _attr_unit_of_measurement: Any
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, kind: str, name: str, device_class: Union[str, None], icon: Union[str, None], unit: Union[str, None]) -> None: ...
    _attr_state: Any
    def _async_update_from_latest_data(self) -> None: ...

class ValveControllerSensor(ValveControllerEntity, SensorEntity):
    _attr_unit_of_measurement: Any
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, DataUpdateCoordinator], kind: str, name: str, device_class: Union[str, None], icon: Union[str, None], unit: Union[str, None]) -> None: ...
    async def _async_continue_entity_setup(self) -> None: ...
    _attr_available: Any
    _attr_state: Any
    def _async_update_from_latest_data(self) -> None: ...
