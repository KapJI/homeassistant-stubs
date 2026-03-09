from . import NTFY_KEY as NTFY_KEY
from .const import DEFAULT_URL as DEFAULT_URL
from .coordinator import NtfyConfigEntry as NtfyConfigEntry, NtfyLatestReleaseUpdateCoordinator as NtfyLatestReleaseUpdateCoordinator, NtfyVersionDataUpdateCoordinator as NtfyVersionDataUpdateCoordinator
from .entity import NtfyCommonBaseEntity as NtfyCommonBaseEntity
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import CONF_URL as CONF_URL, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class NtfyUpdate(StrEnum):
    UPDATE = 'update'

DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NtfyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NtfyUpdateEntity(NtfyCommonBaseEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    coordinator: NtfyVersionDataUpdateCoordinator
    update_checker: Incomplete
    def __init__(self, coordinator: NtfyVersionDataUpdateCoordinator, update_checker: NtfyLatestReleaseUpdateCoordinator, description: EntityDescription) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def title(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    async def async_release_notes(self) -> str | None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
