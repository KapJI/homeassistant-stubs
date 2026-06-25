from . import OverkizDataConfigEntry as OverkizDataConfigEntry
from .entity import OverkizEntity as OverkizEntity
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, entry: OverkizDataConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OverkizLock(OverkizEntity, LockEntity):
    @override
    async def async_lock(self, **kwargs: Any) -> None: ...
    @override
    async def async_unlock(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_locked(self) -> bool | None: ...
