from . import SimpliSafe as SimpliSafe, SimpliSafeEntity as SimpliSafeEntity
from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.lock import Lock as Lock
from simplipy.system.v3 import SystemV3 as SystemV3
from typing import Any

ATTR_LOCK_LOW_BATTERY: str
ATTR_JAMMED: str
ATTR_PIN_PAD_LOW_BATTERY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimpliSafeLock(SimpliSafeEntity, LockEntity):
    _lock: Any
    def __init__(self, simplisafe: SimpliSafe, system: SystemV3, lock: Lock) -> None: ...
    _attr_is_locked: bool
    async def async_lock(self, **kwargs: dict[str, Any]) -> None: ...
    async def async_unlock(self, **kwargs: dict[str, Any]) -> None: ...
    def async_update_from_rest_api(self) -> None: ...
