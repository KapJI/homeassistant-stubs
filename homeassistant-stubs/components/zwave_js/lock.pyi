from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER, SERVICE_CLEAR_LOCK_USERCODE as SERVICE_CLEAR_LOCK_USERCODE, SERVICE_SET_LOCK_USERCODE as SERVICE_SET_LOCK_USERCODE
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_LOCKED as STATE_LOCKED, STATE_UNLOCKED as STATE_UNLOCKED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
STATE_TO_ZWAVE_MAP: dict[int, dict[str, int | bool]]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZWaveLock(ZWaveBaseEntity, LockEntity):
    @property
    def is_locked(self) -> bool | None: ...
    async def _set_lock_state(self, target_state: str, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_set_lock_usercode(self, code_slot: int, usercode: str) -> None: ...
    async def async_clear_lock_usercode(self, code_slot: int) -> None: ...
