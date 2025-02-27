from .const import CONF_IMPORTED_BY as CONF_IMPORTED_BY
from .coordinator import PingConfigEntry as PingConfigEntry, PingUpdateCoordinator as PingUpdateCoordinator
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.device_tracker import CONF_CONSIDER_HOME as CONF_CONSIDER_HOME, DEFAULT_CONSIDER_HOME as DEFAULT_CONSIDER_HOME, ScannerEntity as ScannerEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, entry: PingConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PingDeviceTracker(CoordinatorEntity[PingUpdateCoordinator], ScannerEntity):
    _last_seen: datetime | None
    _attr_name: Incomplete
    config_entry: Incomplete
    _consider_home_interval: Incomplete
    def __init__(self, config_entry: PingConfigEntry, coordinator: PingUpdateCoordinator) -> None: ...
    @property
    def ip_address(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
