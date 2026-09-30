from .coordinator import IndiAllSkyConfigEntry as IndiAllSkyConfigEntry, IndiAllSkyData as IndiAllSkyData, IndiAllSkyDataUpdateCoordinator as IndiAllSkyDataUpdateCoordinator
from .entity import IndiAllSkyEntity as IndiAllSkyEntity
from _typeshed import Incomplete
from aioindiallsky import MediaData as MediaData
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.image import ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription, infer_image_type as infer_image_type
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IndiAllSkyImageEntityDescription(ImageEntityDescription):
    media_fn: Callable[[IndiAllSkyData], MediaData | None]
    fallback_filename: str

IMAGE_DESCRIPTIONS: tuple[IndiAllSkyImageEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: IndiAllSkyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndiAllSkyImageEntity(IndiAllSkyEntity, ImageEntity):
    entity_description: IndiAllSkyImageEntityDescription
    _attr_unique_id: Incomplete
    _last_fetched: datetime | None
    def __init__(self, hass: HomeAssistant, coordinator: IndiAllSkyDataUpdateCoordinator, entry: IndiAllSkyConfigEntry, description: IndiAllSkyImageEntityDescription) -> None: ...
    @property
    @override
    def image_last_updated(self) -> datetime | None: ...
    _attr_content_type: Incomplete
    @override
    async def async_image(self) -> bytes | None: ...
