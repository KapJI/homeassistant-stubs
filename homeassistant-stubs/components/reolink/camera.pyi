from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription, CameraEntityFeature as CameraEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkCameraEntityDescription(CameraEntityDescription, ReolinkChannelEntityDescription):
    stream: str
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., cmd_key=..., cmd_id=..., supported=..., stream) -> None: ...

CAMERA_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkCamera(ReolinkChannelCoordinatorEntity, Camera):
    entity_description: ReolinkCameraEntityDescription
    _attr_supported_features: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkCameraEntityDescription) -> None: ...
    async def stream_source(self) -> str | None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
