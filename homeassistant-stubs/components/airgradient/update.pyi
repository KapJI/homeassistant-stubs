from . import AirGradientConfigEntry as AirGradientConfigEntry, AirGradientCoordinator as AirGradientCoordinator
from .entity import AirGradientEntity as AirGradientEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from propcache.api import cached_property

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: AirGradientConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirGradientUpdate(AirGradientEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _server_unreachable_logged: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirGradientCoordinator) -> None: ...
    @cached_property
    def should_poll(self) -> bool: ...
    @property
    def installed_version(self) -> str: ...
    @property
    def available(self) -> bool: ...
    _attr_latest_version: Incomplete
    _attr_available: bool
    async def async_update(self) -> None: ...
