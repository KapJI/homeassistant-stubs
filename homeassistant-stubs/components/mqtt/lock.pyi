import re
import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_CODE_FORMAT as CONF_CODE_FORMAT, CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_PAYLOAD_LOCK as CONF_PAYLOAD_LOCK, CONF_PAYLOAD_OPEN as CONF_PAYLOAD_OPEN, CONF_PAYLOAD_RESET as CONF_PAYLOAD_RESET, CONF_PAYLOAD_UNLOCK as CONF_PAYLOAD_UNLOCK, CONF_STATE_JAMMED as CONF_STATE_JAMMED, CONF_STATE_LOCKED as CONF_STATE_LOCKED, CONF_STATE_LOCKING as CONF_STATE_LOCKING, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_STATE_UNLOCKED as CONF_STATE_UNLOCKED, CONF_STATE_UNLOCKING as CONF_STATE_UNLOCKING, DEFAULT_PAYLOAD_LOCK as DEFAULT_PAYLOAD_LOCK, DEFAULT_PAYLOAD_RESET as DEFAULT_PAYLOAD_RESET, DEFAULT_PAYLOAD_UNLOCK as DEFAULT_PAYLOAD_UNLOCK, DEFAULT_STATE_JAMMED as DEFAULT_STATE_JAMMED, DEFAULT_STATE_LOCKED as DEFAULT_STATE_LOCKED, DEFAULT_STATE_LOCKING as DEFAULT_STATE_LOCKING, DEFAULT_STATE_OPEN as DEFAULT_STATE_OPEN, DEFAULT_STATE_OPENING as DEFAULT_STATE_OPENING, DEFAULT_STATE_UNLOCKED as DEFAULT_STATE_UNLOCKED, DEFAULT_STATE_UNLOCKING as DEFAULT_STATE_UNLOCKING
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import lock as lock
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, TemplateVarsType as TemplateVarsType
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DEFAULT_NAME: str
MQTT_LOCK_ATTRIBUTES_BLOCKED: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete
STATE_CONFIG_KEYS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MqttLock(MqttEntity, LockEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_LOCK_ATTRIBUTES_BLOCKED
    _compiled_pattern: re.Pattern[Any] | None
    _optimistic: bool
    _valid_states: list[str]
    _command_template: Callable[[PublishPayloadType, TemplateVarsType], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_is_locked: bool
    _attr_assumed_state: Incomplete
    _attr_code_format: Incomplete
    _attr_supported_features: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_is_unlocking: Incomplete
    _attr_is_open: Incomplete
    _attr_is_jammed: Incomplete
    _attr_is_locking: Incomplete
    _attr_is_opening: Incomplete
    @callback
    def _message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
