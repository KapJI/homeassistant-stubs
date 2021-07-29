from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOGGER: Any
STATE_TO_ZWAVE_MAP: dict[int, dict[str, Union[int, bool]]]
SERVICE_SET_LOCK_USERCODE: str
SERVICE_CLEAR_LOCK_USERCODE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveLock(ZWaveBaseEntity, LockEntity):
    @property
    def is_locked(self) -> Union[bool, None]: ...
    async def _set_lock_state(self, target_state: str, **kwargs: dict[str, Any]) -> None: ...
    async def async_lock(self, **kwargs: dict[str, Any]) -> None: ...
    async def async_unlock(self, **kwargs: dict[str, Any]) -> None: ...
    async def async_set_lock_usercode(self, code_slot: int, usercode: str) -> None: ...
    async def async_clear_lock_usercode(self, code_slot: int) -> None: ...
