import voluptuous as vol
from . import subscription as subscription
from .config import MQTT_RO_SCHEMA as MQTT_RO_SCHEMA
from .const import CONF_ENCODING as CONF_ENCODING, CONF_QOS as CONF_QOS, CONF_STATE_TOPIC as CONF_STATE_TOPIC, PAYLOAD_NONE as PAYLOAD_NONE
from .debug_info import log_messages as log_messages
from .mixins import MQTT_ENTITY_COMMON_SCHEMA as MQTT_ENTITY_COMMON_SCHEMA, MqttAvailability as MqttAvailability, MqttEntity as MqttEntity, async_setup_entry_helper as async_setup_entry_helper, write_state_on_attr_change as write_state_on_attr_change
from .models import MqttValueTemplate as MqttValueTemplate, ReceiveMessage as ReceiveMessage
from _typeshed import Incomplete
from homeassistant.components import binary_sensor as binary_sensor
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_FORCE_UPDATE as CONF_FORCE_UPDATE, CONF_NAME as CONF_NAME, CONF_PAYLOAD_OFF as CONF_PAYLOAD_OFF, CONF_PAYLOAD_ON as CONF_PAYLOAD_ON, CONF_VALUE_TEMPLATE as CONF_VALUE_TEMPLATE, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
DEFAULT_NAME: str
CONF_OFF_DELAY: str
DEFAULT_PAYLOAD_OFF: str
DEFAULT_PAYLOAD_ON: str
DEFAULT_FORCE_UPDATE: bool
CONF_EXPIRE_AFTER: str
PLATFORM_SCHEMA_MODERN: Incomplete
DISCOVERY_SCHEMA: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def _async_setup_entity(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, config: ConfigType, config_entry: ConfigEntry, discovery_data: DiscoveryInfoType | None = ...) -> None: ...

class MqttBinarySensor(MqttEntity, BinarySensorEntity, RestoreEntity):
    _default_name = DEFAULT_NAME
    _delay_listener: CALLBACK_TYPE | None
    _entity_id_format: Incomplete
    _expired: bool | None
    _expire_after: int | None
    _expiration_trigger: CALLBACK_TYPE | None
    _attr_is_on: Incomplete
    async def mqtt_async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @staticmethod
    def config_schema() -> vol.Schema: ...
    _attr_force_update: Incomplete
    _attr_device_class: Incomplete
    _value_template: Incomplete
    def _setup_from_config(self, config: ConfigType) -> None: ...
    _sub_state: Incomplete
    def _prepare_subscribe_topics(self) -> None: ...
    async def _subscribe_topics(self) -> None: ...
    def _value_is_expired(self, *_: Any) -> None: ...
    @property
    def available(self) -> bool: ...
