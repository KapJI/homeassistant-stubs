from . import IRON_OS_KEY as IRON_OS_KEY, IronOSConfigEntry as IronOSConfigEntry, IronOSLiveDataCoordinator as IronOSLiveDataCoordinator
from .coordinator import IronOSFirmwareUpdateCoordinator as IronOSFirmwareUpdateCoordinator
from .entity import IronOSBaseEntity as IronOSBaseEntity
from _typeshed import Incomplete
from homeassistant.components.update import ATTR_INSTALLED_VERSION as ATTR_INSTALLED_VERSION, UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity

PARALLEL_UPDATES: int
UPDATE_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IronOSUpdate(IronOSBaseEntity, UpdateEntity, RestoreEntity):
    _attr_supported_features: Incomplete
    firmware_update: Incomplete
    def __init__(self, coordinator: IronOSLiveDataCoordinator, firmware_update: IronOSFirmwareUpdateCoordinator, entity_description: UpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def title(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    async def async_release_notes(self) -> str | None: ...
    _attr_installed_version: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
