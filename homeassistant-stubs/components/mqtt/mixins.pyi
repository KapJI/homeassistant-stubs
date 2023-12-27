import abc
import voluptuous as vol
from . import debug_info as debug_info, subscription as subscription
from .client import async_publish as async_publish
from .const import ATTR_DISCOVERY_HASH as ATTR_DISCOVERY_HASH, ATTR_DISCOVERY_PAYLOAD as ATTR_DISCOVERY_PAYLOAD, ATTR_DISCOVERY_TOPIC as ATTR_DISCOVERY_TOPIC, CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_CONFIGURATION_URL as CONF_CONFIGURATION_URL, CONF_CONNECTIONS as CONF_CONNECTIONS, CONF_DEPRECATED_VIA_HUB as CONF_DEPRECATED_VIA_HUB, CONF_ENCODING as CONF_ENCODING, CONF_HW_VERSION as CONF_HW_VERSION, CONF_IDENTIFIERS as CONF_IDENTIFIERS, CONF_MANUFACTURER as CONF_MANUFACTURER, CONF_OBJECT_ID as CONF_OBJECT_ID, CONF_ORIGIN as CONF_ORIGIN, CONF_QOS as CONF_QOS, CONF_SCHEMA as CONF_SCHEMA, CONF_SUGGESTED_AREA as CONF_SUGGESTED_AREA, CONF_SW_VERSION as CONF_SW_VERSION, CONF_TOPIC as CONF_TOPIC, CONF_VIA_DEVICE as CONF_VIA_DEVICE, DEFAULT_ENCODING as DEFAULT_ENCODING, DEFAULT_PAYLOAD_AVAILABLE as DEFAULT_PAYLOAD_AVAILABLE, DEFAULT_PAYLOAD_NOT_AVAILABLE as DEFAULT_PAYLOAD_NOT_AVAILABLE, DOMAIN as DOMAIN, MQTT_CONNECTED as MQTT_CONNECTED, MQTT_DISCONNECTED as MQTT_DISCONNECTED
from .debug_info import log_message as log_message, log_messages as log_messages
from .discovery import MQTTDiscoveryPayload as MQTTDiscoveryPayload, MQTT_DISCOVERY_DONE as MQTT_DISCOVERY_DONE, MQTT_DISCOVERY_NEW as MQTT_DISCOVERY_NEW, MQTT_DISCOVERY_UPDATED as MQTT_DISCOVERY_UPDATED, MQTT_ORIGIN_INFO_SCHEMA as MQTT_ORIGIN_INFO_SCHEMA, clear_discovery_hash as clear_discovery_hash, set_discovery_hash as set_discovery_hash
from .models import MessageCallbackType as MessageCallbackType, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .subscription import EntitySubscription as EntitySubscription, async_prepare_subscribe_topics as async_prepare_subscribe_topics, async_subscribe_topics as async_subscribe_topics, async_unsubscribe_topics as async_unsubscribe_topics
from .util import get_mqtt_data as get_mqtt_data, mqtt_config_entry_enabled as mqtt_config_entry_enabled, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Callable as Callable, Coroutine
from functools import partial
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONFIGURATION_URL as ATTR_CONFIGURATION_URL, ATTR_HW_VERSION as ATTR_HW_VERSION, ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_NAME as ATTR_NAME, ATTR_SUGGESTED_AREA as ATTR_SUGGESTED_AREA, ATTR_SW_VERSION as ATTR_SW_VERSION, ATTR_VIA_DEVICE as ATTR_VIA_DEVICE, CONF_DEVICE as CONF_DEVICE, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_ICON as CONF_ICON, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, EntityCategory as EntityCategory
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, async_get_hass as async_get_hass, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry, DeviceInfo as DeviceInfo, EventDeviceRegistryUpdatedData as EventDeviceRegistryUpdatedData
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import ENTITY_CATEGORIES_SCHEMA as ENTITY_CATEGORIES_SCHEMA, Entity as Entity, async_generate_entity_id as async_generate_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_device_registry_updated_event as async_track_device_registry_updated_event, async_track_entity_registry_updated_event as async_track_entity_registry_updated_event
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, EventType as EventType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from homeassistant.util.json import json_loads as json_loads
from typing import Any, Protocol

