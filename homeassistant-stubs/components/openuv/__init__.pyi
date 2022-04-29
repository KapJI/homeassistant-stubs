from .const import CONF_FROM_WINDOW as CONF_FROM_WINDOW, CONF_TO_WINDOW as CONF_TO_WINDOW, DATA_PROTECTION_WINDOW as DATA_PROTECTION_WINDOW, DATA_UV as DATA_UV, DEFAULT_FROM_WINDOW as DEFAULT_FROM_WINDOW, DEFAULT_TO_WINDOW as DEFAULT_TO_WINDOW, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SENSORS as CONF_SENSORS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from pyopenuv import Client

DEFAULT_ATTRIBUTION: str
NOTIFICATION_ID: str
NOTIFICATION_TITLE: str
TOPIC_UPDATE: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class OpenUV:
    _entry: Incomplete
    client: Incomplete
    data: Incomplete
    def __init__(self, entry: ConfigEntry, client: Client) -> None: ...
    async def async_update_protection_data(self) -> None: ...
    async def async_update_uv_index_data(self) -> None: ...
    async def async_update(self) -> None: ...

class OpenUvEntity(Entity):
    _attr_extra_state_attributes: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    openuv: Incomplete
    def __init__(self, openuv: OpenUV, description: EntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
