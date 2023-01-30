import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_VALUE_TEMPLATE as CONF_STATE_VALUE_TEMPLATE, PAYLOAD_EMPTY_JSON as PAYLOAD_EMPTY_JSON, PAYLOAD_NONE as PAYLOAD_NONE
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper, warn_for_legacy_schema as warn_for_legacy_schema
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import get_mqtt_data as get_mqtt_data
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import siren as siren
from homeassistant.components.siren import ATTR_AVAILABLE_TONES as ATTR_AVAILABLE_TONES, ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, SirenEntity as SirenEntity, SirenEntityFeature as SirenEntityFeature, SirenTurnOnServiceParameters as SirenTurnOnServiceParameters, TURN_ON_SCHEMA as TURN_ON_SCHEMA, process_turn_on_params as process_turn_on_params
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_dumps as json_dumps, json_loads as json_loads
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, TemplateVarsType as TemplateVarsType
from typing import Any

DEFAULT_NAME: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_PAYLOAD_OFF: str
ENTITY_ID_FORMAT: Incomplete
CONF_AVAILABLE_TONES: str
CONF_COMMAND_OFF_TEMPLATE: str
CONF_STATE_ON: str
CONF_STATE_OFF: str
CONF_SUPPORT_DURATION: str
CONF_SUPPORT_VOLUME_SET: str
STATE: str
PLATFORM_SCHEMA_MODERN: Incomplete
PLATFORM_SCHEMA: Incomplete
DISCOVERY_SCHEMA: Incomplete
MQTT_SIREN_ATTRIBUTES_BLOCKED: Incomplete
SUPPORTED_BASE: Incomplete
SUPPORTED_ATTRIBUTES: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None] = ...) -> None: ...

class MqttSiren(MqttEntity, SirenEntity):
    _entity_id_format: Incomplete
    _attributes_extra_blocked: Incomplete
    _command_templates: dict[str, Union[Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType], None]]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    _state_on: str
    _state_off: str
    _optimistic: bool
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_extra_state_attributes: Incomplete
    _attr_available_tones: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_on: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def _async_publish(self, topic: str, template: str, value: Any, variables: Union[dict[str, Any], None] = ...) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update(self, data: SirenTurnOnServiceParameters) -> None: ...
