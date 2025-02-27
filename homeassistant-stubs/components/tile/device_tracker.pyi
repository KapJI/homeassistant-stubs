from .coordinator import TileConfigEntry as TileConfigEntry, TileCoordinator as TileCoordinator
from .entity import TileEntity as TileEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import as_utc as as_utc

_LOGGER: Incomplete
ATTR_ALTITUDE: str
ATTR_CONNECTION_STATE: str
ATTR_IS_DEAD: str
ATTR_IS_LOST: str
ATTR_LAST_LOST_TIMESTAMP: str
ATTR_LAST_TIMESTAMP: str
ATTR_RING_STATE: str
ATTR_TILE_NAME: str
ATTR_VOIP_STATE: str

async def async_setup_entry(hass: HomeAssistant, entry: TileConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TileDeviceTracker(TileEntity, TrackerEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_extra_state_attributes: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TileCoordinator) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_longitude: Incomplete
    _attr_latitude: Incomplete
    _attr_location_accuracy: Incomplete
    @callback
    def _update_from_latest_data(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
