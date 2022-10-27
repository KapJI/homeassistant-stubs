from .const import CONF_FROM_WINDOW as CONF_FROM_WINDOW, CONF_TO_WINDOW as CONF_TO_WINDOW, DATA_PROTECTION_WINDOW as DATA_PROTECTION_WINDOW, DATA_UV as DATA_UV, DEFAULT_FROM_WINDOW as DEFAULT_FROM_WINDOW, DEFAULT_TO_WINDOW as DEFAULT_TO_WINDOW, DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import OpenUvCoordinator as OpenUvCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_ELEVATION as CONF_ELEVATION, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_SENSORS as CONF_SENSORS, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import aiohttp_client as aiohttp_client, entity_registry as entity_registry
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, UpdateFailed as UpdateFailed

CONF_ENTRY_ID: str
PLATFORMS: Incomplete
SERVICE_NAME_UPDATE_DATA: str
SERVICE_NAME_UPDATE_PROTECTION_DATA: str
SERVICE_NAME_UPDATE_UV_INDEX_DATA: str
SERVICES: Incomplete

def async_get_entity_id_from_unique_id_suffix(hass: HomeAssistant, entry: ConfigEntry, unique_id_suffix: str) -> str: ...
def async_log_deprecated_service_call(hass: HomeAssistant, call: ServiceCall, alternate_service: str, alternate_targets: list[str], breaks_in_ha_version: str) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class OpenUvEntity(CoordinatorEntity):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: OpenUvCoordinator, description: EntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    def _update_from_latest_data(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
