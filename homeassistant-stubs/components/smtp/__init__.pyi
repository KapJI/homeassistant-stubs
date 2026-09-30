from .const import CONF_ENCRYPTION as CONF_ENCRYPTION, CONF_ENTRY as CONF_ENTRY, CONF_OLD_RECIPIENT as CONF_OLD_RECIPIENT, CONF_SERVER as CONF_SERVER, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from aiosmtplib import SMTP
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RECIPIENT as CONF_RECIPIENT, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.ssl import client_context as client_context, client_context_no_verify as client_context_no_verify

_LOGGER: Incomplete
type SmtpConfigEntry = ConfigEntry[SMTP]
PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SmtpConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: SmtpConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: SmtpConfigEntry) -> bool: ...
async def async_migrate_subentries(hass: HomeAssistant, entry: SmtpConfigEntry) -> None: ...
