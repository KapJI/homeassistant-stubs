from . import HabiticaConfigEntry as HabiticaConfigEntry
from .coordinator import HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from _typeshed import Incomplete
from enum import StrEnum
from habiticalib import UserStyles
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

PARALLEL_UPDATES: int

class HabiticaImageEntity(StrEnum):
    AVATAR = 'avatar'

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HabiticaImage(HabiticaBase, ImageEntity):
    entity_description: Incomplete
    _attr_content_type: str
    _current_appearance: UserStyles | None
    _cache: bytes | None
    _attr_image_last_updated: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: HabiticaDataUpdateCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
