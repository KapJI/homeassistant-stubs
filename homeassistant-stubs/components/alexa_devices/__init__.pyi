from .const import CONF_LOGIN_DATA as CONF_LOGIN_DATA, CONF_SITE as CONF_SITE, COUNTRY_DOMAINS as COUNTRY_DOMAINS, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import AmazonConfigEntry as AmazonConfigEntry, AmazonDevicesCoordinator as AmazonDevicesCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.const import CONF_COUNTRY as CONF_COUNTRY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, httpx_client as httpx_client
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.ssl import SSL_ALPN_HTTP11_HTTP2 as SSL_ALPN_HTTP11_HTTP2

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_initial_sync(sync_call: Callable[[], Awaitable[None]]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: AmazonConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: AmazonConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: AmazonConfigEntry) -> bool: ...
