import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, PAYLOAD_NONE as PAYLOAD_NONE
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper, warn_for_legacy_schema as warn_for_legacy_schema
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import humidifier as humidifier
from homeassistant.components.humidifier import ATTR_HUMIDITY as ATTR_HUMIDITY, ATTR_MODE as ATTR_MODE, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityFeature as HumidifierEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_STATE as CONF_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

CONF_AVAILABLE_MODES_LIST: str
CONF_DEVICE_CLASS: str
CONF_MODE_COMMAND_TEMPLATE: str
CONF_MODE_COMMAND_TOPIC: str
CONF_MODE_STATE_TOPIC: str
CONF_MODE_STATE_TEMPLATE: str
CONF_PAYLOAD_RESET_MODE: str
CONF_PAYLOAD_RESET_HUMIDITY: str
CONF_TARGET_HUMIDITY_COMMAND_TEMPLATE: str
CONF_TARGET_HUMIDITY_COMMAND_TOPIC: str
CONF_TARGET_HUMIDITY_MIN: str
CONF_TARGET_HUMIDITY_MAX: str
CONF_TARGET_HUMIDITY_STATE_TEMPLATE: str
CONF_TARGET_HUMIDITY_STATE_TOPIC: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
DEFAULT_PAYLOAD_RESET: str
MQTT_HUMIDIFIER_ATTRIBUTES_BLOCKED: Incomplete
_LOGGER: Incomplete

def valid_mode_configuration(config: ConfigType) -> ConfigType: ...
def valid_humidity_range_configuration(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None] = ...) -> None: ...

class MqttHumidifier(MqttEntity, HumidifierEntity):
    _entity_id_format: Incomplete
    _attributes_extra_blocked: Incomplete
    _command_templates: dict[str, Callable[[PublishPayloadType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType], ReceivePayloadType]]
    _optimistic: bool
    _optimistic_target_humidity: bool
    _optimistic_mode: bool
    _payload: dict[str, str]
    _topic: dict[str, Any]
    _attr_mode: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_device_class: Incomplete
    _attr_min_humidity: Incomplete
    _attr_max_humidity: Incomplete
    _attr_available_modes: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_on: bool
    _attr_target_humidity: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_mode(self, mode: str) -> None: ...
