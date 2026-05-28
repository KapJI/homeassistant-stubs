from .coordinator import PrusaLinkConfigEntry as PrusaLinkConfigEntry, PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from .entity import PrusaLinkEntity as PrusaLinkEntity, PrusaLinkEntityDescription as PrusaLinkEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class PrusaLinkCameraEntityDescription(CameraEntityDescription, PrusaLinkEntityDescription): ...

async def async_setup_entry(hass: HomeAssistant, entry: PrusaLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PrusaLinkJobPreviewEntity(PrusaLinkEntity, Camera):
    entity_description: Incomplete
    last_path: str
    last_image: bytes
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
