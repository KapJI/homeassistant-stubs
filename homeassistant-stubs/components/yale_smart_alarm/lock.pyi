from . import YaleConfigEntry as YaleConfigEntry
from .const import CONF_LOCK_CODE_DIGITS as CONF_LOCK_CODE_DIGITS, DEFAULT_LOCK_CODE_DIGITS as DEFAULT_LOCK_CODE_DIGITS, DOMAIN as DOMAIN, YALE_ALL_ERRORS as YALE_ALL_ERRORS
from .coordinator import YaleDataUpdateCoordinator as YaleDataUpdateCoordinator
from .entity import YaleEntity as YaleEntity
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.const import ATTR_CODE as ATTR_CODE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: YaleConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class YaleDoorlock(YaleEntity, LockEntity):
    _attr_name: Incomplete
    _attr_code_format: Incomplete
    lock_name: Incomplete
    def __init__(self, coordinator: YaleDataUpdateCoordinator, data: dict, code_format: int) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_set_lock(self, command: str, code: str | None) -> None: ...
    @property
    def is_locked(self) -> bool | None: ...
