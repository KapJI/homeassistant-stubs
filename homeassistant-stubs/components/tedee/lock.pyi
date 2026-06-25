from .const import DOMAIN as DOMAIN
from .coordinator import TedeeApiCoordinator as TedeeApiCoordinator, TedeeConfigEntry as TedeeConfigEntry
from .entity import TedeeEntity as TedeeEntity
from _typeshed import Incomplete
from aiotedee import TedeeLock as TedeeLock
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityFeature as LockEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: TedeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TedeeLockEntity(TedeeEntity, LockEntity):
    _attr_name: Incomplete
    def __init__(self, lock: TedeeLock, coordinator: TedeeApiCoordinator) -> None: ...
    @property
    @override
    def is_locked(self) -> bool | None: ...
    @property
    @override
    def is_unlocking(self) -> bool: ...
    @property
    @override
    def is_open(self) -> bool: ...
    @property
    @override
    def is_opening(self) -> bool: ...
    @property
    @override
    def is_locking(self) -> bool: ...
    @property
    @override
    def is_jammed(self) -> bool: ...
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def async_unlock(self, **kwargs: Any) -> None: ...
    @override
    async def async_lock(self, **kwargs: Any) -> None: ...

class TedeeLockWithLatchEntity(TedeeLockEntity):
    @property
    @override
    def supported_features(self) -> LockEntityFeature: ...
    @override
    async def async_open(self, **kwargs: Any) -> None: ...
