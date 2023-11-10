import httpx
from .const import DOMAIN as DOMAIN, IMAGE_TIMEOUT as IMAGE_TIMEOUT
from _typeshed import Incomplete
from aiohttp import web
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_AUTHENTICATED as KEY_AUTHENTICATED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA as PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE as PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.httpx_client import get_async_client as get_async_client
from homeassistant.helpers.typing import ConfigType as ConfigType, UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Final

_LOGGER: Incomplete
SCAN_INTERVAL: Final[Incomplete]
ENTITY_ID_FORMAT: Final[Incomplete]
DEFAULT_CONTENT_TYPE: Final[str]
ENTITY_IMAGE_URL: Final[str]
TOKEN_CHANGE_INTERVAL: Final[Incomplete]
_RND: Final[Incomplete]
GET_IMAGE_TIMEOUT: Final[int]

@dataclass
class ImageEntityDescription(EntityDescription):
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

@dataclass
class Image:
    content_type: str
    content: bytes
    def __init__(self, content_type, content) -> None: ...

class ImageContentTypeError(HomeAssistantError): ...

def valid_image_content_type(content_type: str | None) -> str: ...
async def _async_get_image(image_entity: ImageEntity, timeout: int) -> Image: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class ImageEntity(Entity):
    _entity_component_unrecorded_attributes: Incomplete
    _attr_content_type: str
    _attr_image_last_updated: datetime | None
    _attr_image_url: str | None | UndefinedType
    _attr_should_poll: bool
    _attr_state: None
    _cached_image: Image | None
    _client: Incomplete
    access_tokens: Incomplete
    def __init__(self, hass: HomeAssistant, verify_ssl: bool = ...) -> None: ...
    @property
    def content_type(self) -> str: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def image_last_updated(self) -> datetime | None: ...
    @property
    def image_url(self) -> str | None | UndefinedType: ...
    def image(self) -> bytes | None: ...
    async def _fetch_url(self, url: str) -> httpx.Response | None: ...
    async def _async_load_image_from_url(self, url: str) -> Image | None: ...
    async def async_image(self) -> bytes | None: ...
    @property
    def state(self) -> str | None: ...
    @property
    def state_attributes(self) -> dict[str, str | None]: ...
    def async_update_token(self) -> None: ...

class ImageView(HomeAssistantView):
    name: str
    requires_auth: bool
    url: str
    component: Incomplete
    def __init__(self, component: EntityComponent[ImageEntity]) -> None: ...
    async def get(self, request: web.Request, entity_id: str) -> web.StreamResponse: ...
    async def handle(self, request: web.Request, image_entity: ImageEntity) -> web.StreamResponse: ...
