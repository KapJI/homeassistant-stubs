from . import GroupEntity as GroupEntity
from homeassistant.components.lock import DOMAIN as DOMAIN, LockEntity as LockEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, SERVICE_LOCK as SERVICE_LOCK, SERVICE_OPEN as SERVICE_OPEN, SERVICE_UNLOCK as SERVICE_UNLOCK, STATE_JAMMED as STATE_JAMMED, STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str
PARALLEL_UPDATES: int
_LOGGER: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LockGroup(GroupEntity, LockEntity):
    _attr_available: bool
    _attr_should_poll: bool
    _entity_ids: Any
    _attr_name: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    def __init__(self, unique_id: Union[str, None], name: str, entity_ids: list[str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
    _attr_is_jammed: Any
    _attr_is_locking: Any
    _attr_is_unlocking: Any
    _attr_is_locked: Any
    def async_update_group_state(self) -> None: ...
