from _typeshed import Incomplete
from homeassistant.components.image_processing import FaceInformation as FaceInformation, ImageProcessingFaceEntity as ImageProcessingFaceEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import override

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class DemoImageProcessingFace(ImageProcessingFaceEntity):
    _attr_name: Incomplete
    _camera: Incomplete
    def __init__(self, camera_entity: str, name: str) -> None: ...
    @property
    @override
    def camera_entity(self) -> str: ...
    @property
    @override
    def confidence(self) -> int: ...
    @override
    async def async_process_image(self, image: bytes) -> None: ...
