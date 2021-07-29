from . import DATA_COORDINATOR as DATA_COORDINATOR, DATA_TILE as DATA_TILE, DOMAIN as DOMAIN
from collections.abc import Awaitable
from homeassistant.components.device_tracker.config_entry import TrackerEntity as TrackerEntity
from homeassistant.components.device_tracker.const import SOURCE_TYPE_GPS as SOURCE_TYPE_GPS
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from pytile.tile import Tile as Tile
from typing import Any, Callable

_LOGGER: Any
ATTR_ALTITUDE: str
ATTR_CONNECTION_STATE: str
ATTR_IS_DEAD: str
ATTR_IS_LOST: str
ATTR_LAST_LOST_TIMESTAMP: str
ATTR_RING_STATE: str
ATTR_TILE_NAME: str
ATTR_VOIP_STATE: str
DEFAULT_ATTRIBUTION: str
DEFAULT_ICON: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
async def async_setup_scanner(hass: HomeAssistant, config: ConfigType, async_see: Callable[..., Awaitable[None]], discovery_info: Union[dict[str, Any], None] = ...) -> bool: ...

class TileDeviceTracker(CoordinatorEntity, TrackerEntity):
    _attr_icon: Any
    _attr_extra_state_attributes: Any
    _attr_name: Any
    _attr_unique_id: Any
    _entry: Any
    _tile: Any
    def __init__(self, entry: ConfigEntry, coordinator: DataUpdateCoordinator, tile: Tile) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def location_accuracy(self) -> int: ...
    @property
    def latitude(self) -> Union[float, None]: ...
    @property
    def longitude(self) -> Union[float, None]: ...
    @property
    def source_type(self) -> str: ...
    def _handle_coordinator_update(self) -> None: ...
    def _update_from_latest_data(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
