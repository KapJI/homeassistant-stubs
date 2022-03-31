from . import InvalidAuth as InvalidAuth, WallboxCoordinator as WallboxCoordinator, WallboxEntity as WallboxEntity
from .const import CONF_DATA_KEY as CONF_DATA_KEY, CONF_LOCKED_UNLOCKED_KEY as CONF_LOCKED_UNLOCKED_KEY, CONF_SERIAL_NUMBER_KEY as CONF_SERIAL_NUMBER_KEY, DOMAIN as DOMAIN
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

LOCK_TYPES: dict[str, LockEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WallboxLock(WallboxEntity, LockEntity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: WallboxCoordinator, entry: ConfigEntry, description: LockEntityDescription) -> None: ...
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
