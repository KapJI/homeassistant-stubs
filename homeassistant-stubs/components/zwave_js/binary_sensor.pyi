from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_DOOR as DEVICE_CLASS_DOOR, DEVICE_CLASS_GAS as DEVICE_CLASS_GAS, DEVICE_CLASS_HEAT as DEVICE_CLASS_HEAT, DEVICE_CLASS_LOCK as DEVICE_CLASS_LOCK, DEVICE_CLASS_MOISTURE as DEVICE_CLASS_MOISTURE, DEVICE_CLASS_MOTION as DEVICE_CLASS_MOTION, DEVICE_CLASS_PLUG as DEVICE_CLASS_PLUG, DEVICE_CLASS_PROBLEM as DEVICE_CLASS_PROBLEM, DEVICE_CLASS_SAFETY as DEVICE_CLASS_SAFETY, DEVICE_CLASS_SMOKE as DEVICE_CLASS_SMOKE, DEVICE_CLASS_SOUND as DEVICE_CLASS_SOUND, DEVICE_CLASS_TAMPER as DEVICE_CLASS_TAMPER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from zwave_js_server.client import Client as ZwaveClient

LOGGER: Any
NOTIFICATION_SMOKE_ALARM: str
NOTIFICATION_CARBON_MONOOXIDE: str
NOTIFICATION_CARBON_DIOXIDE: str
NOTIFICATION_HEAT: str
NOTIFICATION_WATER: str
NOTIFICATION_ACCESS_CONTROL: str
NOTIFICATION_HOME_SECURITY: str
NOTIFICATION_POWER_MANAGEMENT: str
NOTIFICATION_SYSTEM: str
NOTIFICATION_EMERGENCY: str
NOTIFICATION_CLOCK: str
NOTIFICATION_APPLIANCE: str
NOTIFICATION_HOME_HEALTH: str
NOTIFICATION_SIREN: str
NOTIFICATION_WATER_VALVE: str
NOTIFICATION_WEATHER: str
NOTIFICATION_IRRIGATION: str
NOTIFICATION_GAS: str

class NotificationZWaveJSEntityDescription(BinarySensorEntityDescription):
    off_state: str
    states: Union[tuple[str, ...], None]

class PropertyZWaveJSMixin:
    on_states: tuple[str, ...]

class PropertyZWaveJSEntityDescription(BinarySensorEntityDescription, PropertyZWaveJSMixin): ...

NOTIFICATION_SENSOR_MAPPINGS: tuple[NotificationZWaveJSEntityDescription, ...]
PROPERTY_SENSOR_MAPPINGS: dict[str, PropertyZWaveJSEntityDescription]
BOOLEAN_SENSOR_MAPPINGS: dict[str, BinarySensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveBooleanBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    _attr_name: Any
    entity_description: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...

class ZWaveNotificationBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    state_key: Any
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo, state_key: str, description: Union[NotificationZWaveJSEntityDescription, None] = ...) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...

class ZWavePropertyBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    entity_description: PropertyZWaveJSEntityDescription
    _attr_name: Any
    def __init__(self, config_entry: ConfigEntry, client: ZwaveClient, info: ZwaveDiscoveryInfo, description: PropertyZWaveJSEntityDescription) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
