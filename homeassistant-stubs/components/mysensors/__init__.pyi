from .const import ATTR_DEVICES as ATTR_DEVICES, DOMAIN as DOMAIN, DevId as DevId, DiscoveryInfo as DiscoveryInfo, MYSENSORS_DISCOVERY as MYSENSORS_DISCOVERY, MYSENSORS_GATEWAYS as MYSENSORS_GATEWAYS, MYSENSORS_ON_UNLOAD as MYSENSORS_ON_UNLOAD, PLATFORMS_WITH_ENTRY_SUPPORT as PLATFORMS_WITH_ENTRY_SUPPORT, SensorType as SensorType
from .device import MySensorsDevice as MySensorsDevice, get_mysensors_devices as get_mysensors_devices
from .gateway import finish_setup as finish_setup, gw_stop as gw_stop, setup_gateway as setup_gateway
from .helpers import on_unload as on_unload
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.typing import ConfigType as ConfigType
from mysensors import BaseAsyncGateway as BaseAsyncGateway

_LOGGER: Incomplete
DATA_HASS_CONFIG: str
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: DeviceEntry) -> bool: ...
def setup_mysensors_platform(hass: HomeAssistant, domain: Platform, discovery_info: DiscoveryInfo, device_class: Union[type[MySensorsDevice], dict[SensorType, type[MySensorsDevice]]], device_args: Union[None, tuple] = ..., async_add_entities: Union[Callable, None] = ...) -> Union[list[MySensorsDevice], None]: ...
