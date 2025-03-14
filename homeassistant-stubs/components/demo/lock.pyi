from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature, LockState as LockState
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

LOCK_UNLOCK_DELAY: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DemoLock(LockEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _state: Incomplete
    _openable: Incomplete
    _jam_on_operation: Incomplete
    def __init__(self, name: str, state: str, openable: bool = False, jam_on_operation: bool = False) -> None: ...
    @property
    def is_locking(self) -> bool: ...
    @property
    def is_unlocking(self) -> bool: ...
    @property
    def is_jammed(self) -> bool: ...
    @property
    def is_locked(self) -> bool: ...
    @property
    def is_open(self) -> bool: ...
    @property
    def is_opening(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
