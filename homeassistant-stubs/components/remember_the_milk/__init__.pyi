from .const import CONF_LIST_ID as CONF_LIST_ID, CONF_SHARED_SECRET as CONF_SHARED_SECRET, DOMAIN as DOMAIN, LOGGER as LOGGER, SUBENTRY_TYPE_LIST as SUBENTRY_TYPE_LIST
from .coordinator import RememberTheMilkConfigEntry as RememberTheMilkConfigEntry, RememberTheMilkData as RememberTheMilkData, RtmTodoCoordinator as RtmTodoCoordinator
from .entity import RememberTheMilkEntity as RememberTheMilkEntity
from .storage import RememberTheMilkConfiguration as RememberTheMilkConfiguration
from _typeshed import Incomplete
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PLATFORMS: Incomplete
RTM_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_CREATE_TASK: str
SERVICE_COMPLETE_TASK: str
SERVICE_SCHEMA_CREATE_TASK: Incomplete
SERVICE_SCHEMA_COMPLETE_TASK: Incomplete
DATA_COMPONENT: str
DATA_STORAGE: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_import(hass: HomeAssistant, storage: RememberTheMilkConfiguration, rtm_config: dict[str, Any]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: RememberTheMilkConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: RememberTheMilkConfigEntry) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: RememberTheMilkConfigEntry) -> bool: ...
