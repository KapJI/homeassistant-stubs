from . import DeconzConfigEntry as DeconzConfigEntry
from .entity import DeconzDevice as DeconzDevice
from homeassistant.components.lock import DOMAIN as LOCK_DOMAIN, LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.light.lock import Lock
from pydeconz.models.sensor.door_lock import DoorLock
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: DeconzConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DeconzLock(DeconzDevice[DoorLock | Lock], LockEntity):
    TYPE = LOCK_DOMAIN
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
