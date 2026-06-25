from .const import CONF_ENCRYPTION as CONF_ENCRYPTION, CONF_SENDER_NAME as CONF_SENDER_NAME, CONF_SERVER as CONF_SERVER, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from .helpers import SmtpClient as SmtpClient
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RECIPIENT as CONF_RECIPIENT, CONF_SENDER as CONF_SENDER, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.util.ssl import create_client_context as create_client_context

_LOGGER: Incomplete
type SmtpConfigEntry = ConfigEntry[SmtpClient]
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: SmtpConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: SmtpConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: SmtpConfigEntry) -> bool: ...
