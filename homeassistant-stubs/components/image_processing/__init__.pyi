from _typeshed import Incomplete
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.components.camera import Image as Image
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_SOURCE as CONF_SOURCE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from typing import Any, Final, TypedDict

_LOGGER: Incomplete
DOMAIN: str
SCAN_INTERVAL: Incomplete

class ImageProcessingDeviceClass(StrEnum):
    ALPR: str
    FACE: str
    OCR: str

SERVICE_SCAN: str
EVENT_DETECT_FACE: str
ATTR_AGE: str
ATTR_CONFIDENCE: Final[str]
ATTR_FACES: str
ATTR_GENDER: str
ATTR_GLASSES: str
ATTR_MOTION: Final[str]
ATTR_TOTAL_FACES: str
CONF_CONFIDENCE: str
DEFAULT_TIMEOUT: int
DEFAULT_CONFIDENCE: int
SOURCE_SCHEMA: Incomplete
PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete

class FaceInformation(TypedDict):
    confidence: float
    name: str
    age: float
    gender: str
    motion: str
    glasses: str
    entity_id: str

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ImageProcessingEntity(Entity):
    _attr_device_class: Union[ImageProcessingDeviceClass, str, None]
    timeout: Incomplete
    @property
    def camera_entity(self) -> Union[str, None]: ...
    @property
    def confidence(self) -> Union[float, None]: ...
    def process_image(self, image: bytes) -> None: ...
    async def async_process_image(self, image: bytes) -> None: ...
    async def async_update(self) -> None: ...

class ImageProcessingFaceEntity(ImageProcessingEntity):
    _attr_device_class: Incomplete
    faces: Incomplete
    total_faces: int
    def __init__(self) -> None: ...
    @property
    def state(self) -> Union[str, int, None]: ...
    @property
    def state_attributes(self) -> dict[str, Any]: ...
    def process_faces(self, faces: list[FaceInformation], total: int) -> None: ...
    def async_process_faces(self, faces: list[FaceInformation], total: int) -> None: ...
