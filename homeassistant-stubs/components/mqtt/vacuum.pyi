from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN, CONF_SCHEMA as CONF_SCHEMA, CONF_STATE_TOPIC as CONF_STATE_TOPIC, DOMAIN as DOMAIN
from .mixins import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import vacuum as vacuum
from homeassistant.components.vacuum import ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, STATE_CLEANING as STATE_CLEANING, STATE_DOCKED as STATE_DOCKED, STATE_ERROR as STATE_ERROR, STATE_RETURNING as STATE_RETURNING, StateVacuumEntity as StateVacuumEntity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_NAME as CONF_NAME, STATE_IDLE as STATE_IDLE, STATE_PAUSED as STATE_PAUSED
from homeassistant.core import HomeAssistant as HomeAssistant, async_get_hass as async_get_hass, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, VolSchemaType as VolSchemaType
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

LEGACY: str
STATE: str
BATTERY: str
FAN_SPEED: str
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
DEFAULT_PAYLOAD_RETURN_TO_BASE: str
DEFAULT_PAYLOAD_STOP: str
DEFAULT_PAYLOAD_CLEAN_SPOT: str
DEFAULT_PAYLOAD_LOCATE: str
DEFAULT_PAYLOAD_START: str
DEFAULT_PAYLOAD_PAUSE: str
_LOGGER: Incomplete
SERVICE_TO_STRING: dict[VacuumEntityFeature, str]
STRING_TO_SERVICE: Incomplete
DEFAULT_SERVICES: Incomplete
ALL_SERVICES: Incomplete

def services_to_strings(services: VacuumEntityFeature, service_to_string: dict[VacuumEntityFeature, str]) -> list[str]: ...

DEFAULT_SERVICE_STRINGS: Incomplete
_FEATURE_PAYLOADS: Incomplete
MQTT_VACUUM_ATTRIBUTES_BLOCKED: Incomplete
MQTT_VACUUM_DOCS_URL: str

def _fail_legacy_config(discovery: bool) -> Callable[[ConfigType], ConfigType]: ...

VACUUM_BASE_SCHEMA: Incomplete
DISCOVERY_SCHEMA: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttStateVacuum(MqttEntity, StateVacuumEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_VACUUM_ATTRIBUTES_BLOCKED
    _command_topic: str | None
    _set_fan_speed_topic: str | None
    _send_command_topic: str | None
    _payloads: dict[str, str | None]
    _state_attrs: Incomplete
    def __init__(self, hass: HomeAssistant, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None) -> None: ...
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _attr_supported_features: Incomplete
    _attr_fan_speed_list: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_fan_speed: Incomplete
    _attr_battery_level: Incomplete
    def _update_state_attributes(self, payload: dict[str, Any]) -> None: ...
    _attr_state: Incomplete
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
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
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
