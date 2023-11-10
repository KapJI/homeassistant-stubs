import asyncio
import datetime as dt
import voluptuous as vol
from .client import MQTT as MQTT, Subscription as Subscription
from .debug_info import TimestampedPublishMessage as TimestampedPublishMessage
from .device_trigger import Trigger as Trigger
from .discovery import MQTTDiscoveryPayload as MQTTDiscoveryPayload
from .tag import MQTTTagScanner as MQTTTagScanner
from _typeshed import Incomplete
from collections import deque
from collections.abc import Callable, Coroutine
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import template as template
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, TemplateVarsType as TemplateVarsType
from paho.mqtt.client import MQTTMessage as MQTTMessage
from typing import Any, TypedDict

class PayloadSentinel(StrEnum):
    NONE: str
    DEFAULT: str

_LOGGER: Incomplete
ATTR_THIS: str
PublishPayloadType: Incomplete

@dataclass
class PublishMessage:
    topic: str
    payload: PublishPayloadType
    qos: int
    retain: bool
    def __init__(self, topic, payload, qos, retain) -> None: ...

@dataclass
class ReceiveMessage:
    topic: str
    payload: ReceivePayloadType
    qos: int
    retain: bool
    subscribed_topic: str
    timestamp: dt.datetime
    def __init__(self, topic, payload, qos, retain, subscribed_topic, timestamp) -> None: ...
AsyncMessageCallbackType = Callable[[ReceiveMessage], Coroutine[Any, Any, None]]
MessageCallbackType = Callable[[ReceiveMessage], None]

class SubscriptionDebugInfo(TypedDict):
    messages: deque[ReceiveMessage]
    count: int

class EntityDebugInfo(TypedDict):
    subscriptions: dict[str, SubscriptionDebugInfo]
    discovery_data: DiscoveryInfoType
    transmitted: dict[str, dict[str, deque[TimestampedPublishMessage]]]

class TriggerDebugInfo(TypedDict):
    device_id: str
    discovery_data: DiscoveryInfoType

class PendingDiscovered(TypedDict):
    pending: deque[MQTTDiscoveryPayload]
    unsub: CALLBACK_TYPE

class MqttOriginInfo(TypedDict, total=False):
    name: str
    manufacturer: str
    sw_version: str
    hw_version: str
    support_url: str

class MqttCommandTemplate:
    _template_state: Incomplete
    _command_template: Incomplete
    _entity: Incomplete
    def __init__(self, command_template: template.Template | None, *, hass: HomeAssistant | None = ..., entity: Entity | None = ...) -> None: ...
    def async_render(self, value: PublishPayloadType = ..., variables: TemplateVarsType = ...) -> PublishPayloadType: ...

class MqttValueTemplate:
    _template_state: Incomplete
    _value_template: Incomplete
    _config_attributes: Incomplete
    _entity: Incomplete
    def __init__(self, value_template: template.Template | None, *, hass: HomeAssistant | None = ..., entity: Entity | None = ..., config_attributes: TemplateVarsType = ...) -> None: ...
    def async_render_with_possible_json_value(self, payload: ReceivePayloadType, default: ReceivePayloadType | PayloadSentinel = ..., variables: TemplateVarsType = ...) -> ReceivePayloadType: ...

class EntityTopicState:
    subscribe_calls: Incomplete
    def __init__(self) -> None: ...
    def process_write_state_requests(self, msg: MQTTMessage) -> None: ...
    def write_state_request(self, entity: Entity) -> None: ...

@dataclass
class MqttData:
    client: MQTT
    config: list[ConfigType]
    debug_info_entities: dict[str, EntityDebugInfo] = ...
    debug_info_triggers: dict[tuple[str, str], TriggerDebugInfo] = ...
    device_triggers: dict[str, Trigger] = ...
    data_config_flow_lock: asyncio.Lock = ...
    discovery_already_discovered: set[tuple[str, str]] = ...
    discovery_pending_discovered: dict[tuple[str, str], PendingDiscovered] = ...
    discovery_registry_hooks: dict[tuple[str, str], CALLBACK_TYPE] = ...
    discovery_unsubscribe: list[CALLBACK_TYPE] = ...
    integration_unsubscribe: dict[str, CALLBACK_TYPE] = ...
    issues: dict[str, set[str]] = ...
    last_discovery: float = ...
    reload_dispatchers: list[CALLBACK_TYPE] = ...
    reload_handlers: dict[str, CALLBACK_TYPE] = ...
    reload_schema: dict[str, vol.Schema] = ...
    state_write_requests: EntityTopicState = ...
    subscriptions_to_restore: list[Subscription] = ...
    tags: dict[str, dict[str, MQTTTagScanner]] = ...
    def __init__(self, client, config, debug_info_entities, debug_info_triggers, device_triggers, data_config_flow_lock, discovery_already_discovered, discovery_pending_discovered, discovery_registry_hooks, discovery_unsubscribe, integration_unsubscribe, issues, last_discovery, reload_dispatchers, reload_handlers, reload_schema, state_write_requests, subscriptions_to_restore, tags) -> None: ...
