from .const import DOMAIN as DOMAIN
from .entity import NewZwaveDiscoveryInfo as NewZwaveDiscoveryInfo, ZWaveBaseEntity as ZWaveBaseEntity
from .helpers import get_opening_state_notification_value as get_opening_state_notification_value, is_opening_state_notification_value as is_opening_state_notification_value
from .models import NewZWaveDiscoverySchema as NewZWaveDiscoverySchema, ValueType as ValueType, ZWaveValueDiscoverySchema as ZWaveValueDiscoverySchema, ZwaveDiscoveryInfo as ZwaveDiscoveryInfo, ZwaveJSConfigEntry as ZwaveJSConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass, field
from enum import IntEnum
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.start import async_at_started as async_at_started
from zwave_js_server.const.command_class.notification import NotificationEvent as NotificationEvent
from zwave_js_server.model.driver import Driver as Driver
from zwave_js_server.model.value import Value as ZwaveValue

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
ACCESS_CONTROL_DOOR_STATE_OPEN_REGULAR: int
ACCESS_CONTROL_DOOR_STATE_OPEN_TILT: int

class OpeningState(IntEnum):
    CLOSED = 0
    OPEN = 1
    TILTED = 2

def _opening_state_is_closed(opening_state: OpeningState) -> bool: ...
def _opening_state_is_open(opening_state: OpeningState) -> bool: ...
def _opening_state_is_open_or_tilted(opening_state: OpeningState) -> bool: ...
def _opening_state_is_tilted(opening_state: OpeningState) -> bool: ...

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

@dataclass(frozen=True, kw_only=True)
class OpeningStateZWaveJSEntityDescription(BinarySensorEntityDescription):
    state_key: int
    parse_opening_state: Callable[[OpeningState], bool]

@dataclass(frozen=True, kw_only=True)
class LegacyDoorStateRepairDescription:
    issue_translation_key: str
    replacement_state_key: OpeningState

LEGACY_DOOR_STATE_REPAIR_DESCRIPTIONS: dict[str, LegacyDoorStateRepairDescription]
LEGACY_DOOR_STATE_REPAIR_ISSUE_KEYS: Incomplete
MIGRATED_NOTIFICATION_TYPES: Incomplete
NOTIFICATION_SENSOR_MAPPINGS: tuple[NotificationZWaveJSEntityDescription, ...]
PROPERTY_SENSOR_MAPPINGS: dict[str, PropertyZWaveJSEntityDescription]
BOOLEAN_SENSOR_MAPPINGS: dict[tuple[int, int | str], BinarySensorEntityDescription]

@callback
def is_valid_notification_binary_sensor(info: ZwaveDiscoveryInfo | NewZwaveDiscoveryInfo) -> bool | NotificationZWaveJSEntityDescription: ...
@callback
def _async_delete_legacy_entity_repairs(hass: HomeAssistant, entity_id: str) -> None: ...
@callback
def _async_check_legacy_entity_repair(hass: HomeAssistant, driver: Driver, entity: ZWaveLegacyDoorStateBinarySensor) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ZwaveJSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZWaveBooleanBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    _attr_name: Incomplete
    entity_description: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: ZwaveDiscoveryInfo | NewZwaveDiscoveryInfo) -> None: ...
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

class ZWaveLegacyDoorStateBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    entity_description: OpeningStateZWaveJSEntityDescription
    _opening_state_value_id: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: NewZwaveDiscoveryInfo) -> None: ...
    @property
    def is_on(self) -> bool | None: ...

class ZWaveOpeningStateBinarySensor(ZWaveBaseEntity, BinarySensorEntity):
    entity_description: OpeningStateZWaveJSEntityDescription
    _known_states: set[str]
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: ZwaveJSConfigEntry, driver: Driver, info: NewZwaveDiscoveryInfo) -> None: ...
    @callback
    def should_rediscover_on_metadata_update(self) -> bool: ...
    async def _async_remove_and_rediscover(self, value: ZwaveValue) -> None: ...
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

OPENING_STATE_NOTIFICATION_SCHEMA: Incomplete
DISCOVERY_SCHEMAS: list[NewZWaveDiscoverySchema]
