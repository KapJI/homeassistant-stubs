import voluptuous as vol
from . import subscription as subscription
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_RO_SCHEMA as MQTT_RO_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_EMPTY_JSON as PAYLOAD_EMPTY_JSON
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper
from .models import MessageCallbackType as MessageCallbackType, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import update as update
from homeassistant.components.update import DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from typing import Any, TypedDict

_LOGGER: Incomplete
DEFAULT_NAME: str
CONF_ENTITY_PICTURE: str
CONF_LATEST_VERSION_TEMPLATE: str
CONF_LATEST_VERSION_TOPIC: str
CONF_PAYLOAD_INSTALL: str
CONF_RELEASE_SUMMARY: str
CONF_RELEASE_URL: str
CONF_TITLE: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

class _MqttUpdatePayloadType(TypedDict, total=False):
    installed_version: str
    latest_version: str
    title: str
    release_summary: str
    release_url: str
    entity_picture: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = ...) -> None: ...

class MqttUpdate(MqttEntity, UpdateEntity, RestoreEntity):
    _entity_id_format: Incomplete
    _config: Incomplete
    _attr_device_class: Incomplete
    _attr_release_summary: Incomplete
    _attr_release_url: Incomplete
    _attr_title: Incomplete
    _entity_picture: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = ...) -> None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _templates: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    @property
    def supported_features(self) -> UpdateEntityFeature: ...
