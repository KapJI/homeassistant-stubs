from .const import DOMAIN as DOMAIN
from .coordinator import LeilSaunaCoordinator as LeilSaunaCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete
type LeilSaunaConfigEntry = ConfigEntry[LeilSaunaCoordinator]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry) -> bool: ...
