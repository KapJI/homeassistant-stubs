from .coordinator import RoborockConfigEntry as RoborockConfigEntry, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockMap(RoborockCoordinatedEntityV1, ImageEntity):
    _attr_has_entity_name: bool
    image_last_updated: datetime
    _attr_name: str
    config_entry: Incomplete
    map_flag: Incomplete
    cached_map: bytes
    _attr_entity_category: Incomplete
    def __init__(self, config_entry: ConfigEntry, unique_id: str, coordinator: RoborockDataUpdateCoordinator, map_flag: int, map_name: str) -> None: ...
    @property
    def is_selected(self) -> bool: ...
    _attr_image_last_updated: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
