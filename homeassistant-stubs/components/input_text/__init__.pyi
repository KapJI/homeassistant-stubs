from .const import InputTextEntityStateAttribute as InputTextEntityStateAttribute
from _typeshed import Incomplete
from homeassistant.components.text import TextEntity as TextEntity
from homeassistant.const import ATTR_MODE as ATTR_MODE, CONF_ICON as CONF_ICON, CONF_ID as CONF_ID, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, MAX_LENGTH_STATE_STATE as MAX_LENGTH_STATE_STATE, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import collection as collection
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType, VolDictType as VolDictType
from typing import Any, Self, override

_LOGGER: Incomplete
DOMAIN: str
CONF_INITIAL: str
CONF_MIN: str
CONF_MIN_VALUE: int
CONF_MAX: str
CONF_MAX_VALUE: int
CONF_PATTERN: str
CONF_VALUE: str
MODE_TEXT: str
MODE_PASSWORD: str
ATTR_VALUE = CONF_VALUE
ATTR_MIN: str
ATTR_MAX: str
ATTR_PATTERN = CONF_PATTERN
SERVICE_SET_VALUE: str
STORAGE_KEY = DOMAIN
STORAGE_VERSION: int
STORAGE_FIELDS: VolDictType

def _cv_input_text(config: dict[str, Any]) -> dict[str, Any]: ...

CONFIG_SCHEMA: Incomplete
RELOAD_SERVICE_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class InputTextStorageCollection(collection.DictStorageCollection):
    CREATE_UPDATE_SCHEMA: Incomplete
    @override
    async def _process_create_data(self, data: dict[str, Any]) -> dict[str, Any]: ...
    @callback
    @override
    def _get_suggested_id(self, info: dict[str, Any]) -> str: ...
    @override
    async def _update_data(self, item: dict[str, Any], update_data: dict[str, Any]) -> dict[str, Any]: ...

class InputText(collection.CollectionEntity, TextEntity, RestoreEntity):
    _unrecorded_attributes: Incomplete
    _attr_should_poll: bool
    editable: bool
    _attr_native_value: Incomplete
    def __init__(self, config: ConfigType) -> None: ...
    _attr_icon: Incomplete
    _attr_mode: Incomplete
    _attr_name: Incomplete
    _attr_native_min: Incomplete
    _attr_native_max: Incomplete
    _attr_pattern: Incomplete
    _attr_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def _update_config_attributes(self, config: ConfigType) -> None: ...
    @classmethod
    @override
    def from_storage(cls, config: ConfigType) -> Self: ...
    @classmethod
    @override
    def from_yaml(cls, config: ConfigType) -> Self: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_set_value(self, value: str) -> None: ...
    @override
    async def async_update_config(self, config: ConfigType) -> None: ...
