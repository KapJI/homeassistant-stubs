import upcloud_api
from .const import CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE as CONFIG_ENTRY_UPDATE_SIGNAL_TEMPLATE, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PROBLEM as STATE_PROBLEM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any, Dict

_LOGGER: Any
ATTR_CORE_NUMBER: str
ATTR_HOSTNAME: str
ATTR_MEMORY_AMOUNT: str
ATTR_TITLE: str
ATTR_UUID: str
ATTR_ZONE: str
CONF_SERVERS: str
DATA_UPCLOUD: str
DEFAULT_COMPONENT_NAME: str
DEFAULT_COMPONENT_DEVICE_CLASS: str
CONFIG_ENTRY_DOMAINS: Any
SIGNAL_UPDATE_UPCLOUD: str
STATE_MAP: Any
CONFIG_SCHEMA: Any

class UpCloudDataUpdateCoordinator(DataUpdateCoordinator[Dict[str, upcloud_api.Server]]):
    cloud_manager: Any
    def __init__(self, hass: HomeAssistant, cloud_manager: upcloud_api.CloudManager, update_interval: timedelta, username: str) -> None: ...
    update_interval: Any
    async def async_update_config(self, config_entry: ConfigEntry) -> None: ...
    async def _async_update_data(self) -> dict[str, upcloud_api.Server]: ...

class UpCloudHassData:
    coordinators: dict[str, UpCloudDataUpdateCoordinator]
    scan_interval_migrations: dict[str, int]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _config_entry_update_signal_name(config_entry: ConfigEntry) -> str: ...
async def _async_signal_options_update(hass: HomeAssistant, config_entry: ConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class UpCloudServerEntity(CoordinatorEntity):
    _attr_device_class: Any
    uuid: Any
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, upcloud_api.Server]], uuid: str) -> None: ...
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
