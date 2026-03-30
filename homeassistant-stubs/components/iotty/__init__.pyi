from .const import DOMAIN as DOMAIN
from .coordinator import IottyConfigEntry as IottyConfigEntry, IottyConfigEntryData as IottyConfigEntryData, IottyDataUpdateCoordinator as IottyDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.config_entry_oauth2_flow import ImplementationUnavailableError as ImplementationUnavailableError, OAuth2Session as OAuth2Session, async_get_config_entry_implementation as async_get_config_entry_implementation

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: IottyConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IottyConfigEntry) -> bool: ...
