from . import PajGpsConfigEntry as PajGpsConfigEntry
from .coordinator import PajGpsCoordinator as PajGpsCoordinator
from .entity import PajGpsEntity as PajGpsEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: PajGpsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PajGPSDeviceTracker(PajGpsEntity, TrackerEntity):
    _attr_name: Incomplete
    _attr_icon: str
    _attr_unique_id: Incomplete
    def __init__(self, pajgps_coordinator: PajGpsCoordinator, device_id: int) -> None: ...
    @property
    def latitude(self) -> float | None: ...
    @property
    def longitude(self) -> float | None: ...
