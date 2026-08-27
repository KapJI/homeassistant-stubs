import asyncio
from . import IseoConfigEntry as IseoConfigEntry
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.bluetooth import async_ble_device_from_address as async_ble_device_from_address
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from iseo_argo_ble import IseoClient as IseoClient, LockState as LockState
from typing import Any, override

_LOGGER: Incomplete
PARALLEL_UPDATES: int
_RELOCK_DELAY: int
_RELOCK_POLL_DELAY: int
_POLL_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IseoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IseoLockEntity(LockEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _entry: Incomplete
    _relock_task: asyncio.Task[None] | None
    _ble_lock: Incomplete
    _door_status_supported: bool | None
    _fw_version_set: bool
    client: IseoClient
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_is_locked: bool | None
    _attr_is_unlocking: bool
    _attr_available: bool
    _poll_suppress_until: datetime | None
    def __init__(self, entry: IseoConfigEntry) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    async def _async_poll_interval(self, _now: datetime) -> None: ...
    def _cancel_relock_task(self) -> None: ...
    def _set_available(self, available: bool, reason: object = None) -> None: ...
    def _update_firmware_version(self, state: LockState) -> None: ...
    _attr_assumed_state: bool
    async def _poll_state(self, force: bool = False) -> bool: ...
    def _set_unlocking(self, available: bool = True) -> None: ...
    def _set_unlocked(self, available: bool = True) -> None: ...
    def _set_locked(self, available: bool = True) -> None: ...
    async def _auto_relock(self) -> None: ...
    @override
    async def async_lock(self, **kwargs: Any) -> None: ...
    @override
    async def async_unlock(self, **kwargs: Any) -> None: ...
