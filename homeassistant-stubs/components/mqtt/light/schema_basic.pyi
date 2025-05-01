from .. import subscription as subscription
from ..config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from ..const import CONF_BRIGHTNESS_COMMAND_TEMPLATE as CONF_BRIGHTNESS_COMMAND_TEMPLATE, CONF_BRIGHTNESS_COMMAND_TOPIC as CONF_BRIGHTNESS_COMMAND_TOPIC, CONF_BRIGHTNESS_SCALE as CONF_BRIGHTNESS_SCALE, CONF_BRIGHTNESS_STATE_TOPIC as CONF_BRIGHTNESS_STATE_TOPIC, CONF_BRIGHTNESS_VALUE_TEMPLATE as CONF_BRIGHTNESS_VALUE_TEMPLATE, CONF_COLOR_MODE_STATE_TOPIC as CONF_COLOR_MODE_STATE_TOPIC, CONF_COLOR_MODE_VALUE_TEMPLATE as CONF_COLOR_MODE_VALUE_TEMPLATE, CONF_COLOR_TEMP_COMMAND_TEMPLATE as CONF_COLOR_TEMP_COMMAND_TEMPLATE, CONF_COLOR_TEMP_COMMAND_TOPIC as CONF_COLOR_TEMP_COMMAND_TOPIC, CONF_COLOR_TEMP_KELVIN as CONF_COLOR_TEMP_KELVIN, CONF_COLOR_TEMP_STATE_TOPIC as CONF_COLOR_TEMP_STATE_TOPIC, CONF_COLOR_TEMP_VALUE_TEMPLATE as CONF_COLOR_TEMP_VALUE_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_EFFECT_COMMAND_TEMPLATE as CONF_EFFECT_COMMAND_TEMPLATE, CONF_EFFECT_COMMAND_TOPIC as CONF_EFFECT_COMMAND_TOPIC, CONF_EFFECT_LIST as CONF_EFFECT_LIST, CONF_EFFECT_STATE_TOPIC as CONF_EFFECT_STATE_TOPIC, CONF_EFFECT_VALUE_TEMPLATE as CONF_EFFECT_VALUE_TEMPLATE, CONF_HS_COMMAND_TEMPLATE as CONF_HS_COMMAND_TEMPLATE, CONF_HS_COMMAND_TOPIC as CONF_HS_COMMAND_TOPIC, CONF_HS_STATE_TOPIC as CONF_HS_STATE_TOPIC, CONF_HS_VALUE_TEMPLATE as CONF_HS_VALUE_TEMPLATE, CONF_MAX_KELVIN as CONF_MAX_KELVIN, CONF_MAX_MIREDS as CONF_MAX_MIREDS, CONF_MIN_KELVIN as CONF_MIN_KELVIN, CONF_MIN_MIREDS as CONF_MIN_MIREDS, CONF_ON_COMMAND_TYPE as CONF_ON_COMMAND_TYPE, CONF_RGBWW_COMMAND_TEMPLATE as CONF_RGBWW_COMMAND_TEMPLATE, CONF_RGBWW_COMMAND_TOPIC as CONF_RGBWW_COMMAND_TOPIC, CONF_RGBWW_STATE_TOPIC as CONF_RGBWW_STATE_TOPIC, CONF_RGBWW_VALUE_TEMPLATE as CONF_RGBWW_VALUE_TEMPLATE, CONF_RGBW_COMMAND_TEMPLATE as CONF_RGBW_COMMAND_TEMPLATE, CONF_RGBW_COMMAND_TOPIC as CONF_RGBW_COMMAND_TOPIC, CONF_RGBW_STATE_TOPIC as CONF_RGBW_STATE_TOPIC, CONF_RGBW_VALUE_TEMPLATE as CONF_RGBW_VALUE_TEMPLATE, CONF_RGB_COMMAND_TEMPLATE as CONF_RGB_COMMAND_TEMPLATE, CONF_RGB_COMMAND_TOPIC as CONF_RGB_COMMAND_TOPIC, CONF_RGB_STATE_TOPIC as CONF_RGB_STATE_TOPIC, CONF_RGB_VALUE_TEMPLATE as CONF_RGB_VALUE_TEMPLATE, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, CONF_WHITE_COMMAND_TOPIC as CONF_WHITE_COMMAND_TOPIC, CONF_WHITE_SCALE as CONF_WHITE_SCALE, CONF_XY_COMMAND_TEMPLATE as CONF_XY_COMMAND_TEMPLATE, CONF_XY_COMMAND_TOPIC as CONF_XY_COMMAND_TOPIC, CONF_XY_STATE_TOPIC as CONF_XY_STATE_TOPIC, CONF_XY_VALUE_TEMPLATE as CONF_XY_VALUE_TEMPLATE, DEFAULT_BRIGHTNESS_SCALE as DEFAULT_BRIGHTNESS_SCALE, DEFAULT_ON_COMMAND_TYPE as DEFAULT_ON_COMMAND_TYPE, DEFAULT_PAYLOAD_OFF as DEFAULT_PAYLOAD_OFF, DEFAULT_PAYLOAD_ON as DEFAULT_PAYLOAD_ON, DEFAULT_WHITE_SCALE as DEFAULT_WHITE_SCALE, PAYLOAD_NONE as PAYLOAD_NONE, VALUES_ON_COMMAND_TYPE as VALUES_ON_COMMAND_TYPE
from ..entity import MqttEntity as MqttEntity
from ..models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, TemplateVarsType as TemplateVarsType
from ..schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from ..util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from .schema import MQTT_LIGHT_SCHEMA_SCHEMA as MQTT_LIGHT_SCHEMA_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_EFFECT as ATTR_EFFECT, ATTR_EFFECT_LIST as ATTR_EFFECT_LIST, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_MAX_COLOR_TEMP_KELVIN as ATTR_MAX_COLOR_TEMP_KELVIN, ATTR_MIN_COLOR_TEMP_KELVIN as ATTR_MIN_COLOR_TEMP_KELVIN, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, ATTR_WHITE as ATTR_WHITE, ATTR_XY_COLOR as ATTR_XY_COLOR, ColorMode as ColorMode, DEFAULT_MAX_KELVIN as DEFAULT_MAX_KELVIN, DEFAULT_MIN_KELVIN as DEFAULT_MIN_KELVIN, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, _DEPRECATED_ATTR_COLOR_TEMP as _DEPRECATED_ATTR_COLOR_TEMP, _DEPRECATED_ATTR_MAX_MIREDS as _DEPRECATED_ATTR_MAX_MIREDS, _DEPRECATED_ATTR_MIN_MIREDS as _DEPRECATED_ATTR_MIN_MIREDS, valid_supported_color_modes as valid_supported_color_modes
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, STATE_ON as STATE_ON
from homeassistant.core import callback as callback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from typing import Any

