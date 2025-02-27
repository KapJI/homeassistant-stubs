from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from _typeshed import Incomplete
from enum import StrEnum
from habiticalib import Avatar as Avatar
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class HabiticaImageEntity(StrEnum):
    AVATAR = 'avatar'

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaImage(HabiticaBase, ImageEntity):
    entity_description: Incomplete
    _attr_content_type: str
    _avatar: Avatar | None
    _cache: bytes | None
    _attr_image_last_updated: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: HabiticaDataUpdateCoordinator) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_image(self) -> bytes | None: ...
