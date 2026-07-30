from .coordinator import RoborockB01Q10UpdateCoordinator as RoborockB01Q10UpdateCoordinator, RoborockConfigEntry as RoborockConfigEntry, RoborockCoordinatorType as RoborockCoordinatorType, RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .entity import RoborockCoordinatedEntityB01Q10 as RoborockCoordinatedEntityB01Q10, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.image import ImageEntity as ImageEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from roborock.devices.traits.v1.home import HomeTrait as HomeTrait
from roborock.devices.traits.v1.map_content import MapContent as MapContent
from typing import override

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: RoborockConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RoborockMap(RoborockCoordinatedEntityV1, ImageEntity):
    _attr_has_entity_name: bool
    image_last_updated: datetime
    _attr_name: str
    config_entry: Incomplete
    _home_trait: Incomplete
    map_flag: Incomplete
    cached_map: bytes | None
    _attr_entity_category: Incomplete
    _attr_image_last_updated: Incomplete
    def __init__(self, config_entry: ConfigEntry, coordinator: RoborockDataUpdateCoordinator, home_trait: HomeTrait, map_flag: int, map_name: str) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    def _map_content(self) -> MapContent | None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    @override
    async def async_image(self) -> bytes | None: ...

class RoborockMapQ10(RoborockCoordinatedEntityB01Q10, ImageEntity):
    _attr_content_type: str
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    _map_trait: Incomplete
    _cached_map: bytes | None
    def __init__(self, coordinator: RoborockB01Q10UpdateCoordinator) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    _attr_image_last_updated: Incomplete
    @callback
    def _handle_map_update(self) -> None: ...
    @override
    async def async_image(self) -> bytes | None: ...
