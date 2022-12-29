import voluptuous as vol
from .. import subscription as subscription
from ..config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from ..const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC
from ..debug_info import log_messages as log_messages
from ..mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, warn_for_legacy_schema as warn_for_legacy_schema
from ..models import ReceiveMessage as ReceiveMessage
from ..util import get_mqtt_data as get_mqtt_data, valid_publish_topic as valid_publish_topic
from .const import MQTT_VACUUM_ATTRIBUTES_BLOCKED as MQTT_VACUUM_ATTRIBUTES_BLOCKED
from .schema import MQTT_VACUUM_SCHEMA as MQTT_VACUUM_SCHEMA, services_to_strings as services_to_strings, strings_to_services as strings_to_services
from _typeshed import Incomplete
from homeassistant.components.vacuum import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING, StateVacuumEntity as StateVacuumEntity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_NAME as CONF_NAME, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.json import json_dumps as json_dumps, json_loads as json_loads
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

SERVICE_TO_STRING: dict[VacuumEntityFeature, str]
STRING_TO_SERVICE: Incomplete
DEFAULT_SERVICES: Incomplete
ALL_SERVICES: Incomplete
BATTERY: str
FAN_SPEED: str
STATE: str
POSSIBLE_STATES: dict[str, str]
CONF_SUPPORTED_FEATURES = ATTR_SUPPORTED_FEATURES
CONF_PAYLOAD_TURN_ON: str
CONF_PAYLOAD_TURN_OFF: str
CONF_PAYLOAD_RETURN_TO_BASE: str
CONF_PAYLOAD_STOP: str
CONF_PAYLOAD_CLEAN_SPOT: str
CONF_PAYLOAD_LOCATE: str
CONF_PAYLOAD_START: str
CONF_PAYLOAD_PAUSE: str
CONF_SET_FAN_SPEED_TOPIC: str
CONF_FAN_SPEED_LIST: str
CONF_SEND_COMMAND_TOPIC: str
DEFAULT_NAME: str
DEFAULT_RETAIN: bool
DEFAULT_SERVICE_STRINGS: Incomplete
DEFAULT_PAYLOAD_RETURN_TO_BASE: str
DEFAULT_PAYLOAD_STOP: str
DEFAULT_PAYLOAD_CLEAN_SPOT: str
DEFAULT_PAYLOAD_LOCATE: str
DEFAULT_PAYLOAD_START: str
DEFAULT_PAYLOAD_PAUSE: str
_FEATURE_PAYLOADS: Incomplete
PLATFORM_SCHEMA_STATE_MODERN: Incomplete
PLATFORM_SCHEMA_STATE: Incomplete
DISCOVERY_SCHEMA_STATE: Incomplete

async def async_setup_entity_state(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...

class MqttStateVacuum(MqttEntity, StateVacuumEntity):
    _entity_id_format: Incomplete
    _attributes_extra_blocked: Incomplete
    _command_topic: Union[str, None]
    _set_fan_speed_topic: Union[str, None]
    _send_command_topic: Union[str, None]
    _payloads: dict[str, Union[str, None]]
    _state_attrs: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: Union[DiscoveryInfoType, None]) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_supported_features: Incomplete
    _attr_fan_speed_list: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_fan_speed: Incomplete
    _attr_battery_level: Incomplete
    def _update_state_attributes(self, payload: dict[str, Any]) -> None: ...
    _attr_state: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def _async_publish_command(self, feature: VacuumEntityFeature) -> None: ...
    async def async_start(self) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: Union[dict[str, Any], list[Any], None] = ..., **kwargs: Any) -> None: ...
