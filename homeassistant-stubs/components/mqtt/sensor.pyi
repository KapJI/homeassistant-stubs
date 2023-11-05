import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RO_SCHEMA as MQTT_RO_SCHEMA
from .const import CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_NONE as PAYLOAD_NONE
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttAvailability as MqttAvailability, MqttEntity as MqttEntity, async_setup_entity_entry_helper as async_setup_entity_entry_helper, validate_sensor_entity_category as validate_sensor_entity_category, write_state_on_attr_change as write_state_on_attr_change
from .models import MqttValueTemplate as MqttValueTemplate, PayloadSentinel as PayloadSentinel, ReceiveMessage as ReceiveMessage, ReceivePayloadType as ReceivePayloadType
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components import sensor as sensor
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, ENTITY_ID_FORMAT as ENTITY_ID_FORMAT, RestoreSensor as RestoreSensor, STATE_CLASSES_SCHEMA as STATE_CLASSES_SCHEMA, SensorDeviceClass as SensorDeviceClass, SensorExtraStoredData as SensorExtraStoredData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONF_EXPIRE_AFTER: str
CONF_LAST_RESET_TOPIC: str
CONF_LAST_RESET_VALUE_TEMPLATE: str
CONF_SUGGESTED_DISPLAY_PRECISION: str
MQTT_SENSOR_ATTRIBUTES_BLOCKED: Incomplete
DEFAULT_NAME: str
DEFAULT_FORCE_UPDATE: bool
_PLATFORM_SCHEMA_BASE: Incomplete
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MqttSensor(MqttEntity, RestoreSensor):
    _default_name = DEFAULT_NAME
    _entity_id_format = ENTITY_ID_FORMAT
    _attr_last_reset: datetime | None
    _attributes_extra_blocked = MQTT_SENSOR_ATTRIBUTES_BLOCKED
    _expiration_trigger: CALLBACK_TYPE | None
    _expire_after: int | None
    _expired: bool | None
    _template: Callable[[ReceivePayloadType, PayloadSentinel], ReceivePayloadType]
    _last_reset_template: Callable[[ReceivePayloadType], ReceivePayloadType]
    _attr_native_value: Incomplete
    async def mqtt_async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_device_class: Incomplete
    _attr_force_update: Incomplete
    _attr_suggested_display_precision: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    def _value_is_expired(self, *_: datetime) -> None: ...
    @property
    def available(self) -> bool: ...
