from .api import AuthenticatedMonzoAPI as AuthenticatedMonzoAPI, MonzoAPI as MonzoAPI
from .const import CONF_CLOUDHOOK_URL as CONF_CLOUDHOOK_URL, CONF_WEBHOOK_URL as CONF_WEBHOOK_URL, DOMAIN as DOMAIN
from .coordinator import MonzoConfigEntry as MonzoConfigEntry, MonzoCoordinator as MonzoCoordinator, MonzoRuntimeData as MonzoRuntimeData
from .helpers import get_authenticated_owner_name as get_authenticated_owner_name
from .services import async_setup_services as async_setup_services
from .webhook import MonzoWebhookManager as MonzoWebhookManager, async_delete_remote_webhooks as async_delete_remote_webhooks
from _typeshed import Incomplete
from homeassistant.components import cloud as cloud
from homeassistant.components.webhook import async_generate_id as async_generate_id
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, OAuth2TokenRequestError as OAuth2TokenRequestError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def _async_create_api(hass: HomeAssistant, entry: MonzoConfigEntry) -> AuthenticatedMonzoAPI: ...
async def _async_create_removal_api(hass: HomeAssistant, entry: MonzoConfigEntry) -> MonzoAPI: ...

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: MonzoConfigEntry) -> None: ...
