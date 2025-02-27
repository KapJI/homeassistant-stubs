from .coordinator import DormakabaDkeyConfigEntry as DormakabaDkeyConfigEntry, DormakabaDkeyCoordinator as DormakabaDkeyCoordinator
from .entity import DormakabaDkeyEntity as DormakabaDkeyEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: DormakabaDkeyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DormakabaDkeyLock(DormakabaDkeyEntity, LockEntity):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: DormakabaDkeyCoordinator) -> None: ...
    _attr_is_locked: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
