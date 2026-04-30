from .const import CONF_URL_SECURITY as CONF_URL_SECURITY, DOORTAG_CATEGORY_DOOR as DOORTAG_CATEGORY_DOOR, DOORTAG_CATEGORY_FURNITURE as DOORTAG_CATEGORY_FURNITURE, DOORTAG_CATEGORY_GARAGE as DOORTAG_CATEGORY_GARAGE, DOORTAG_CATEGORY_GATE as DOORTAG_CATEGORY_GATE, DOORTAG_CATEGORY_OTHER as DOORTAG_CATEGORY_OTHER, DOORTAG_CATEGORY_WINDOW as DOORTAG_CATEGORY_WINDOW, DOORTAG_STATUS_CALIBRATING as DOORTAG_STATUS_CALIBRATING, DOORTAG_STATUS_CALIBRATION_FAILED as DOORTAG_STATUS_CALIBRATION_FAILED, DOORTAG_STATUS_CLOSED as DOORTAG_STATUS_CLOSED, DOORTAG_STATUS_MAINTENANCE as DOORTAG_STATUS_MAINTENANCE, DOORTAG_STATUS_NO_NEWS as DOORTAG_STATUS_NO_NEWS, DOORTAG_STATUS_OPEN as DOORTAG_STATUS_OPEN, DOORTAG_STATUS_UNDEFINED as DOORTAG_STATUS_UNDEFINED, DOORTAG_STATUS_WEAK_SIGNAL as DOORTAG_STATUS_WEAK_SIGNAL, NETATMO_CREATE_CONNECTIVITY_BINARY_SENSOR as NETATMO_CREATE_CONNECTIVITY_BINARY_SENSOR, NETATMO_CREATE_OPENING_BINARY_SENSOR as NETATMO_CREATE_OPENING_BINARY_SENSOR, NETATMO_CREATE_WEATHER_BINARY_SENSOR as NETATMO_CREATE_WEATHER_BINARY_SENSOR
from .data_handler import NetatmoConfigEntry as NetatmoConfigEntry, NetatmoDevice as NetatmoDevice, SIGNAL_NAME as SIGNAL_NAME
from .entity import NetatmoModuleEntity as NetatmoModuleEntity, NetatmoWeatherModuleEntity as NetatmoWeatherModuleEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyatmo.modules.device_types import DeviceCategory as NetatmoDeviceCategory
from typing import Any, Final

_LOGGER: Incomplete
DEFAULT_OPENING_SENSOR_KEY: str
OPENING_STATUS_TO_BINARY_SENSOR_STATE: Final[dict[str, bool | None]]
OPENING_CATEGORY_TO_DEVICE_CLASS: Final[dict[str | None, BinarySensorDeviceClass]]

def get_opening_category(netatmo_device: NetatmoDevice) -> str: ...

OPENING_CATEGORY_TO_KEY: Final[dict[str, str | None]]

@dataclass(frozen=True, kw_only=True)
class NetatmoBinarySensorEntityDescription(BinarySensorEntityDescription):
    netatmo_name: str | None = ...
    value_fn: Callable[[str], str | bool | None] = ...

NETATMO_CONNECTIVITY_BINARY_SENSOR_DESCRIPTIONS: Final[list[NetatmoBinarySensorEntityDescription]]
NETATMO_OPENING_BINARY_SENSOR_DESCRIPTIONS: Final[list[NetatmoBinarySensorEntityDescription]]
DEVICE_CATEGORY_BINARY_URLS: Final[dict[NetatmoDeviceCategory, str]]
DEVICE_CATEGORY_WEATHER_BINARY_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoBinarySensorEntityDescription]]]
DEVICE_CATEGORY_CONNECTIVITY_BINARY_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoBinarySensorEntityDescription]]]
DEVICE_CATEGORY_OPENING_BINARY_SENSORS: Final[dict[NetatmoDeviceCategory, list[NetatmoBinarySensorEntityDescription]]]
DEVICE_CATEGORY_BINARY_PUBLISHERS: Final[list[NetatmoDeviceCategory]]

async def async_setup_entry(hass: HomeAssistant, entry: NetatmoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NetatmoBinarySensor(NetatmoModuleEntity, BinarySensorEntity):
    entity_description: NetatmoBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_configuration_url: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoBinarySensorEntityDescription, **kwargs: Any) -> None: ...
    _attr_available: bool
    _attr_is_on: bool
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoWeatherBinarySensor(NetatmoWeatherModuleEntity, NetatmoBinarySensor):
    entity_description: NetatmoBinarySensorEntityDescription
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoBinarySensorEntityDescription) -> None: ...

class NetatmoOpeningBinarySensor(NetatmoBinarySensor):
    entity_description: NetatmoBinarySensorEntityDescription
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, netatmo_device: NetatmoDevice, description: NetatmoBinarySensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    @callback
    def async_update_callback(self) -> None: ...

class NetatmoConnectivityBinarySensor(NetatmoBinarySensor):
    entity_description: NetatmoBinarySensorEntityDescription
    _attr_has_entity_name: bool
