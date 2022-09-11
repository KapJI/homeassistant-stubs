from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.lock import DOMAIN as DOMAIN, LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.models.event import EventType as EventType
from pydeconz.models.light.lock import Lock
from pydeconz.models.sensor.door_lock import DoorLock
from typing import Any, Union

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzLock(DeconzDevice[Union[DoorLock, Lock]], LockEntity):
    TYPE: Incomplete
    @property
    def is_locked(self) -> bool: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
