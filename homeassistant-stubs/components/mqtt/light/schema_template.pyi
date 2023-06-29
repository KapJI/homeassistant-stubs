import voluptuous as vol
from .. import subscription as subscription
from ..config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from ..const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_NONE as PAYLOAD_NONE
from ..debug_info import log_messages as log_messages
from ..mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity
from ..models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from ..util import get_mqtt_data as get_mqtt_data
from .schema import MQTT_LIGHT_SCHEMA_SCHEMA as MQTT_LIGHT_SCHEMA_SCHEMA
from .schema_basic import MQTT_LIGHT_ATTRIBUTES_BLOCKED as MQTT_LIGHT_ATTRIBUTES_BLOCKED
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature, filter_supported_color_modes as filter_supported_color_modes
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_STATE_TEMPLATE as CONF_STATE_TEMPLATE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, TemplateVarsType as TemplateVarsType
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DEFAULT_NAME: str
CONF_BLUE_TEMPLATE: str
CONF_BRIGHTNESS_TEMPLATE: str
CONF_COLOR_TEMP_TEMPLATE: str
CONF_COMMAND_OFF_TEMPLATE: str
CONF_COMMAND_ON_TEMPLATE: str
CONF_EFFECT_LIST: str
CONF_EFFECT_TEMPLATE: str
CONF_GREEN_TEMPLATE: str
CONF_MAX_MIREDS: str
CONF_MIN_MIREDS: str
CONF_RED_TEMPLATE: str
COMMAND_TEMPLATES: Incomplete
VALUE_TEMPLATES: Incomplete
PLATFORM_SCHEMA_MODERN_TEMPLATE: Incomplete
DISCOVERY_SCHEMA_TEMPLATE: Incomplete

async def async_setup_entity_template(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...

class MqttLightTemplate(MqttEntity, LightEntity, RestoreEntity):
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_LIGHT_ATTRIBUTES_BLOCKED
    _optimistic: bool
    _command_templates: dict[str, Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType], ReceivePayloadType]]
    _fixed_color_mode: ColorMode | str | None
    _topics: dict[str, str | None]
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_max_mireds: Incomplete
    _attr_min_mireds: Incomplete
    _attr_effect_list: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    def _update_color_mode(self) -> None: ...
    _attr_is_on: bool
    _attr_brightness: Incomplete
    _attr_color_temp: Incomplete
    _attr_hs_color: Incomplete
    _attr_effect: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
