from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsConfigEntry as StreamlabsConfigEntry, StreamlabsCoordinator as StreamlabsCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall

ATTR_AWAY_MODE: str
SERVICE_SET_AWAY_MODE: str
AWAY_MODE_AWAY: str
AWAY_MODE_HOME: str
CONF_LOCATION_ID: str
ISSUE_PLACEHOLDER: Incomplete
SET_AWAY_MODE_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: StreamlabsConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: StreamlabsConfigEntry) -> bool: ...
