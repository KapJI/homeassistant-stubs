from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Doorlock as Doorlock
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ProtectLock(ProtectDeviceEntity, LockEntity):
    device: Doorlock
    entity_description: LockEntityDescription
    _attr_name: Any
    def __init__(self, data: ProtectData, doorlock: Doorlock) -> None: ...
    _attr_is_locked: bool
    _attr_is_locking: bool
    _attr_is_unlocking: bool
    _attr_is_jammed: bool
    _attr_available: bool
    def _async_update_device_from_protect(self) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
