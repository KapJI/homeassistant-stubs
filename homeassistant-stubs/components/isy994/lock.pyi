from .const import ISY994_NODES as ISY994_NODES, ISY994_PROGRAMS as ISY994_PROGRAMS, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity, ISYProgramEntity as ISYProgramEntity
from .helpers import migrate_old_unique_ids as migrate_old_unique_ids
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

VALUE_TO_STATE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYLockEntity(ISYNodeEntity, LockEntity):
    @property
    def is_locked(self) -> Union[bool, None]: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...

class ISYLockProgramEntity(ISYProgramEntity, LockEntity):
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
