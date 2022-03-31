from .const import CONF_FORCE as CONF_FORCE, DATA_ADGUARD_CLIENT as DATA_ADGUARD_CLIENT, DATA_ADGUARD_VERSION as DATA_ADGUARD_VERSION, DOMAIN as DOMAIN, SERVICE_ADD_URL as SERVICE_ADD_URL, SERVICE_DISABLE_URL as SERVICE_DISABLE_URL, SERVICE_ENABLE_URL as SERVICE_ENABLE_URL, SERVICE_REFRESH as SERVICE_REFRESH, SERVICE_REMOVE_URL as SERVICE_REMOVE_URL
from adguardhome import AdGuardHome
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SSL as CONF_SSL, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from typing import Any

_LOGGER: Any
SERVICE_URL_SCHEMA: Any
SERVICE_ADD_URL_SCHEMA: Any
SERVICE_REFRESH_SCHEMA: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AdGuardHomeEntity(Entity):
    _available: bool
    _enabled_default: Any
    _icon: Any
    _name: Any
    _entry: Any
    adguard: Any
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry, name: str, icon: str, enabled_default: bool = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    async def _adguard_update(self) -> None: ...

class AdGuardHomeDeviceEntity(AdGuardHomeEntity):
    @property
    def device_info(self) -> DeviceInfo: ...
