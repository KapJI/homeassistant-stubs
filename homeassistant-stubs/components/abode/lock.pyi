from . import AbodeConfigEntry as AbodeConfigEntry
from .entity import AbodeDevice as AbodeDevice
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from jaraco.abode.devices.lock import Lock as Lock
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: AbodeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AbodeLock(AbodeDevice, LockEntity):
    _device: Lock
    _attr_name: Incomplete
    @override
    def lock(self, **kwargs: Any) -> None: ...
    @override
    def unlock(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_locked(self) -> bool: ...
