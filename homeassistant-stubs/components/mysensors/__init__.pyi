from .const import ATTR_DEVICES as ATTR_DEVICES, CONF_BAUD_RATE as CONF_BAUD_RATE, CONF_DEVICE as CONF_DEVICE, CONF_GATEWAYS as CONF_GATEWAYS, CONF_NODES as CONF_NODES, CONF_PERSISTENCE as CONF_PERSISTENCE, CONF_PERSISTENCE_FILE as CONF_PERSISTENCE_FILE, CONF_RETAIN as CONF_RETAIN, CONF_TCP_PORT as CONF_TCP_PORT, CONF_TOPIC_IN_PREFIX as CONF_TOPIC_IN_PREFIX, CONF_TOPIC_OUT_PREFIX as CONF_TOPIC_OUT_PREFIX, CONF_VERSION as CONF_VERSION, DOMAIN as DOMAIN, DevId as DevId, DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY, MYSENSORS_GATEWAYS as MYSENSORS_GATEWAYS, MYSENSORS_ON_UNLOAD as MYSENSORS_ON_UNLOAD, PLATFORMS_WITH_ENTRY_SUPPORT as PLATFORMS_WITH_ENTRY_SUPPORT, SensorType as SensorType
from .device import MySensorsDevice as MySensorsDevice, get_mysensors_devices as get_mysensors_devices
from .gateway import finish_setup as finish_setup, get_mysensors_gateway as get_mysensors_gateway, gw_stop as gw_stop, setup_gateway as setup_gateway
from .helpers import on_unload as on_unload
from homeassistant import config_entries as config_entries
from homeassistant.components.mqtt import valid_publish_topic as valid_publish_topic, valid_subscribe_topic as valid_subscribe_topic
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_OPTIMISTIC as CONF_OPTIMISTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.typing import ConfigType as ConfigType
from mysensors import BaseAsyncGateway as BaseAsyncGateway
from typing import Any, Callable

_LOGGER: Any
CONF_DEBUG: str
CONF_NODE_NAME: str
DATA_HASS_CONFIG: str
DEFAULT_BAUD_RATE: int
DEFAULT_TCP_PORT: int
DEFAULT_VERSION: str

def set_default_persistence_file(value: dict) -> dict: ...
def has_all_unique_files(value: list[dict]) -> list[dict]: ...
def is_persistence_file(value: str) -> str: ...
def deprecated(key: str) -> Callable[[dict], dict]: ...

NODE_SCHEMA: Any
GATEWAY_SCHEMA: Any
CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def setup_mysensors_platform(hass: HomeAssistant, domain: str, discovery_info: DiscoveryInfo, device_class: Union[type[MySensorsDevice], dict[SensorType, type[MySensorsDevice]]], device_args: Union[None, tuple] = ..., async_add_entities: Union[Callable, None] = ...) -> Union[list[MySensorsDevice], None]: ...
