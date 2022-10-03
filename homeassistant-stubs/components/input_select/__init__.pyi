from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.const import ATTR_EDITABLE as ATTR_EDITABLE, ATTR_OPTION as ATTR_OPTION, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.integration_platform import async_process_integration_platform_for_component as async_process_integration_platform_for_component
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
CONF_INITIAL: str
CONF_OPTIONS: str
ATTR_OPTIONS: str
ATTR_CYCLE: str
SERVICE_SELECT_OPTION: str
SERVICE_SELECT_NEXT: str
SERVICE_SELECT_PREVIOUS: str
SERVICE_SELECT_FIRST: str
SERVICE_SELECT_LAST: str
SERVICE_SET_OPTIONS: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_VERSION_MINOR: int

def _unique(options: Any) -> Any: ...

STORAGE_FIELDS: Incomplete

def _remove_duplicates(options: list[str], name: Union[str, None]) -> list[str]: ...
def _cv_input_select(cfg: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_SCHEMA: Incomplete
RELOAD_SERVICE_SCHEMA: Incomplete

class InputSelectStore(Store):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class InputSelectStorageCollection(collection.StorageCollection):
    CREATE_UPDATE_SCHEMA: Incomplete
    async def _process_create_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    def _get_suggested_id(self, info: dict[str, Any]) -> str: ...
    async def _update_data(self, data: dict[str, Any], update_data: dict[str, Any]) -> dict[str, Any]: ...

class InputSelect(collection.CollectionEntity, SelectEntity, RestoreEntity):
    _attr_should_poll: bool
    editable: bool
    _attr_current_option: Incomplete
    _attr_icon: Incomplete
    _attr_name: Incomplete
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    @classmethod
    def from_storage(cls, config: ConfigType) -> InputSelect: ...
    @classmethod
    def from_yaml(cls, config: ConfigType) -> InputSelect: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, bool]: ...
    async def async_select_option(self, option: str) -> None: ...
    def async_select_index(self, idx: int) -> None: ...
    def async_offset_index(self, offset: int, cycle: bool) -> None: ...
    def async_next(self, cycle: bool) -> None: ...
    def async_previous(self, cycle: bool) -> None: ...
    async def async_set_options(self, options: list[str]) -> None: ...
    async def async_update_config(self, config: ConfigType) -> None: ...
