import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_RETAIN as CONF_RETAIN, DEFAULT_OPTIMISTIC as DEFAULT_OPTIMISTIC, DEFAULT_RETAIN as DEFAULT_RETAIN
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper, write_state_on_attr_change as write_state_on_attr_change
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import lawn_mower as lawn_mower
from homeassistant.components.lawn_mower import LawnMowerActivity as LawnMowerActivity, LawnMowerEntity as LawnMowerEntity, LawnMowerEntityFeature as LawnMowerEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONF_ACTIVITY_STATE_TOPIC: str
CONF_ACTIVITY_VALUE_TEMPLATE: str
CONF_DOCK_COMMAND_TOPIC: str
CONF_DOCK_COMMAND_TEMPLATE: str
CONF_PAUSE_COMMAND_TOPIC: str
CONF_PAUSE_COMMAND_TEMPLATE: str
CONF_START_MOWING_COMMAND_TOPIC: str
CONF_START_MOWING_COMMAND_TEMPLATE: str
DEFAULT_NAME: str
ENTITY_ID_FORMAT: Incomplete
MQTT_LAWN_MOWER_ATTRIBUTES_BLOCKED: frozenset[str]
FEATURE_DOCK: str
FEATURE_PAUSE: str
FEATURE_START_MOWING: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttLawnMower(MqttEntity, LawnMowerEntity, RestoreEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attributes_extra_blocked = MQTT_LAWN_MOWER_ATTRIBUTES_BLOCKED
    _command_templates: dict[str, Callable[[PublishPayloadType], PublishPayloadType]]
    _command_topics: dict[str, str]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_assumed_state: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_activity: Incomplete
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def _async_operate(self, option: str, activity: LawnMowerActivity) -> None: ...
    async def async_start_mowing(self) -> None: ...
    async def async_dock(self) -> None: ...
    async def async_pause(self) -> None: ...
