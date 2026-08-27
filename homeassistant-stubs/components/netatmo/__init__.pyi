from . import api as api
from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import NetatmoConfigEntry as NetatmoConfigEntry, NetatmoDataHandler as NetatmoDataHandler
from .services import async_setup_services as async_setup_services
from .webhook import async_register_webhook as async_register_webhook, async_unregister_webhook as async_unregister_webhook
from _typeshed import Incomplete
from homeassistant.components import cloud as cloud
from homeassistant.const import CONF_WEBHOOK_ID as CONF_WEBHOOK_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, OAuth2TokenRequestError as OAuth2TokenRequestError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation
from homeassistant.helpers.device_registry import AnyDeviceEntry as AnyDeviceEntry, DeviceEntry as DeviceEntry
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.start import async_at_started as async_at_started
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
MAX_WEBHOOK_RETRIES: int

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: NetatmoConfigEntry) -> bool: ...
async def async_config_entry_updated(hass: HomeAssistant, entry: NetatmoConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: NetatmoConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: NetatmoConfigEntry) -> None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: NetatmoConfigEntry, device_entry: AnyDeviceEntry) -> bool: ...
