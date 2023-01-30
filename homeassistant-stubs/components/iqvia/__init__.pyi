from .const import CONF_ZIP_CODE as CONF_ZIP_CODE, DOMAIN as DOMAIN, LOGGER as LOGGER, TYPE_ALLERGY_FORECAST as TYPE_ALLERGY_FORECAST, TYPE_ALLERGY_INDEX as TYPE_ALLERGY_INDEX, TYPE_ALLERGY_OUTLOOK as TYPE_ALLERGY_OUTLOOK, TYPE_ASTHMA_FORECAST as TYPE_ASTHMA_FORECAST, TYPE_ASTHMA_INDEX as TYPE_ASTHMA_INDEX, TYPE_DISEASE_FORECAST as TYPE_DISEASE_FORECAST, TYPE_DISEASE_INDEX as TYPE_DISEASE_INDEX
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DEFAULT_ATTRIBUTION: str
DEFAULT_SCAN_INTERVAL: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class IQVIAEntity(CoordinatorEntity[DataUpdateCoordinator[dict[str, Any]]]):
    _attr_has_entity_name: bool
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, Any]], entry: ConfigEntry, description: EntityDescription) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
