import voluptuous as vol
from .. import subscription as subscription
from ..config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from ..const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, PAYLOAD_NONE as PAYLOAD_NONE
from ..debug_info import log_messages as log_messages
from ..mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity
from ..models import MessageCallbackType as MessageCallbackType, MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType, TemplateVarsType as TemplateVarsType
from ..util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from .schema import MQTT_LIGHT_SCHEMA_SCHEMA as MQTT_LIGHT_SCHEMA_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_EFFECT_LIST as ATTR_EFFECT_LIST, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_MAX_MIREDS as ATTR_MAX_MIREDS, ATTR_MIN_MIREDS as ATTR_MIN_MIREDS, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, ATTR_WHITE as ATTR_WHITE, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, valid_supported_color_modes as valid_supported_color_modes
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
CONF_BRIGHTNESS_COMMAND_TEMPLATE: str
CONF_BRIGHTNESS_COMMAND_TOPIC: str
CONF_BRIGHTNESS_SCALE: str
CONF_BRIGHTNESS_STATE_TOPIC: str
CONF_BRIGHTNESS_VALUE_TEMPLATE: str
CONF_COLOR_MODE_STATE_TOPIC: str
CONF_COLOR_MODE_VALUE_TEMPLATE: str
CONF_COLOR_TEMP_COMMAND_TEMPLATE: str
CONF_COLOR_TEMP_COMMAND_TOPIC: str
CONF_COLOR_TEMP_STATE_TOPIC: str
CONF_COLOR_TEMP_VALUE_TEMPLATE: str
CONF_EFFECT_COMMAND_TEMPLATE: str
CONF_EFFECT_COMMAND_TOPIC: str
CONF_EFFECT_LIST: str
CONF_EFFECT_STATE_TOPIC: str
CONF_EFFECT_VALUE_TEMPLATE: str
CONF_HS_COMMAND_TEMPLATE: str
CONF_HS_COMMAND_TOPIC: str
CONF_HS_STATE_TOPIC: str
CONF_HS_VALUE_TEMPLATE: str
CONF_MAX_MIREDS: str
CONF_MIN_MIREDS: str
CONF_RGB_COMMAND_TEMPLATE: str
CONF_RGB_COMMAND_TOPIC: str
CONF_RGB_STATE_TOPIC: str
CONF_RGB_VALUE_TEMPLATE: str
CONF_RGBW_COMMAND_TEMPLATE: str
CONF_RGBW_COMMAND_TOPIC: str
CONF_RGBW_STATE_TOPIC: str
CONF_RGBW_VALUE_TEMPLATE: str
CONF_RGBWW_COMMAND_TEMPLATE: str
CONF_RGBWW_COMMAND_TOPIC: str
CONF_RGBWW_STATE_TOPIC: str
CONF_RGBWW_VALUE_TEMPLATE: str
CONF_XY_COMMAND_TEMPLATE: str
CONF_XY_COMMAND_TOPIC: str
CONF_XY_STATE_TOPIC: str
CONF_XY_VALUE_TEMPLATE: str
CONF_WHITE_COMMAND_TOPIC: str
CONF_WHITE_SCALE: str
CONF_ON_COMMAND_TYPE: str
MQTT_LIGHT_ATTRIBUTES_BLOCKED: Incomplete
DEFAULT_BRIGHTNESS_SCALE: int
DEFAULT_NAME: str
DEFAULT_PAYLOAD_OFF: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_WHITE_SCALE: int
DEFAULT_ON_COMMAND_TYPE: str
VALUES_ON_COMMAND_TYPE: Incomplete
COMMAND_TEMPLATE_KEYS: Incomplete
VALUE_TEMPLATE_KEYS: Incomplete
PLATFORM_SCHEMA_MODERN_BASIC: Incomplete
DISCOVERY_SCHEMA_BASIC: Incomplete

async def async_setup_entity_basic(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...

class MqttLight(MqttEntity, LightEntity, RestoreEntity):
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_LIGHT_ATTRIBUTES_BLOCKED
    _topic: dict[str, str | None]
    _payload: dict[str, str]
    _command_templates: dict[str, Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType, ReceivePayloadType], ReceivePayloadType]]
    _optimistic: bool
    _optimistic_brightness: bool
    _optimistic_color_mode: bool
    _optimistic_color_temp: bool
    _optimistic_effect: bool
    _optimistic_hs_color: bool
    _optimistic_rgb_color: bool
    _optimistic_rgbw_color: bool
    _optimistic_rgbww_color: bool
    _optimistic_xy_color: bool
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_min_mireds: Incomplete
    _attr_max_mireds: Incomplete
    _attr_effect_list: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    def _is_optimistic(self, attribute: str) -> bool: ...
    _attr_is_on: bool
    _attr_brightness: Incomplete
    _attr_rgb_color: Incomplete
    _attr_rgbw_color: Incomplete
    _attr_rgbww_color: Incomplete
    _attr_color_temp: Incomplete
    _attr_effect: Incomplete
    _attr_hs_color: Incomplete
    _attr_xy_color: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
