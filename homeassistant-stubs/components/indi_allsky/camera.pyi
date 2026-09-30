from .coordinator import IndiAllSkyConfigEntry as IndiAllSkyConfigEntry, IndiAllSkyDataUpdateCoordinator as IndiAllSkyDataUpdateCoordinator
from .entity import IndiAllSkyEntity as IndiAllSkyEntity
from _typeshed import Incomplete
from homeassistant.components.camera import Camera as Camera
from homeassistant.components.image import infer_image_type as infer_image_type
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: IndiAllSkyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IndiAllSkyCamera(IndiAllSkyEntity, Camera):
    translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: IndiAllSkyDataUpdateCoordinator, entry: IndiAllSkyConfigEntry) -> None: ...
    content_type: Incomplete
    @override
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
