from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryRootEntity as TeslemetryRootEntity, TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity, CoverEntityFeature as CoverEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from tesla_fleet_api.const import Scope
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from typing import Any

OPEN: int
CLOSED: int
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CoverRestoreEntity(RestoreEntity, CoverEntity):
    _attr_is_closed: bool
    async def async_added_to_hass(self) -> None: ...

class TeslemetryWindowEntity(TeslemetryRootEntity, CoverEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: bool
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingWindowEntity(TeslemetryVehiclePollingEntity, TeslemetryWindowEntity, CoverEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_is_closed: bool
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingWindowEntity(TeslemetryVehicleStreamEntity, TeslemetryWindowEntity, CoverRestoreEntity):
    fd: bool | None
    fp: bool | None
    rd: bool | None
    rp: bool | None
    scoped: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: Incomplete
    def __init__(self, data: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _handle_stream_update(self, data: dict[str, Any]) -> None: ...

class TeslemetryChargePortEntity(TeslemetryRootEntity, CoverEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: bool
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingChargePortEntity(TeslemetryVehiclePollingEntity, TeslemetryChargePortEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_is_closed: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingChargePortEntity(TeslemetryVehicleStreamEntity, TeslemetryChargePortEntity, CoverRestoreEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_value_from_stream(self, value: bool | None) -> None: ...

class TeslemetryFrontTrunkEntity(TeslemetryRootEntity, CoverEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: bool
    async def async_open_cover(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingFrontTrunkEntity(TeslemetryVehiclePollingEntity, TeslemetryFrontTrunkEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_is_closed: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingFrontTrunkEntity(TeslemetryVehicleStreamEntity, TeslemetryFrontTrunkEntity, CoverRestoreEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_value_from_stream(self, value: bool | None) -> None: ...

class TeslemetryRearTrunkEntity(TeslemetryRootEntity, CoverEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: bool
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...

class TeslemetryVehiclePollingRearTrunkEntity(TeslemetryVehiclePollingEntity, TeslemetryRearTrunkEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_is_closed: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingRearTrunkEntity(TeslemetryVehicleStreamEntity, TeslemetryRearTrunkEntity, CoverRestoreEntity):
    scoped: Incomplete
    _attr_supported_features: Incomplete
    _attr_is_closed: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _async_value_from_stream(self, value: bool | None) -> None: ...

class TeslemetrySunroofEntity(TeslemetryVehiclePollingEntity, CoverEntity):
    api: Vehicle
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_entity_registry_enabled_default: bool
    scoped: Incomplete
    def __init__(self, vehicle: TeslemetryVehicleData, scopes: list[Scope]) -> None: ...
    _attr_is_closed: Incomplete
    _attr_current_cover_position: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
