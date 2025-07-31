from . import UPTIME_KUMA_KEY as UPTIME_KUMA_KEY
from .const import DOMAIN as DOMAIN
from .coordinator import UptimeKumaConfigEntry as UptimeKumaConfigEntry, UptimeKumaDataUpdateCoordinator as UptimeKumaDataUpdateCoordinator, UptimeKumaSoftwareUpdateCoordinator as UptimeKumaSoftwareUpdateCoordinator
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

class UptimeKumaUpdate(StrEnum):
    UPDATE = 'update'

async def async_setup_entry(hass: HomeAssistant, entry: UptimeKumaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UptimeKumaUpdateEntity(CoordinatorEntity[UptimeKumaDataUpdateCoordinator], UpdateEntity):
    entity_description: Incomplete
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    update_checker: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: UptimeKumaDataUpdateCoordinator, update_coordinator: UptimeKumaSoftwareUpdateCoordinator) -> None: ...
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
