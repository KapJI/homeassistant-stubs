from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_JAMMED as STATE_JAMMED, STATE_LOCKED as STATE_LOCKED, STATE_LOCKING as STATE_LOCKING, STATE_UNLOCKED as STATE_UNLOCKED, STATE_UNLOCKING as STATE_UNLOCKING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOCK_UNLOCK_DELAY: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DemoLock(LockEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _state: Incomplete
    _openable: Incomplete
    _jam_on_operation: Incomplete
    def __init__(self, name: str, state: str, openable: bool = ..., jam_on_operation: bool = ...) -> None: ...
    @property
    def is_locking(self) -> bool: ...
    @property
    def is_unlocking(self) -> bool: ...
    @property
    def is_jammed(self) -> bool: ...
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
