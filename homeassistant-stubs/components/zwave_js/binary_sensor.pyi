from .const import DOMAIN as DOMAIN
from .entity import NewZwaveDiscoveryInfo as NewZwaveDiscoveryInfo, ZWaveBaseEntity as ZWaveBaseEntity
from .models import NewZWaveDiscoverySchema as NewZWaveDiscoverySchema, ValueType as ValueType, ZWaveValueDiscoverySchema as ZWaveValueDiscoverySchema, ZwaveDiscoveryInfo as ZwaveDiscoveryInfo, ZwaveJSConfigEntry as ZwaveJSConfigEntry
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from zwave_js_server.const.command_class.notification import NotificationEvent as NotificationEvent
from zwave_js_server.model.driver import Driver as Driver

PARALLEL_UPDATES: int
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

@dataclass(frozen=True, kw_only=True)
class NotificationZWaveJSEntityDescription(BinarySensorEntityDescription):
    not_states: set[NotificationEvent | int] = field(default_factory=Incomplete)
    states: set[NotificationEvent | int] | None = ...

@dataclass(frozen=True, kw_only=True)
class PropertyZWaveJSEntityDescription(BinarySensorEntityDescription):
    on_states: tuple[str, ...]

@dataclass(frozen=True, kw_only=True)
class NewNotificationZWaveJSEntityDescription(BinarySensorEntityDescription):
    state_key: str

MIGRATED_NOTIFICATION_TYPES: Incomplete
NOTIFICATION_SENSOR_MAPPINGS: tuple[NotificationZWaveJSEntityDescription, ...]
PROPERTY_SENSOR_MAPPINGS: dict[str, PropertyZWaveJSEntityDescription]
BOOLEAN_SENSOR_MAPPINGS: dict[tuple[int, int | str], BinarySensorEntityDescription]

@callback
def is_valid_notification_binary_sensor(info: ZwaveDiscoveryInfo | NewZwaveDiscoveryInfo) -> bool | NotificationZWaveJSEntityDescription: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ZwaveJSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZWaveBooleanBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWaveNotificationBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    state_key: Incomplete
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo | NewZwaveDiscoveryInfo, state_key: str, description: NotificationZWaveJSEntityDescription | None = None) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWavePropertyBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    entity_description: PropertyZWaveJSEntityDescription
    _attr_name: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo, description: PropertyZWaveJSEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWaveConfigParameterBinarySensor(ZWaveBooleanBinarySensor):
    _attr_entity_category: Incomplete
    _attr_name: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo) -> None: ...

DISCOVERY_SCHEMAS: list[NewZWaveDiscoverySchema]
