from .coordinator import XboxConfigEntry as XboxConfigEntry, XboxPresenceCoordinator as XboxPresenceCoordinator
from .entity import XboxBaseEntity as XboxBaseEntity, XboxBaseEntityDescription as XboxBaseEntityDescription, profile_pic as profile_pic
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pythonxbox.api.provider.people.models import Person as Person
from pythonxbox.api.provider.titlehub.models import Title as Title
from typing import override

PARALLEL_UPDATES: int

class XboxImage(StrEnum):
    NOW_PLAYING = 'now_playing'
    GAMERPIC = 'gamerpic'
    AVATAR = 'avatar'
    POSTER = 'poster'
    BRANDED_KEY_ART = 'branded_key_art'
    TITLED_HERO_ART = 'titled_hero_art'
    SUPER_HERO_ART = 'super_hero_art'
    BOX_ART = 'box_art'
    FEATURE_PROMOTIONAL_SQUARE_ART = 'feature_promotional_square_art'

@dataclass(kw_only=True, frozen=True)
class XboxImageEntityDescription(XboxBaseEntityDescription, ImageEntityDescription):
    image_url_fn: Callable[[Person, Title | None], str | None]

IMAGE_DESCRIPTIONS: tuple[XboxImageEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: XboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class XboxImageEntity(XboxBaseEntity, ImageEntity):
    entity_description: XboxImageEntityDescription
    _attr_image_url: Incomplete
    _attr_image_last_updated: Incomplete
    def __init__(self, hass: HomeAssistant, coordinator: XboxPresenceCoordinator, xuid: str, entity_description: XboxImageEntityDescription) -> None: ...
    _cached_image: Incomplete
    @override
    def _handle_coordinator_update(self) -> None: ...
