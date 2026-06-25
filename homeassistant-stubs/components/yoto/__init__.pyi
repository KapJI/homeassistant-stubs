from .const import DOMAIN as DOMAIN
from .coordinator import YotoConfigEntry as YotoConfigEntry, YotoDataUpdateCoordinator as YotoDataUpdateCoordinator
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady, OAuth2TokenRequestError as OAuth2TokenRequestError, OAuth2TokenRequestReauthError as OAuth2TokenRequestReauthError
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: YotoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: YotoConfigEntry) -> bool: ...