_LOGGER: Incomplete
AVAILABILITY_ALL: str
AVAILABILITY_ANY: str
AVAILABILITY_LATEST: str
AVAILABILITY_MODES: Incomplete
CONF_AVAILABILITY_MODE: str
CONF_AVAILABILITY_TEMPLATE: str
CONF_AVAILABILITY_TOPIC: str
CONF_ENABLED_BY_DEFAULT: str
CONF_PAYLOAD_AVAILABLE: str
CONF_PAYLOAD_NOT_AVAILABLE: str
CONF_JSON_ATTRS_TOPIC: str
CONF_JSON_ATTRS_TEMPLATE: str
MQTT_ATTRIBUTES_BLOCKED: Incomplete
MQTT_AVAILABILITY_SINGLE_SCHEMA: Incomplete
MQTT_AVAILABILITY_LIST_SCHEMA: Incomplete
MQTT_AVAILABILITY_SCHEMA: Incomplete

def validate_device_has_at_least_one_identifier(value: ConfigType) -> ConfigType: ...
def validate_sensor_entity_category(domain: str, discovery: bool) -> Callable[[ConfigType], ConfigType]: ...

MQTT_ENTITY_DEVICE_INFO_SCHEMA: Incomplete
MQTT_ENTITY_COMMON_SCHEMA: Incomplete

class SetupEntity(Protocol):
    async def __call__(self, hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = None) -> None: ...

def async_handle_schema_error(discovery_payload: MQTTDiscoveryPayload, err: vol.MultipleInvalid) -> None: ...
async def _async_discover(hass: HomeAssistant, domain: str, setup: partial[CALLBACK_TYPE] | None, async_setup: partial[Coroutine[Any, Any, None]] | None, discovery_payload: MQTTDiscoveryPayload) -> None: ...
async def async_setup_non_entity_entry_helper(hass: HomeAssistant, domain: str, async_setup: partial[Coroutine[Any, Any, None]], discovery_schema: vol.Schema) -> None: ...
async def async_setup_entity_entry_helper(hass: HomeAssistant, entry: ConfigEntry, entity_class: type[MqttEntity] | None, domain: str, async_add_entities: AddEntitiesCallback, discovery_schema: vol.Schema, platform_schema_modern: vol.Schema, schema_class_mapping: dict[str, type[MqttEntity]] | None = None) -> None: ...
def init_entity_id_from_config(hass: HomeAssistant, entity: Entity, config: ConfigType, entity_id_format: str) -> None: ...
def write_state_on_attr_change(entity: Entity, attributes: set[str]) -> Callable[[MessageCallbackType], MessageCallbackType]: ...

