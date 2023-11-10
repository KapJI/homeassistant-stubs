import dataclasses
import upcloud_api
from .const import CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE as CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PROBLEM as STATE_PROBLEM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete
ATTR_CORE_NUMBER: str
ATTR_HOSTNAME: str
ATTR_MEMORY_AMOUNT: str
ATTR_TITLE: str
ATTR_UUID: str
ATTR_ZONE: str
CONF_SERVERS: str
DATA_UPCLOUD: str
DEFAULT_COMPONENT_NAME: str
PLATFORMS: Incomplete
SIGNAL_UPDATE_UPCLOUD: str
STATE_MAP: Incomplete

class UpCloudDataUpdateCoordinator(DataUpdateCoordinator[dict[str, upcloud_api.Server]]):
    cloud_manager: Incomplete
    def __init__(self, hass: HomeAssistant, *, cloud_manager: upcloud_api.CloudManager, update_interval: timedelta, username: str) -> None: ...
    update_interval: Incomplete
    async def async_update_config(self, config_entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, upcloud_api.Server]: ...

@dataclasses.dataclass
class UpCloudHassData:
    coordinators: dict[str, UpCloudDataUpdateCoordinator] = ...
    def __init__(self, coordinators) -> None: ...

def _config_entry_update_signal_name(config_entry: ConfigEntry) -> str: ...
async def _async_signal_options_update(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class UpCloudServerEntity(CoordinatorEntity[UpCloudDataUpdateCoordinator]):
    uuid: Incomplete
    def __init__(self, coordinator: UpCloudDataUpdateCoordinator, uuid: str) -> None: ...
    @property
    def _server(self) -> upcloud_api.Server: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def device_info(self) -> DeviceInfo: ...
