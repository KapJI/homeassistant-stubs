from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_PRECISION as CONF_PRECISION, CONF_RECONNECT_INTERVAL as CONF_RECONNECT_INTERVAL, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DATA_TASK as DATA_TASK, DEFAULT_PRECISION as DEFAULT_PRECISION, DEFAULT_RECONNECT_INTERVAL as DEFAULT_RECONNECT_INTERVAL, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DEVICE_NAME_ENERGY as DEVICE_NAME_ENERGY, DEVICE_NAME_GAS as DEVICE_NAME_GAS, DOMAIN as DOMAIN, LOGGER as LOGGER, SENSORS as SENSORS
from .models import DSMRSensorEntityDescription as DSMRSensorEntityDescription
from dsmr_parser.objects import DSMRObject as DSMRObject
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import CoreState as CoreState, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import EventType as EventType, StateType as StateType
from homeassistant.util import Throttle as Throttle
from typing import Any

UNIT_CONVERSION: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DSMREntity(SensorEntity):
    entity_description: DSMRSensorEntityDescription
    _attr_should_poll: bool
    _entry: Any
    telegram: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, entity_description: DSMRSensorEntityDescription, entry: ConfigEntry) -> None: ...
    def update_data(self, telegram: dict[str, DSMRObject]) -> None: ...
    def get_dsmr_object_attr(self, attribute: str) -> Union[str, None]: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @staticmethod
    def translate_tariff(value: str, dsmr_version: str) -> Union[str, None]: ...
