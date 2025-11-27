from .const import DOMAIN as DOMAIN
from .coordinator import VolvoConfigEntry as VolvoConfigEntry
from .entity import VolvoEntity as VolvoEntity, VolvoEntityDescription as VolvoEntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from volvocarsapi.models import VolvoCarsApiBaseModel as VolvoCarsApiBaseModel

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class VolvoLockDescription(VolvoEntityDescription, LockEntityDescription):
    api_lock_value: str = ...
    api_unlock_value: str = ...
    lock_command: str
    unlock_command: str
    required_command_key: str

_DESCRIPTIONS: tuple[VolvoLockDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VolvoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VolvoLock(VolvoEntity, LockEntity):
    entity_description: VolvoLockDescription
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    _attr_is_locked: Incomplete
    def _update_state(self, api_field: VolvoCarsApiBaseModel | None) -> None: ...
    _attr_is_locking: bool
    _attr_is_unlocking: bool
    async def _async_handle_command(self, command: str, locked: bool) -> None: ...
    def _reset_and_create_error(self, command: str, *, status: str = '', message: str = '') -> HomeAssistantError: ...
