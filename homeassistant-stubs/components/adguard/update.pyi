from . import AdGuardConfigEntry as AdGuardConfigEntry, AdGuardData as AdGuardData
from .const import DOMAIN as DOMAIN
from .entity import AdGuardHomeEntity as AdGuardHomeEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: AdGuardConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AdGuardHomeUpdate(AdGuardHomeEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, data: AdGuardData, entry: AdGuardConfigEntry) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_release_summary: Incomplete
    _attr_release_url: Incomplete
    async def _adguard_update(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
