import voluptuous as vol
from . import subscription as subscription
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC, PAYLOAD_NONE as PAYLOAD_NONE
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper, warn_for_legacy_schema as warn_for_legacy_schema
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import climate as climate
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, DEFAULT_MAX_HUMIDITY as DEFAULT_MAX_HUMIDITY, DEFAULT_MAX_TEMP as DEFAULT_MAX_TEMP, DEFAULT_MIN_HUMIDITY as DEFAULT_MIN_HUMIDITY, DEFAULT_MIN_TEMP as DEFAULT_MIN_TEMP, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE, SWING_OFF as SWING_OFF, SWING_ON as SWING_ON
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
DEFAULT_NAME: str
CONF_ACTION_TEMPLATE: str
CONF_ACTION_TOPIC: str
CONF_AUX_COMMAND_TOPIC: str
CONF_AUX_STATE_TEMPLATE: str
CONF_AUX_STATE_TOPIC: str
CONF_AWAY_MODE_COMMAND_TOPIC: str
CONF_AWAY_MODE_STATE_TEMPLATE: str
CONF_AWAY_MODE_STATE_TOPIC: str
CONF_CURRENT_HUMIDITY_TEMPLATE: str
CONF_CURRENT_HUMIDITY_TOPIC: str
CONF_CURRENT_TEMP_TEMPLATE: str
CONF_CURRENT_TEMP_TOPIC: str
CONF_FAN_MODE_COMMAND_TEMPLATE: str
CONF_FAN_MODE_COMMAND_TOPIC: str
CONF_FAN_MODE_LIST: str
CONF_FAN_MODE_STATE_TEMPLATE: str
CONF_FAN_MODE_STATE_TOPIC: str
CONF_HOLD_COMMAND_TEMPLATE: str
CONF_HOLD_COMMAND_TOPIC: str
CONF_HOLD_STATE_TEMPLATE: str
CONF_HOLD_STATE_TOPIC: str
CONF_HOLD_LIST: str
CONF_HUMIDITY_COMMAND_TEMPLATE: str
CONF_HUMIDITY_COMMAND_TOPIC: str
CONF_HUMIDITY_STATE_TEMPLATE: str
CONF_HUMIDITY_STATE_TOPIC: str
CONF_HUMIDITY_MAX: str
CONF_HUMIDITY_MIN: str
CONF_MODE_COMMAND_TEMPLATE: str
CONF_MODE_COMMAND_TOPIC: str
CONF_MODE_LIST: str
CONF_MODE_STATE_TEMPLATE: str
CONF_MODE_STATE_TOPIC: str
CONF_POWER_COMMAND_TOPIC: str
CONF_POWER_STATE_TEMPLATE: str
CONF_POWER_STATE_TOPIC: str
CONF_PRECISION: str
CONF_PRESET_MODE_STATE_TOPIC: str
CONF_PRESET_MODE_COMMAND_TOPIC: str
CONF_PRESET_MODE_VALUE_TEMPLATE: str
CONF_PRESET_MODE_COMMAND_TEMPLATE: str
CONF_PRESET_MODES_LIST: str
CONF_SEND_IF_OFF: str
CONF_SWING_MODE_COMMAND_TEMPLATE: str
CONF_SWING_MODE_COMMAND_TOPIC: str
CONF_SWING_MODE_LIST: str
CONF_SWING_MODE_STATE_TEMPLATE: str
CONF_SWING_MODE_STATE_TOPIC: str
CONF_TEMP_COMMAND_TEMPLATE: str
CONF_TEMP_COMMAND_TOPIC: str
CONF_TEMP_HIGH_COMMAND_TEMPLATE: str
CONF_TEMP_HIGH_COMMAND_TOPIC: str
CONF_TEMP_HIGH_STATE_TEMPLATE: str
CONF_TEMP_HIGH_STATE_TOPIC: str
CONF_TEMP_LOW_COMMAND_TEMPLATE: str
CONF_TEMP_LOW_COMMAND_TOPIC: str
CONF_TEMP_LOW_STATE_TEMPLATE: str
CONF_TEMP_LOW_STATE_TOPIC: str
CONF_TEMP_STATE_TEMPLATE: str
CONF_TEMP_STATE_TOPIC: str
CONF_TEMP_INITIAL: str
CONF_TEMP_MAX: str
CONF_TEMP_MIN: str
CONF_TEMP_STEP: str
MQTT_CLIMATE_ATTRIBUTES_BLOCKED: Incomplete
VALUE_TEMPLATE_KEYS: Incomplete
COMMAND_TEMPLATE_KEYS: Incomplete
TOPIC_KEYS: Incomplete

def valid_preset_mode_configuration(config: ConfigType) -> ConfigType: ...
def valid_humidity_range_configuration(config: ConfigType) -> ConfigType: ...
def valid_humidity_state_configuration(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
PLATFORM_SCHEMA: Incomplete
_DISCOVERY_SCHEMA_BASE: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None] = ...) -> None: ...

class MqttClimate(MqttEntity, ClimateEntity):
    _entity_id_format: Incomplete
    _attributes_extra_blocked: Incomplete
    _command_templates: dict[str, Callable[[PublishPayloadType], PublishPayloadType]]
    _value_templates: dict[str, Callable[[ReceivePayloadType], ReceivePayloadType]]
    _feature_preset_mode: bool
    _optimistic: bool
    _optimistic_preset_mode: bool
    _topic: dict[str, Any]
    _attr_fan_mode: Incomplete
    _attr_hvac_action: Incomplete
    _attr_hvac_mode: Incomplete
    _attr_is_aux_heat: Incomplete
    _attr_swing_mode: Incomplete
    _attr_target_temperature_low: Incomplete
    _attr_target_temperature_high: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_hvac_modes: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_min_humidity: Incomplete
    _attr_max_humidity: Incomplete
    _attr_precision: Incomplete
    _attr_fan_modes: Incomplete
    _attr_swing_modes: Incomplete
    _attr_target_temperature_step: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_target_temperature: Incomplete
    _attr_preset_modes: Incomplete
    _attr_preset_mode: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def _publish(self, topic: str, payload: PublishPayloadType) -> None: ...
    async def _set_climate_attribute(self, temp: Union[float, None], cmnd_topic: str, cmnd_template: str, state_topic: str, attr: str) -> bool: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_humidity(self, humidity: int) -> None: ...
    async def async_set_swing_mode(self, swing_mode: str) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def _set_aux_heat(self, state: bool) -> None: ...
    async def async_turn_aux_heat_on(self) -> None: ...
    async def async_turn_aux_heat_off(self) -> None: ...
