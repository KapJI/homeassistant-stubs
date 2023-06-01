import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, PAYLOAD_NONE as PAYLOAD_NONE
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper
from .models import MessageCallbackType as MessageCallbackType, MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import fan as fan
from homeassistant.components.fan import ATTR_DIRECTION as ATTR_DIRECTION, ATTR_OSCILLATING as ATTR_OSCILLATING, ATTR_PERCENTAGE as ATTR_PERCENTAGE, ATTR_PRESET_MODE as ATTR_PRESET_MODE, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_STATE as CONF_STATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.percentage import int_states_in_range as int_states_in_range, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

CONF_DIRECTION_STATE_TOPIC: str
CONF_DIRECTION_COMMAND_TOPIC: str
CONF_DIRECTION_VALUE_TEMPLATE: str
CONF_DIRECTION_COMMAND_TEMPLATE: str
CONF_PERCENTAGE_STATE_TOPIC: str
CONF_PERCENTAGE_COMMAND_TOPIC: str
CONF_PERCENTAGE_VALUE_TEMPLATE: str
CONF_PERCENTAGE_COMMAND_TEMPLATE: str
CONF_PAYLOAD_RESET_PERCENTAGE: str
CONF_SPEED_RANGE_MIN: str
CONF_SPEED_RANGE_MAX: str
CONF_PRESET_MODE_STATE_TOPIC: str
CONF_PRESET_MODE_COMMAND_TOPIC: str
CONF_PRESET_MODE_VALUE_TEMPLATE: str
CONF_PRESET_MODE_COMMAND_TEMPLATE: str
CONF_PRESET_MODES_LIST: str
CONF_PAYLOAD_RESET_PRESET_MODE: str
CONF_OSCILLATION_STATE_TOPIC: str
CONF_OSCILLATION_COMMAND_TOPIC: str
CONF_OSCILLATION_VALUE_TEMPLATE: str
CONF_OSCILLATION_COMMAND_TEMPLATE: str
CONF_PAYLOAD_OSCILLATION_ON: str
CONF_PAYLOAD_OSCILLATION_OFF: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
DEFAULT_PAYLOAD_RESET: str
DEFAULT_SPEED_RANGE_MIN: int
DEFAULT_SPEED_RANGE_MAX: int
OSCILLATE_ON_PAYLOAD: str
OSCILLATE_OFF_PAYLOAD: str
MQTT_FAN_ATTRIBUTES_BLOCKED: Incomplete
_LOGGER: Incomplete

def valid_speed_range_configuration(config: ConfigType) -> ConfigType: ...
def valid_preset_mode_configuration(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = ...) -> None: ...

class MqttFan(MqttEntity, FanEntity):
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_FAN_ATTRIBUTES_BLOCKED
    _command_templates: dict[str, Callable[[PublishPayloadType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType], ReceivePayloadType]]
    _feature_percentage: bool
    _feature_preset_mode: bool
    _topic: dict[str, Any]
    _optimistic: bool
    _optimistic_direction: bool
    _optimistic_oscillation: bool
    _optimistic_percentage: bool
    _optimistic_preset_mode: bool
    _payload: dict[str, Any]
    _speed_range: tuple[int, int]
    _attr_percentage: Incomplete
    _attr_preset_mode: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_on: bool
    _attr_oscillating: bool
    _attr_current_direction: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, percentage: int | None = ..., preset_mode: str | None = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
