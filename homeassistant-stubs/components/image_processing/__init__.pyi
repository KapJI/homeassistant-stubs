from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_NAME as ATTR_NAME, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_SOURCE as CONF_SOURCE
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from typing import Any

_LOGGER: Any
DOMAIN: str
SCAN_INTERVAL: Any
DEVICE_CLASSES: Any
SERVICE_SCAN: str
EVENT_DETECT_FACE: str
ATTR_AGE: str
ATTR_CONFIDENCE: str
ATTR_FACES: str
ATTR_GENDER: str
ATTR_GLASSES: str
ATTR_MOTION: str
ATTR_TOTAL_FACES: str
CONF_CONFIDENCE: str
DEFAULT_TIMEOUT: int
DEFAULT_CONFIDENCE: int
SOURCE_SCHEMA: Any
PLATFORM_SCHEMA: Any
PLATFORM_SCHEMA_BASE: Any

async def async_setup(hass, config): ...

class ImageProcessingEntity(Entity):
    timeout: Any
    @property
    def camera_entity(self) -> None: ...
    @property
    def confidence(self) -> None: ...
    def process_image(self, image) -> None: ...
    async def async_process_image(self, image): ...
    async def async_update(self) -> None: ...

class ImageProcessingFaceEntity(ImageProcessingEntity):
    faces: Any
    total_faces: int
    def __init__(self) -> None: ...
    @property
    def state(self): ...
    @property
    def device_class(self): ...
    @property
    def state_attributes(self): ...
    def process_faces(self, faces, total) -> None: ...
    def async_process_faces(self, faces, total) -> None: ...
