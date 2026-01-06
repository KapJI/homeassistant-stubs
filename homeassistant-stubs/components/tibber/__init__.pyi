import tibber
from .const import AUTH_IMPLEMENTATION as AUTH_IMPLEMENTATION, CONF_LEGACY_ACCESS_TOKEN as CONF_LEGACY_ACCESS_TOKEN, DATA_HASS_CONFIG as DATA_HASS_CONFIG, DOMAIN as DOMAIN, TibberConfigEntry as TibberConfigEntry
from .coordinator import TibberDataAPICoordinator as TibberDataAPICoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.typing import ConfigType as ConfigType
from tibber import data_api as tibber_data_api

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete
_LOGGER: Incomplete

@dataclass
class TibberRuntimeData:
    tibber_connection: tibber.Tibber
    session: OAuth2Session
    data_api_coordinator: TibberDataAPICoordinator | None = field(default=None)
    _client: tibber_data_api.TibberDataAPI | None = ...
    async def async_get_client(self, hass: HomeAssistant) -> tibber_data_api.TibberDataAPI: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: TibberConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: TibberConfigEntry) -> bool: ...
