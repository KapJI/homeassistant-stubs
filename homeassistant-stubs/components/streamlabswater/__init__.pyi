from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsCoordinator as StreamlabsCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

ATTR_AWAY_MODE: str
SERVICE_SET_AWAY_MODE: str
AWAY_MODE_AWAY: str
AWAY_MODE_HOME: str
CONF_LOCATION_ID: str
ISSUE_PLACEHOLDER: Incomplete
CONFIG_SCHEMA: Incomplete
SET_AWAY_MODE_SCHEMA: Incomplete
PLATFORMS: list[Platform]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
