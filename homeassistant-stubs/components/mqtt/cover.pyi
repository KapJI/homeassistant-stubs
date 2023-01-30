import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper, warn_for_legacy_schema as warn_for_legacy_schema
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import cover as cover
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, ATTR_TILT_POSITION as ATTR_TILT_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
CONF_GET_POSITION_TOPIC: str
CONF_GET_POSITION_TEMPLATE: str
CONF_SET_POSITION_TOPIC: str
CONF_SET_POSITION_TEMPLATE: str
CONF_TILT_COMMAND_TOPIC: str
CONF_TILT_COMMAND_TEMPLATE: str
CONF_TILT_STATUS_TOPIC: str
CONF_TILT_STATUS_TEMPLATE: str
CONF_PAYLOAD_CLOSE: str
CONF_PAYLOAD_OPEN: str
CONF_PAYLOAD_STOP: str
CONF_POSITION_CLOSED: str
CONF_POSITION_OPEN: str
CONF_STATE_CLOSED: str
CONF_STATE_CLOSING: str
CONF_STATE_OPEN: str
CONF_STATE_OPENING: str
CONF_STATE_STOPPED: str
CONF_TILT_CLOSED_POSITION: str
CONF_TILT_MAX: str
CONF_TILT_MIN: str
CONF_TILT_OPEN_POSITION: str
CONF_TILT_STATE_OPTIMISTIC: str
TILT_PAYLOAD: str
COVER_PAYLOAD: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_CLOSE: str
DEFAULT_PAYLOAD_OPEN: str
DEFAULT_PAYLOAD_STOP: str
DEFAULT_POSITION_CLOSED: int
DEFAULT_POSITION_OPEN: int
DEFAULT_RETAIN: bool
DEFAULT_STATE_STOPPED: str
DEFAULT_TILT_CLOSED_POSITION: int
DEFAULT_TILT_MAX: int
DEFAULT_TILT_MIN: int
DEFAULT_TILT_OPEN_POSITION: int
DEFAULT_TILT_OPTIMISTIC: bool
TILT_FEATURES: Incomplete
MQTT_COVER_ATTRIBUTES_BLOCKED: Incomplete

def validate_options(config: ConfigType) -> ConfigType: ...

_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
PLATFORM_SCHEMA: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None] = ...) -> None: ...

class MqttCover(MqttEntity, CoverEntity):
    _entity_id_format: str
    _attributes_extra_blocked: frozenset[str]
    _position: Incomplete
    _state: Incomplete
    _optimistic: Incomplete
    _tilt_value: Incomplete
    _tilt_optimistic: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _value_template: Incomplete
    _set_position_template: Incomplete
    _get_position_template: Incomplete
    _set_tilt_template: Incomplete
    _tilt_status_template: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
    @property
    def is_closed(self) -> Union[bool, None]: ...
    @property
    def is_opening(self) -> bool: ...
    @property
    def is_closing(self) -> bool: ...
    @property
    def current_cover_position(self) -> Union[int, None]: ...
    @property
    def current_cover_tilt_position(self) -> Union[int, None]: ...
    @property
    def device_class(self) -> Union[CoverDeviceClass, None]: ...
    @property
    def supported_features(self) -> CoverEntityFeature: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    async def async_open_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_close_cover_tilt(self, **kwargs: Any) -> None: ...
    async def async_set_cover_tilt_position(self, **kwargs: Any) -> None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_toggle_tilt(self, **kwargs: Any) -> None: ...
    def is_tilt_closed(self) -> bool: ...
    def find_percentage_in_range(self, position: float, range_type: str = ...) -> int: ...
    def find_in_range_from_percent(self, percentage: float, range_type: str = ...) -> int: ...
    def tilt_payload_received(self, _payload: Any) -> None: ...