class MqttAttributes(Entity):
    _attributes_extra_blocked: frozenset[str]
    _attributes_sub_state: Incomplete
    _attributes_config: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def attributes_prepare_discovery_update(self, config: DiscoveryInfoType) -> None: ...
    async def attributes_discovery_update(self, config: DiscoveryInfoType) -> None: ...
    _attr_extra_state_attributes: Incomplete
    def _attributes_prepare_subscribe_topics(self) -> None: ...
    async def _attributes_subscribe_topics(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...

class MqttAvailability(Entity):
    _availability_sub_state: Incomplete
    _available: Incomplete
    _available_latest: bool
    def __init__(self, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def availability_prepare_discovery_update(self, config: DiscoveryInfoType) -> None: ...
    async def availability_discovery_update(self, config: DiscoveryInfoType) -> None: ...
    _avail_topics: Incomplete
    _avail_config: Incomplete
    def _availability_setup_from_config(self, config: ConfigType) -> None: ...
    def _availability_prepare_subscribe_topics(self) -> None: ...
    async def _availability_subscribe_topics(self) -> None: ...
    def async_mqtt_connect(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...

async def cleanup_device_registry(hass: HomeAssistant, device_id: str | None, config_entry_id: str | None) -> None: ...
def get_discovery_hash(discovery_data: DiscoveryInfoType) -> tuple[str, str]: ...
def send_discovery_done(hass: HomeAssistant, discovery_data: DiscoveryInfoType) -> None: ...
def stop_discovery_updates(hass: HomeAssistant, discovery_data: DiscoveryInfoType, remove_discovery_updated: Callable[[], None] | None = None) -> None: ...
async def async_remove_discovery_payload(hass: HomeAssistant, discovery_data: DiscoveryInfoType) -> None: ...
async def async_clear_discovery_topic_if_entity_removed(hass: HomeAssistant, discovery_data: DiscoveryInfoType, event: EventType[er.EventEntityRegistryUpdatedData]) -> None: ...

class MqttDiscoveryDeviceUpdate(ABC, metaclass=abc.ABCMeta):
    hass: Incomplete
    log_name: Incomplete
    _discovery_data: Incomplete
    _device_id: Incomplete
    _config_entry: Incomplete
    _config_entry_id: Incomplete
    _skip_device_removal: bool
    _remove_discovery_updated: Incomplete
    _remove_device_updated: Incomplete
    def __init__(self, hass: HomeAssistant, discovery_data: DiscoveryInfoType, device_id: str | None, config_entry: ConfigEntry, log_name: str) -> None: ...
    def _entry_unload(self, *_: Any) -> None: ...
    async def async_discovery_update(self, discovery_payload: MQTTDiscoveryPayload) -> None: ...
    async def _async_device_removed(self, event: EventType[EventDeviceRegistryUpdatedData]) -> None: ...
    async def _async_tear_down(self) -> None: ...
    @abstractmethod
    async def async_update(self, discovery_data: MQTTDiscoveryPayload) -> None: ...
    @abstractmethod
    async def async_tear_down(self) -> None: ...

class MqttDiscoveryUpdate(Entity):
    _discovery_data: Incomplete
    _discovery_update: Incomplete
    _remove_discovery_updated: Incomplete
    _removed_from_hass: bool
    _registry_hooks: Incomplete
    def __init__(self, hass: HomeAssistant, discovery_data: DiscoveryInfoType | None, discovery_update: Callable[[MQTTDiscoveryPayload], Coroutine[Any, Any, None]] | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_removed_from_registry(self) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _cleanup_discovery_on_remove(self) -> None: ...

def device_info_from_specifications(specifications: dict[str, Any] | None) -> DeviceInfo | None: ...

class MqttEntityDeviceInfo(Entity):
    _device_specifications: Incomplete
    _config_entry: Incomplete
    def __init__(self, specifications: dict[str, Any] | None, config_entry: ConfigEntry) -> None: ...
    def device_info_discovery_update(self, config: DiscoveryInfoType) -> None: ...
    @property
    def device_info(self) -> DeviceInfo | None: ...

class MqttEntity(MqttAttributes, MqttAvailability, MqttDiscoveryUpdate, MqttEntityDeviceInfo, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _default_name: str | None
    _entity_id_format: str
    _issue_key: str | None
    hass: Incomplete
    _config: Incomplete
    _attr_unique_id: Incomplete
    _sub_state: Incomplete
    _discovery: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    def _init_entity_id(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def mqtt_async_added_to_hass(self) -> None: ...
    async def discovery_update(self, discovery_payload: MQTTDiscoveryPayload) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_publish(self, topic: str, payload: PublishPayloadType, qos: int = 0, retain: bool = False, encoding: str | None = ...) -> None: ...
    @staticmethod
    @abstractmethod
    def config_schema() -> vol.Schema: ...
    _attr_name: Incomplete
    def _set_entity_name(self, config: ConfigType) -> None: ...
    def collect_issues(self) -> None: ...
    _attr_entity_category: Incomplete
    _attr_entity_registry_enabled_default: Incomplete
    _attr_icon: Incomplete
    def _setup_common_attributes_from_config(self, config: ConfigType) -> None: ...
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @abstractmethod
    def _prepare_subscribe_topics(self) -> None: ...
    @abstractmethod
    async def _subscribe_topics(self) -> None: ...

def update_device(hass: HomeAssistant, config_entry: ConfigEntry, config: ConfigType) -> str | None: ...
def async_removed_from_device(hass: HomeAssistant, event: EventType[EventDeviceRegistryUpdatedData], mqtt_device_id: str, config_entry_id: str) -> bool: ...
