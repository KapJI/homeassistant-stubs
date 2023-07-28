from .const import DOMAIN as DOMAIN
from .entity import YALEXSBLEEntity as YALEXSBLEEntity
from .models import YaleXSBLEData as YaleXSBLEData
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from yalexs_ble import ConnectionInfo as ConnectionInfo, LockInfo as LockInfo, LockState as LockState

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleXSBLELock(YALEXSBLEEntity, LockEntity):
    _attr_name: Incomplete
    _attr_is_locked: bool
    _attr_is_locking: bool
    _attr_is_unlocking: bool
    _attr_is_jammed: bool
    def _async_update_state(self, new_state: LockState, lock_info: LockInfo, connection_info: ConnectionInfo) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
