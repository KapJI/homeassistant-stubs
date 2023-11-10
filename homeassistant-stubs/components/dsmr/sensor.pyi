from .const import CONF_DSMR_VERSION as CONF_DSMR_VERSION, CONF_PRECISION as CONF_PRECISION, CONF_PROTOCOL as CONF_PROTOCOL, CONF_RECONNECT_INTERVAL as CONF_RECONNECT_INTERVAL, CONF_SERIAL_ID as CONF_SERIAL_ID, CONF_SERIAL_ID_GAS as CONF_SERIAL_ID_GAS, CONF_TIME_BETWEEN_UPDATE as CONF_TIME_BETWEEN_UPDATE, DATA_TASK as DATA_TASK, DEFAULT_PRECISION as DEFAULT_PRECISION, DEFAULT_RECONNECT_INTERVAL as DEFAULT_RECONNECT_INTERVAL, DEFAULT_TIME_BETWEEN_UPDATE as DEFAULT_TIME_BETWEEN_UPDATE, DEVICE_NAME_ELECTRICITY as DEVICE_NAME_ELECTRICITY, DEVICE_NAME_GAS as DEVICE_NAME_GAS, DOMAIN as DOMAIN, DSMR_PROTOCOL as DSMR_PROTOCOL, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from dsmr_parser.objects import DSMRObject as DSMRObject
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, EntityCategory as EntityCategory, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import Throttle as Throttle

EVENT_FIRST_TELEGRAM: str
UNIT_CONVERSION: Incomplete

@dataclass
class DSMRSensorEntityDescriptionMixin:
    obis_reference: str
    def __init__(self, obis_reference) -> None: ...

@dataclass
class DSMRSensorEntityDescription(SensorEntityDescription, DSMRSensorEntityDescriptionMixin):
    dsmr_versions: set[str] | None = ...
    is_gas: bool = ...
    def __init__(self, obis_reference, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, dsmr_versions, is_gas) -> None: ...

SENSORS: tuple[DSMRSensorEntityDescription, ...]

def add_gas_sensor_5B(telegram: dict[str, DSMRObject]) -> DSMRSensorEntityDescription: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DSMREntity(SensorEntity):
    entity_description: DSMRSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _entry: Incomplete
    telegram: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entity_description: DSMRSensorEntityDescription, entry: ConfigEntry, telegram: dict[str, DSMRObject], device_class: SensorDeviceClass, native_unit_of_measurement: str | None) -> None: ...
    def update_data(self, telegram: dict[str, DSMRObject] | None) -> None: ...
    def get_dsmr_object_attr(self, attribute: str) -> str | None: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> StateType: ...
    @staticmethod
    def translate_tariff(value: str, dsmr_version: str) -> str | None: ...