_LOGGER: Incomplete
DEFAULT_NAME: str
MQTT_LIGHT_ATTRIBUTES_BLOCKED: Incomplete
COMMAND_TEMPLATE_KEYS: Incomplete
VALUE_TEMPLATE_KEYS: Incomplete
PLATFORM_SCHEMA_MODERN_BASIC: Incomplete
DISCOVERY_SCHEMA_BASIC: Incomplete

class MqttLight(MqttEntity, LightEntity, RestoreEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_LIGHT_ATTRIBUTES_BLOCKED
    _topic: dict[str, str | None]
    _payload: dict[str, str]
    _color_temp_kelvin: bool
    _command_templates: dict[str, Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType, ReceivePayloadType], ReceivePayloadType]]
    _optimistic: bool
    _optimistic_brightness: bool
    _optimistic_color_mode: bool
    _optimistic_color_temp_kelvin: bool
    _optimistic_effect: bool
    _optimistic_hs_color: bool
    _optimistic_rgb_color: bool
    _optimistic_rgbw_color: bool
    _optimistic_rgbww_color: bool
    _optimistic_xy_color: bool
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_min_color_temp_kelvin: Incomplete
    _attr_max_color_temp_kelvin: Incomplete
    _attr_effect_list: Incomplete
    _attr_assumed_state: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    def _is_optimistic(self, attribute: str) -> bool: ...
    _attr_is_on: bool
    @callback
    def _state_received(self, msg: ReceiveMessage) -> None: ...
    _attr_brightness: Incomplete
    @callback
    def _brightness_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _rgbx_received(self, msg: ReceiveMessage, template: str, color_mode: ColorMode, convert_color: Callable[..., tuple[int, ...]]) -> tuple[int, ...] | None: ...
    _attr_rgb_color: Incomplete
    @callback
    def _rgb_received(self, msg: ReceiveMessage) -> None: ...
    _attr_rgbw_color: Incomplete
    @callback
    def _rgbw_received(self, msg: ReceiveMessage) -> None: ...
    _attr_rgbww_color: Incomplete
    @callback
    def _rgbww_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _color_mode_received(self, msg: ReceiveMessage) -> None: ...
    _attr_color_temp_kelvin: Incomplete
    @callback
    def _color_temp_received(self, msg: ReceiveMessage) -> None: ...
    _attr_effect: Incomplete
    @callback
    def _effect_received(self, msg: ReceiveMessage) -> None: ...
    _attr_hs_color: Incomplete
    @callback
    def _hs_received(self, msg: ReceiveMessage) -> None: ...
    _attr_xy_color: Incomplete
    @callback
    def _xy_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
