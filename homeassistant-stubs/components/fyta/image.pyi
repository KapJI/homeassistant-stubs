from .coordinator import FytaConfigEntry as FytaConfigEntry, FytaCoordinator as FytaCoordinator
from .entity import FytaPlantEntity as FytaPlantEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from fyta_cli.fyta_models import Plant as Plant
from homeassistant.components.image import Image as Image, ImageEntity as ImageEntity, ImageEntityDescription as ImageEntityDescription, valid_image_content_type as valid_image_content_type
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class FytaImageEntityDescription(ImageEntityDescription):
    url_fn: Callable[[Plant], str]
    name_key: str | None = ...

IMAGES: Final[list[FytaImageEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, entry: FytaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FytaPlantImageEntity(FytaPlantEntity, ImageEntity):
    entity_description: FytaImageEntityDescription
    def __init__(self, coordinator: FytaCoordinator, entry: ConfigEntry, description: FytaImageEntityDescription, plant_id: int) -> None: ...
    _cached_image: Incomplete
    async def async_image(self) -> bytes | None: ...
    _attr_image_last_updated: Incomplete
    @property
    def image_url(self) -> str: ...
