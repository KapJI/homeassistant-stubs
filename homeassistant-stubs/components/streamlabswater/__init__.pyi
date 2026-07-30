from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsConfigEntry as StreamlabsConfigEntry, StreamlabsCoordinator as StreamlabsCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

ISSUE_PLACEHOLDER: Incomplete
PLATFORMS: list[Platform]
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: StreamlabsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: StreamlabsConfigEntry) -> bool: ...
