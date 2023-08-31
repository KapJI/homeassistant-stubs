from .const import ATTR_FLAP_ID as ATTR_FLAP_ID, ATTR_LOCATION as ATTR_LOCATION, ATTR_LOCK_STATE as ATTR_LOCK_STATE, ATTR_PET_NAME as ATTR_PET_NAME, CONF_FEEDERS as CONF_FEEDERS, CONF_FLAPS as CONF_FLAPS, CONF_PETS as CONF_PETS, DOMAIN as DOMAIN, SERVICE_SET_LOCK_STATE as SERVICE_SET_LOCK_STATE, SERVICE_SET_PET_LOCATION as SERVICE_SET_PET_LOCATION, SURE_API_TIMEOUT as SURE_API_TIMEOUT
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from surepy import SurepyEntity

_LOGGER: Incomplete
PLATFORMS: Incomplete
SCAN_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SurePetcareDataCoordinator(DataUpdateCoordinator[dict[int, SurepyEntity]]):
    surepy: Incomplete
    lock_states_callbacks: Incomplete
    def __init__(self, entry: ConfigEntry, hass: HomeAssistant) -> None: ...
    async def _async_update_data(self) -> dict[int, SurepyEntity]: ...
    async def handle_set_lock_state(self, call: ServiceCall) -> None: ...
    def get_pets(self) -> dict[str, int]: ...
    async def handle_set_pet_location(self, call: ServiceCall) -> None: ...
