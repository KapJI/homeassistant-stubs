from _typeshed import Incomplete
from homeassistant.components.image_processing import FaceInformation as FaceInformation, ImageProcessingFaceEntity as ImageProcessingFaceEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class DemoImageProcessingFace(ImageProcessingFaceEntity):
    _attr_name: Incomplete
    _camera: Incomplete
    def __init__(self, camera_entity: str, name: str) -> None: ...
    @property
    def camera_entity(self) -> str: ...
    @property
    def confidence(self) -> int: ...
    def process_image(self, image: bytes) -> None: ...
