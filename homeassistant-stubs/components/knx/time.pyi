from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, CONF_SYNC_STATE as CONF_SYNC_STATE, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS, KNX_MODULE_KEY as KNX_MODULE_KEY
from .entity import KnxUiEntity as KnxUiEntity, KnxUiEntityPlatformController as KnxUiEntityPlatformController, KnxYamlEntity as KnxYamlEntity
from .knx_module import KNXModule as KNXModule
from .storage.const import CONF_ENTITY as CONF_ENTITY, CONF_GA_TIME as CONF_GA_TIME
from .storage.util import ConfigExtractor as ConfigExtractor
from _typeshed import Incomplete
from datetime import time as dt_time
from homeassistant import config_entries as config_entries
from homeassistant.components.time import TimeEntity as TimeEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, Platform as Platform, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any
from xknx.devices import TimeDevice as XknxTimeDevice

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class _KNXTime(TimeEntity, RestoreEntity):
    _device: XknxTimeDevice
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> dt_time | None: ...
    async def async_set_value(self, value: dt_time) -> None: ...

class KnxYamlTime(_KNXTime, KnxYamlEntity):
    _device: XknxTimeDevice
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, knx_module: KNXModule, config: ConfigType) -> None: ...

class KnxUiTime(_KNXTime, KnxUiEntity):
    _device: XknxTimeDevice
    def __init__(self, knx_module: KNXModule, unique_id: str, config: dict[str, Any]) -> None: ...
