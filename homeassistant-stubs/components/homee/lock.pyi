from . import HomeeConfigEntry as HomeeConfigEntry
from .entity import HomeeEntity as HomeeEntity
from .helpers import get_name_for_enum as get_name_for_enum, setup_homee_platform as setup_homee_platform
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyHomee.model import HomeeNode as HomeeNode
from typing import Any

PARALLEL_UPDATES: int

async def add_lock_entities(config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, nodes: list[HomeeNode]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeLock(HomeeEntity, LockEntity):
    _attr_name: Incomplete
    @property
    def is_locked(self) -> bool: ...
    @property
    def is_locking(self) -> bool: ...
    @property
    def is_unlocking(self) -> bool: ...
    @property
    def changed_by(self) -> str: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
