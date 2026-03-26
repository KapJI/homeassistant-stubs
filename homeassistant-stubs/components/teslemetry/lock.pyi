from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from typing import Any

ENGAGED: str
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryVehicleLockEntity(TeslemetryRootEntity, LockEntity):
    api: Vehicle
    _attr_is_locked: bool
    async def async_lock(self, **kwargs: Any) -> None: ...
    async def async_unlock(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingVehicleLockEntity(TeslemetryVehiclePollingEntity, TeslemetryVehicleLockEntity):
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scoped: bool) -> None: ...
    _attr_is_locked: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingVehicleLockEntity(TeslemetryVehicleStreamEntity, TeslemetryVehicleLockEntity, RestoreEntity):
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scoped: bool) -> None: ...
    _attr_is_locked: bool
    async def async_added_to_hass(self) -> None: ...
    def _callback(self, value: bool | None) -> None: ...

class TeslemetryCableLockEntity(TeslemetryRootEntity, LockEntity):
    api: Vehicle
    async def async_lock(self, **kwargs: Any) -> None: ...
    _attr_is_locked: bool
    async def async_unlock(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingCableLockEntity(TeslemetryVehiclePollingEntity, TeslemetryCableLockEntity):
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scoped: bool) -> None: ...
    _attr_is_locked: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingCableLockEntity(TeslemetryVehicleStreamEntity, TeslemetryCableLockEntity, RestoreEntity):
    scoped: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scoped: bool) -> None: ...
    _attr_is_locked: bool
    async def async_added_to_hass(self) -> None: ...
    def _callback(self, value: str | None) -> None: ...
