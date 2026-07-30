from . import subscription as subscription
from .config import MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_RETAIN as CONF_RETAIN, CONF_SCHEMA as CONF_SCHEMA, CONF_STATE_TOPIC as CONF_STATE_TOPIC, DEFAULT_RETAIN as DEFAULT_RETAIN, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import infrared as infrared
from homeassistant.components.infrared import InfraredCommand as InfraredCommand, InfraredEmitterEntity as InfraredEmitterEntity, InfraredReceivedSignal as InfraredReceivedSignal, InfraredReceiverEntity as InfraredReceiverEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads_object as json_loads_object
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
DEFAULT_EMITTER_NAME: str
DEFAULT_RECEIVER_NAME: str
MQTT_INFRARED_ATTRIBUTES_BLOCKED: frozenset[str]
SIGNAL_SCHEMA: Incomplete

def validate_mqtt_infrared_config(config_value: dict[str, Any]) -> ConfigType: ...
def validate_mqtt_infrared_discovery(config_value: dict[str, Any]) -> ConfigType: ...

INFRARED_BASE_SCHEMA: Incomplete
EMITTER_SCHEMA: Incomplete
RECEIVER_SCHEMA: Incomplete
DISCOVERY_SCHEMA_MAPPING: dict[str, VolSchemaType]
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MqttInfraredEmitterEntity(MqttEntity, InfraredEmitterEntity):
    _attributes_extra_blocked = MQTT_INFRARED_ATTRIBUTES_BLOCKED
    _default_name = DEFAULT_EMITTER_NAME
    _entity_id_format: Incomplete
    _command_template: Callable[[PublishPayloadType, dict[str, Any]], PublishPayloadType]
    @staticmethod
    @override
    def config_schema() -> VolSchemaType: ...
    @override
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    @override
    def _prepare_subscribe_topics(self) -> None: ...
    @override
    async def _subscribe_topics(self) -> None: ...
    @override
    async def async_send_command(self, command: InfraredCommand) -> None: ...

class MqttInfraredReceiverEntity(MqttEntity, InfraredReceiverEntity):
    _attributes_extra_blocked = MQTT_INFRARED_ATTRIBUTES_BLOCKED
    _default_name = DEFAULT_RECEIVER_NAME
    _entity_id_format: Incomplete
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    @override
    def config_schema() -> VolSchemaType: ...
    @override
    def _setup_from_config(self, config: ConfigType) -> None: ...
    @callback
    def _handle_state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    @override
    def _prepare_subscribe_topics(self) -> None: ...
    @override
    async def _subscribe_topics(self) -> None: ...
