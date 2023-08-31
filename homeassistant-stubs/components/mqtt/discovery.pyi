from .. import mqtt as mqtt
from .abbreviations import ABBREVIATIONS as ABBREVIATIONS, DEVICE_ABBREVIATIONS as DEVICE_ABBREVIATIONS, ORIGIN_ABBREVIATIONS as ORIGIN_ABBREVIATIONS
from .const import ATTR_DISCOVERY_HASH as ATTR_DISCOVERY_HASH, ATTR_DISCOVERY_PAYLOAD as ATTR_DISCOVERY_PAYLOAD, ATTR_DISCOVERY_TOPIC as ATTR_DISCOVERY_TOPIC, CONF_AVAILABILITY as CONF_AVAILABILITY, CONF_ORIGIN as CONF_ORIGIN, CONF_SUPPORT_URL as CONF_SUPPORT_URL, CONF_SW_VERSION as CONF_SW_VERSION, CONF_TOPIC as CONF_TOPIC, DOMAIN as DOMAIN
from .models import MqttOriginInfo as MqttOriginInfo, ReceiveMessage as ReceiveMessage
from .util import get_mqtt_data as get_mqtt_data
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE as CONF_DEVICE, CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service_info.mqtt import MqttServiceInfo as MqttServiceInfo
from homeassistant.helpers.typing import DiscoveryInfoType as DiscoveryInfoType
from homeassistant.loader import async_get_mqtt as async_get_mqtt
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

_LOGGER: Incomplete
TOPIC_MATCHER: Incomplete
SUPPORTED_COMPONENTS: Incomplete
MQTT_DISCOVERY_UPDATED: str
MQTT_DISCOVERY_NEW: str
MQTT_DISCOVERY_DONE: str
TOPIC_BASE: str
MQTT_ORIGIN_INFO_SCHEMA: Incomplete

class MQTTDiscoveryPayload(dict[str, Any]):
    discovery_data: DiscoveryInfoType

def clear_discovery_hash(hass: HomeAssistant, discovery_hash: tuple[str, str]) -> None: ...
def set_discovery_hash(hass: HomeAssistant, discovery_hash: tuple[str, str]) -> None: ...
def async_log_discovery_origin_info(message: str, discovery_payload: MQTTDiscoveryPayload) -> None: ...
async def async_start(hass: HomeAssistant, discovery_topic: str, config_entry: ConfigEntry) -> None: ...
async def async_stop(hass: HomeAssistant) -> None: ...
