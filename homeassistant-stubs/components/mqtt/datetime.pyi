import datetime as datetime_library
from . import subscription as subscription
from .config import MQTT_RW_SCHEMA as MQTT_RW_SCHEMA
from .const import CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_NONE as PAYLOAD_NONE
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, PublishPayloadType as PublishPayloadType, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components import datetime as datetime
from homeassistant.components.datetime import DateTimeEntity as DateTimeEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_OPTIMISTIC as CONF_OPTIMISTIC, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.service_info.mqtt import ReceivePayloadType as ReceivePayloadType
from homeassistant.helpers.typing import ConfigType as ConfigType, VolSchemaType as VolSchemaType
from homeassistant.util.dt import async_get_time_zone as async_get_time_zone
from typing import Any
from zoneinfo import ZoneInfo

_LOGGER: Incomplete
CONF_TIMEZONE: str
PARALLEL_UPDATES: int
DEFAULT_NAME: str
MQTT_DATETIME_ATTRIBUTES_BLOCKED: frozenset[str]
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MqttDateTime(MqttEntity, DateTimeEntity):
    _attr_native_value: datetime_library.datetime | None
    _attributes_extra_blocked = MQTT_DATETIME_ATTRIBUTES_BLOCKED
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _zone_info: ZoneInfo | None
    _time_zone_delta: datetime_library.timedelta | None
    _optimistic: bool
    _command_template: Callable[[PublishPayloadType, dict[str, Any]], PublishPayloadType]
    _value_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    @staticmethod
    def config_schema() -> VolSchemaType: ...
    _timezone_config: Incomplete
    _attr_assumed_state: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    async def _async_finish_update_config(self) -> None: ...
    @callback
    def _handle_state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_set_value(self, value: datetime_library.datetime) -> None: ...
