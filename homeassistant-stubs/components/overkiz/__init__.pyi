from .const import CONF_API_TYPE as CONF_API_TYPE, CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_HUB as CONF_HUB, DOMAIN as DOMAIN, LOGGER as LOGGER, OVERKIZ_DEVICE_TO_PLATFORM as OVERKIZ_DEVICE_TO_PLATFORM, PLATFORMS as PLATFORMS, UPDATE_INTERVAL_ALL_ASSUMED_STATE as UPDATE_INTERVAL_ALL_ASSUMED_STATE, UPDATE_INTERVAL_LOCAL as UPDATE_INTERVAL_LOCAL
from .coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from collections import defaultdict
from dataclasses import dataclass
from homeassistant.components.application_credentials import ClientCredential as ClientCredential, async_import_client_credential as async_import_client_credential
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, OAuth2TokenRequestError as OAuth2TokenRequestError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.helpers.typing import ConfigType as ConfigType
from pyoverkiz.client import OverkizClient
from pyoverkiz.enums import Server
from pyoverkiz.models import Device as Device, PersistedActionGroup as PersistedActionGroup

CONFIG_SCHEMA: Incomplete

@dataclass
class HomeAssistantOverkizData:
    coordinator: OverkizDataUpdateCoordinator
    platforms: defaultdict[Platform, list[Device]]
    scenarios: list[PersistedActionGroup]
type OverkizDataConfigEntry = ConfigEntry[HomeAssistantOverkizData]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> bool: ...
async def _async_migrate_strenum_unique_ids(hass: HomeAssistant, config_entry: OverkizDataConfigEntry) -> None: ...
def create_local_client(hass: HomeAssistant, host: str, token: str, verify_ssl: bool) -> OverkizClient: ...
def create_cloud_client(hass: HomeAssistant, username: str, password: str, server: Server) -> OverkizClient: ...
async def create_rexel_client(hass: HomeAssistant, entry: OverkizDataConfigEntry) -> OverkizClient: ...
