import pathlib
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiohttp import web
from homeassistant.components.http.static import CACHE_HEADERS as CACHE_HEADERS
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import collection as collection
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
STORAGE_KEY: str
STORAGE_VERSION: int
VALID_SIZES: Incomplete
MAX_SIZE: Incomplete
CREATE_FIELDS: Incomplete
UPDATE_FIELDS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ImageStorageCollection(collection.DictStorageCollection):
    CREATE_SCHEMA: Incomplete
    UPDATE_SCHEMA: Incomplete
    image_dir: Incomplete
    def __init__(self, hass: HomeAssistant, image_dir: pathlib.Path) -> None: ...
    async def _process_create_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    def _move_data(self, data: dict[str, Any]) -> int: ...
    def _get_suggested_id(self, info: dict[str, Any]) -> str: ...
    async def _update_data(self, item: dict[str, Any], update_data: dict[str, Any]) -> dict[str, Any]: ...
    async def _change_listener(self, change_type: str, item_id: str, data: dict[str, Any]) -> None: ...

class ImageUploadView(HomeAssistantView):
    url: str
    name: str
    async def post(self, request: web.Request) -> web.Response: ...

class ImageServeView(HomeAssistantView):
    url: str
    name: str
    requires_auth: bool
    transform_lock: Incomplete
    image_folder: Incomplete
    image_collection: Incomplete
    def __init__(self, image_folder: pathlib.Path, image_collection: ImageStorageCollection) -> None: ...
    async def get(self, request: web.Request, image_id: str, filename: str) -> web.FileResponse: ...

def _generate_thumbnail(original_path: pathlib.Path, content_type: str, target_path: pathlib.Path, target_size: tuple[int, int]) -> None: ...
def _validate_size_from_filename(filename: str) -> tuple[int, int]: ...
