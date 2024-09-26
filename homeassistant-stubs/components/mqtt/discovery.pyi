from .abbreviations import ABBREVIATIONS as ABBREVIATIONS, DEVICE_ABBREVIATIONS as DEVICE_ABBREVIATIONS, ORIGIN_ABBREVIATIONS as ORIGIN_ABBREVIATIONS
from .client import async_subscribe_internal as async_subscribe_internal
from .const import ATTR_DISCOVERY_HASH as ATTR_DISCOVERY_HASH, ATTR_DISCOVERY_PAYLOAD as ATTR_DISCOVERY_PAYLOAD, ATTR_DISCOVERY_TOPIC as ATTR_DISCOVERY_TOPIC, CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_ORIGIN as CONF_ORIGIN, CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN, SUPPORTED_COMPONENTS as SUPPORTED_COMPONENTS
from .models import DATA_MQTT as DATA_MQTT, MqttOriginInfo as MqttOriginInfo, ReceiveMessage as ReceiveMessage
from .schemas import MQTT_ORIGIN_INFO_SCHEMA as MQTT_ORIGIN_INFO_SCHEMA
from .util import async_forward_entry_setup_and_setup_discovery as async_forward_entry_setup_and_setup_discovery
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HassJobType as HassJobType, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service_info.mqtt import MqttServiceInfo as MqttServiceInfo
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.loader import async_get_mqtt as async_get_mqtt
from homeassistant.util.json import json_loads_object as json_loads_object
from homeassistant.util.signal_type import SignalTypeFormat as SignalTypeFormat
from typing import Any

ABBREVIATIONS_SET: Incomplete
DEVICE_ABBREVIATIONS_SET: Incomplete
ORIGIN_ABBREVIATIONS_SET: Incomplete
_LOGGER: Incomplete
TOPIC_MATCHER: Incomplete
MQTT_DISCOVERY_UPDATED: SignalTypeFormat[MQTTDiscoveryPayload]
MQTT_DISCOVERY_NEW: SignalTypeFormat[MQTTDiscoveryPayload]
MQTT_DISCOVERY_DONE: SignalTypeFormat[Any]
TOPIC_BASE: str

class MQTTDiscoveryPayload(dict[str, Any]):
    discovery_data: DiscoveryInfoType

def clear_discovery_hash(hass: HomeAssistant, discovery_hash: tuple[str, str]) -> None: ...
def set_discovery_hash(hass: HomeAssistant, discovery_hash: tuple[str, str]) -> None: ...
def async_log_discovery_origin_info(message: str, discovery_payload: MQTTDiscoveryPayload, level: int = ...) -> None: ...
def _replace_abbreviations(payload: Any | dict[str, Any], abbreviations: dict[str, str], abbreviations_set: set[str]) -> None: ...
def _replace_all_abbreviations(discovery_payload: Any | dict[str, Any]) -> None: ...
def _replace_topic_base(discovery_payload: dict[str, Any]) -> None: ...
def _valid_origin_info(discovery_payload: MQTTDiscoveryPayload) -> bool: ...
async def async_start(hass: HomeAssistant, discovery_topic: str, config_entry: ConfigEntry) -> None: ...
async def async_stop(hass: HomeAssistant) -> None: ...
