from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_DOOR as DEVICE_CLASS_DOOR, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_HEAT as DEVICE_CLASS_HEAT, DEVICE_CLASS_LOCK as DEVICE_CLASS_LOCK, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE, DEVICE_CLASS_SOUND as DEVICE_CLASS_SOUND
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, TypedDict
from zwave_js_server.client import Client as ZwaveClient

LOGGER: Any
NOTIFICATION_SMOKE_ALARM: int
NOTIFICATION_CARBON_MONOOXIDE: int
NOTIFICATION_CARBON_DIOXIDE: int
NOTIFICATION_HEAT: int
NOTIFICATION_WATER: int
NOTIFICATION_ACCESS_CONTROL: int
NOTIFICATION_HOME_SECURITY: int
NOTIFICATION_POWER_MANAGEMENT: int
NOTIFICATION_SYSTEM: int
NOTIFICATION_EMERGENCY: int
NOTIFICATION_CLOCK: int
NOTIFICATION_APPLIANCE: int
NOTIFICATION_HOME_HEALTH: int
NOTIFICATION_SIREN: int
NOTIFICATION_WATER_VALVE: int
NOTIFICATION_WEATHER: int
NOTIFICATION_IRRIGATION: int
NOTIFICATION_GAS: int

class NotificationSensorMapping(TypedDict):
    type: int
    states: list[str]
    device_class: str
    enabled: bool

NOTIFICATION_SENSOR_MAPPINGS: list[NotificationSensorMapping]
PROPERTY_DOOR_STATUS: str

class PropertySensorMapping(TypedDict):
    property_name: str
    on_states: list[str]
    device_class: str
    enabled: bool

PROPERTY_SENSOR_MAPPINGS: list[PropertySensorMapping]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveBooleanBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    _attr_name: Any
    _attr_device_class: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...

class ZWaveNotificationBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    state_key: Any
    _mapping_info: Any
    _attr_name: Any
    _attr_device_class: Any
    _attr_unique_id: Any
    _attr_entity_registry_enabled_default: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo, state_key: str) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    def _get_sensor_mapping(self) -> NotificationSensorMapping: ...

class ZWavePropertyBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    _mapping_info: Any
    _attr_name: Any
    _attr_device_class: Any
    _attr_entity_registry_enabled_default: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    def _get_sensor_mapping(self) -> PropertySensorMapping: ...
