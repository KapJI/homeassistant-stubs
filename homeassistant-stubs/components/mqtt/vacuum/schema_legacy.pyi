import voluptuous as vol
from .. import subscription as subscription
from ..config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from ..const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN
from ..debug_info import log_messages as log_messages
from ..mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, write_state_on_attr_change as write_state_on_attr_change
from ..models import MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from ..util import valid_publish_topic as valid_publish_topic
from .const import MQTT_VACUUM_ATTRIBUTES_BLOCKED as MQTT_VACUUM_ATTRIBUTES_BLOCKED
from .schema import MQTT_VACUUM_SCHEMA as MQTT_VACUUM_SCHEMA, services_to_strings as services_to_strings, strings_to_services as strings_to_services
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.vacuum import ATTR_STATUS as ATTR_STATUS, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, VacuumEntity as VacuumEntity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.const import ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_NAME as CONF_NAME
from homeassistant.core import callback as callback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

SERVICE_TO_STRING: Incomplete
STRING_TO_SERVICE: Incomplete
DEFAULT_SERVICES: Incomplete
ALL_SERVICES: Incomplete
CONF_SUPPORTED_FEATURES = ATTR_SUPPORTED_FEATURES
CONF_BATTERY_LEVEL_TEMPLATE: str
CONF_BATTERY_LEVEL_TOPIC: str
CONF_CHARGING_TEMPLATE: str
CONF_CHARGING_TOPIC: str
CONF_CLEANING_TEMPLATE: str
CONF_CLEANING_TOPIC: str
CONF_DOCKED_TEMPLATE: str
CONF_DOCKED_TOPIC: str
CONF_ERROR_TEMPLATE: str
CONF_ERROR_TOPIC: str
CONF_FAN_SPEED_LIST: str
CONF_FAN_SPEED_TEMPLATE: str
CONF_FAN_SPEED_TOPIC: str
CONF_PAYLOAD_CLEAN_SPOT: str
CONF_PAYLOAD_LOCATE: str
CONF_PAYLOAD_RETURN_TO_BASE: str
CONF_PAYLOAD_START_PAUSE: str
CONF_PAYLOAD_STOP: str
CONF_PAYLOAD_TURN_OFF: str
CONF_PAYLOAD_TURN_ON: str
CONF_SEND_COMMAND_TOPIC: str
CONF_SET_FAN_SPEED_TOPIC: str
DEFAULT_NAME: str
DEFAULT_PAYLOAD_CLEAN_SPOT: str
DEFAULT_PAYLOAD_LOCATE: str
DEFAULT_PAYLOAD_RETURN_TO_BASE: str
DEFAULT_PAYLOAD_START_PAUSE: str
DEFAULT_PAYLOAD_STOP: str
DEFAULT_PAYLOAD_TURN_OFF: str
DEFAULT_PAYLOAD_TURN_ON: str
DEFAULT_RETAIN: bool
DEFAULT_SERVICE_STRINGS: Incomplete
MQTT_LEGACY_VACUUM_ATTRIBUTES_BLOCKED: Incomplete
PLATFORM_SCHEMA_LEGACY_MODERN: Incomplete
DISCOVERY_SCHEMA_LEGACY: Incomplete
_COMMANDS: Incomplete

class MqttVacuum(MqttEntity, VacuumEntity):
    _attr_battery_level: int
    _attr_is_on: bool
    _attributes_extra_blocked = MQTT_LEGACY_VACUUM_ATTRIBUTES_BLOCKED
    _charging: bool
    _cleaning: bool
    _command_topic: str | None
    _docked: bool
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _encoding: str | None
    _error: str | None
    _qos: bool
    _retain: bool
    _payloads: dict[str, str]
    _send_command_topic: str | None
    _set_fan_speed_topic: str | None
    _state_topics: dict[str, str | None]
    _templates: dict[str, Callable[[ReceivePayloadType, PayloadSentinel], ReceivePayloadType]]
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_supported_features: Incomplete
    _attr_fan_speed_list: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_status: str
    _attr_fan_speed: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    @property
    def battery_icon(self) -> str: ...
    async def _async_publish_command(self, feature: VacuumEntityFeature) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_clean_spot(self, **kwargs: Any) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_start_pause(self, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = ..., **kwargs: Any) -> None: ...
