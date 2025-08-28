import voluptuous as vol
from . import subscription as subscription
from .config import DEFAULT_RETAIN as DEFAULT_RETAIN, MQTT_BASE_SCHEMA as MQTT_BASE_SCHEMA
from .const import ALARM_CONTROL_PANEL_SUPPORTED_FEATURES as ALARM_CONTROL_PANEL_SUPPORTED_FEATURES, CONF_CODE_ARM_REQUIRED as CONF_CODE_ARM_REQUIRED, CONF_CODE_DISARM_REQUIRED as CONF_CODE_DISARM_REQUIRED, CONF_CODE_TRIGGER_REQUIRED as CONF_CODE_TRIGGER_REQUIRED, CONF_COMMAND_TEMPLATE as CONF_COMMAND_TEMPLATE, CONF_COMMAND_TOPIC as CONF_COMMAND_TOPIC, CONF_PAYLOAD_ARM_AWAY as CONF_PAYLOAD_ARM_AWAY, CONF_PAYLOAD_ARM_CUSTOM_BYPASS as CONF_PAYLOAD_ARM_CUSTOM_BYPASS, CONF_PAYLOAD_ARM_HOME as CONF_PAYLOAD_ARM_HOME, CONF_PAYLOAD_ARM_NIGHT as CONF_PAYLOAD_ARM_NIGHT, CONF_PAYLOAD_ARM_VACATION as CONF_PAYLOAD_ARM_VACATION, CONF_PAYLOAD_DISARM as CONF_PAYLOAD_DISARM, CONF_PAYLOAD_TRIGGER as CONF_PAYLOAD_TRIGGER, CONF_RETAIN as CONF_RETAIN, CONF_STATE_TOPIC as CONF_STATE_TOPIC, CONF_SUPPORTED_FEATURES as CONF_SUPPORTED_FEATURES, DEFAULT_ALARM_CONTROL_PANEL_COMMAND_TEMPLATE as DEFAULT_ALARM_CONTROL_PANEL_COMMAND_TEMPLATE, DEFAULT_PAYLOAD_ARM_AWAY as DEFAULT_PAYLOAD_ARM_AWAY, DEFAULT_PAYLOAD_ARM_CUSTOM_BYPASS as DEFAULT_PAYLOAD_ARM_CUSTOM_BYPASS, DEFAULT_PAYLOAD_ARM_HOME as DEFAULT_PAYLOAD_ARM_HOME, DEFAULT_PAYLOAD_ARM_NIGHT as DEFAULT_PAYLOAD_ARM_NIGHT, DEFAULT_PAYLOAD_ARM_VACATION as DEFAULT_PAYLOAD_ARM_VACATION, DEFAULT_PAYLOAD_DISARM as DEFAULT_PAYLOAD_DISARM, DEFAULT_PAYLOAD_TRIGGER as DEFAULT_PAYLOAD_TRIGGER, PAYLOAD_NONE as PAYLOAD_NONE, REMOTE_CODE as REMOTE_CODE, REMOTE_CODE_TEXT as REMOTE_CODE_TEXT
from .entity import MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper
from .models import MqttCommandTemplate as MqttCommandTemplate, MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA
from .util import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from _typeshed import Incomplete
from homeassistant.components import alarm_control_panel as alarm
from homeassistant.components.alarm_control_panel import AlarmControlPanelState as AlarmControlPanelState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CODE as CONF_CODE, CONF_NAME as CONF_NAME, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
PARALLEL_UPDATES: int
MQTT_ALARM_ATTRIBUTES_BLOCKED: Incomplete
DEFAULT_NAME: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MqttAlarm(MqttEntity, alarm.AlarmControlPanelEntity):
    _default_name = DEFAULT_NAME
    _entity_id_format: Incomplete
    _attributes_extra_blocked = MQTT_ALARM_ATTRIBUTES_BLOCKED
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _value_template: Incomplete
    _command_template: Incomplete
    _attr_code_format: Incomplete
    _attr_code_arm_required: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _attr_alarm_state: Incomplete
    def _state_message_received(self, msg: ReceiveMessage) -> None: ...
    @callback
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    async def async_alarm_trigger(self, code: str | None = None) -> None: ...
    async def _publish(self, code: str | None, action: str) -> None: ...
    def _validate_code(self, code: str | None, state: str) -> bool: ...
