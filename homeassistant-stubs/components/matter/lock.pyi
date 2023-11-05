from .const import LOGGER as LOGGER
from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from homeassistant.components.lock import LockEntity as LockEntity, LockEntityDescription as LockEntityDescription, LockEntityFeature as LockEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DoorLockFeature: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MatterLock(MatterEntity, LockEntity):
    features: int | None
    @property
    def code_format(self) -> str | None: ...
    @property
    def supports_door_position_sensor(self) -> bool: ...
    @property
    def supports_unbolt(self) -> bool: ...
    async def send_device_command(self, command: clusters.ClusterCommand, timed_request_timeout_ms: int = ...) -> None: ...
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...
    async def async_open(self, **kwargs: Any) -> None: ...
    _attr_supported_features: Incomplete
    _attr_is_locked: bool
    _attr_is_locking: bool
    _attr_is_unlocking: bool
    _attr_is_jammed: Incomplete
    def _update_from_device(self) -> None: ...

DISCOVERY_SCHEMAS: Incomplete
