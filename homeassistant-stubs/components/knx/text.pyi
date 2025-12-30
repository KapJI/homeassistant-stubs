from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .knx_module import KNXModule as KNXModule
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_TEXT as CONF_GA_TEXT
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.text import TextEntity as TextEntity, TextMode as TextMode
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from propcache.api import cached_property
from xknx.devices import Notification as XknxNotification

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KnxText(TextEntity, RestoreEntity):
    _device: XknxNotification
    _attr_native_max: int
    async def async_added_to_hass(self) -> None: ...
    @cached_property
    def pattern(self) -> str | None: ...
    @property
    def native_value(self) -> str | None: ...
    async def async_set_value(self, value: str) -> None: ...

class KnxYamlText(_KnxText, KnxYamlEntity):
    _device: XknxNotification
    _attr_mode: Incomplete
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiText(_KnxText, KnxUiEntity):
    _device: XknxNotification
    _attr_mode: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, config: ConfigType) -> None: ...
