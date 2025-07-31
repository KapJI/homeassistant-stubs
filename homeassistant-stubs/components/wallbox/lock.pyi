from .const import CHARGER_DATA_KEY as CHARGER_DATA_KEY, CHARGER_LOCKED_UNLOCKED_KEY as CHARGER_LOCKED_UNLOCKED_KEY, CHARGER_SERIAL_NUMBER_KEY as CHARGER_SERIAL_NUMBER_KEY
from .coordinator import WallboxConfigEntry as WallboxConfigEntry, WallboxCoordinator as WallboxCoordinator
from .entity import WallboxEntity as WallboxEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

LOCK_TYPES: dict[str, LockEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: WallboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class WallboxLock(WallboxEntity, LockEntity):
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WallboxCoordinator, description: LockEntityDescription) -> None: ...
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
