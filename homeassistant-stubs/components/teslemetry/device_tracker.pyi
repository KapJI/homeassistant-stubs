from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryVehiclePollingEntity as TeslemetryVehiclePollingEntity, TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.device_tracker import TrackerEntity as TrackerEntity, TrackerEntityDescription as TrackerEntityDescription
from homeassistant.const import STATE_HOME as STATE_HOME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from teslemetry_stream import TeslemetryStreamVehicle as TeslemetryStreamVehicle
from teslemetry_stream.const import TeslaLocation as TeslaLocation

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TeslemetryDeviceTrackerEntityDescription(TrackerEntityDescription):
    value_listener: Callable[[TeslemetryStreamVehicle, Callable[[TeslaLocation | None], None]], Callable[[], None]]
    name_listener: Callable[[TeslemetryStreamVehicle, Callable[[str | None], None]], Callable[[], None]] | None = ...
    streaming_firmware: str
    polling_prefix: str | None = ...

DESCRIPTIONS: tuple[TeslemetryDeviceTrackerEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryVehiclePollingDeviceTrackerEntity(TeslemetryVehiclePollingEntity, TrackerEntity):
    entity_description: TeslemetryDeviceTrackerEntityDescription
    def __init__(self, vehicle: TeslemetryVehicleData, description: TeslemetryDeviceTrackerEntityDescription) -> None: ...
    _attr_latitude: Incomplete
    _attr_longitude: Incomplete
    _attr_location_name: Incomplete
    _attr_available: Incomplete
    def _async_update_attrs(self) -> None: ...

class TeslemetryStreamingDeviceTrackerEntity(TeslemetryVehicleStreamEntity, TrackerEntity, RestoreEntity):
    entity_description: TeslemetryDeviceTrackerEntityDescription
    def __init__(self, vehicle: TeslemetryVehicleData, description: TeslemetryDeviceTrackerEntityDescription) -> None: ...
    _attr_latitude: Incomplete
    _attr_longitude: Incomplete
    _attr_location_name: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _location_callback(self, location: TeslaLocation | None) -> None: ...
    def _name_callback(self, name: str | None) -> None: ...
