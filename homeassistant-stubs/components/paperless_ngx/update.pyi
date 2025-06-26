from .const import LOGGER as LOGGER
from .coordinator import PaperlessConfigEntry as PaperlessConfigEntry, PaperlessStatusCoordinator as PaperlessStatusCoordinator
from .entity import PaperlessEntity as PaperlessEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PAPERLESS_CHANGELOGS: str
PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: PaperlessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PaperlessUpdate(PaperlessEntity[PaperlessStatusCoordinator], UpdateEntity):
    release_url = PAPERLESS_CHANGELOGS
    @property
    def should_poll(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def installed_version(self) -> str | None: ...
    _attr_available: bool
    _attr_latest_version: Incomplete
    async def async_update(self) -> None: ...
