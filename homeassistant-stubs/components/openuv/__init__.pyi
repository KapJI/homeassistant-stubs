from .const import DATA_CLIENT as DATA_CLIENT, DATA_LISTENER as DATA_LISTENER, DATA_PROTECTION_WINDOW as DATA_PROTECTION_WINDOW, DATA_UV as DATA_UV, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_API_KEY as CONF_API_KEY, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SENSORS as CONF_SENSORS
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from pyopenuv import Client
from typing import Any

DEFAULT_ATTRIBUTION: str
NOTIFICATION_ID: str
NOTIFICATION_TITLE: str
TOPIC_UPDATE: Any
PLATFORMS: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class OpenUV:
    client: Any
    data: Any
    def __init__(self, client: Client) -> None: ...
    async def async_update_protection_data(self) -> None: ...
    async def async_update_uv_index_data(self) -> None: ...
    async def async_update(self) -> None: ...

class OpenUvEntity(Entity):
    _attr_extra_state_attributes: Any
    _attr_should_poll: bool
    _attr_unique_id: Any
    _sensor_type: Any
    openuv: Any
    def __init__(self, openuv: OpenUV, sensor_type: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
