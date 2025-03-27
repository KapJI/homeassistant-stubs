from .const import _LOGGER as _LOGGER
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationDeviceInfo as VodafoneStationDeviceInfo, VodafoneStationRouter as VodafoneStationRouter
from _typeshed import Incomplete
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
@callback
def async_add_new_tracked_entities(coordinator: VodafoneStationRouter, async_add_entities: AddConfigEntryEntitiesCallback, tracked: set[str]) -> None: ...

class VodafoneStationTracker(CoordinatorEntity[VodafoneStationRouter], ScannerEntity):
    _attr_translation_key: str
    _attr_has_entity_name: bool
    mac_address: str
    _coordinator: Incomplete
    _attr_mac_address: Incomplete
    _attr_unique_id: Incomplete
    _attr_hostname: Incomplete
    def __init__(self, coordinator: VodafoneStationRouter, device_info: VodafoneStationDeviceInfo) -> None: ...
    @property
    def _device_info(self) -> VodafoneStationDeviceInfo: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def ip_address(self) -> str | None: ...
