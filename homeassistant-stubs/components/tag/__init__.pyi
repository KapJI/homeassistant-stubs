from .const import DEVICE_ID as DEVICE_ID, DOMAIN as DOMAIN, EVENT_TAG_SCANNED as EVENT_TAG_SCANNED, TAG_ID as TAG_ID
from _typeshed import Incomplete
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass

_LOGGER: Incomplete
LAST_SCANNED: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
TAGS: str
CREATE_FIELDS: Incomplete
UPDATE_FIELDS: Incomplete
CONFIG_SCHEMA: Incomplete

class TagIDExistsError(HomeAssistantError):
    item_id: Incomplete
    def __init__(self, item_id: str) -> None: ...

class TagIDManager(collection.IDManager):
    def generate_id(self, suggestion: str) -> str: ...

class TagStorageCollection(collection.DictStorageCollection):
    CREATE_SCHEMA: Incomplete
    UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict) -> dict: ...
    def _get_suggested_id(self, info: dict[str, str]) -> str: ...
    async def _update_data(self, item: dict, update_data: dict) -> dict: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_scan_tag(hass: HomeAssistant, tag_id: str, device_id: str | None, context: Context | None = ...) -> None: ...
