from .entity import VictronBaseEntity as VictronBaseEntity
from .hub import VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.device_tracker import SourceType as SourceType, TrackerEntity as TrackerEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any
from victron_mqtt import Device as VictronVenusDevice, GpsLocation, Metric as VictronVenusMetric

PARALLEL_UPDATES: int
ATTR_ALTITUDE: str
ATTR_COURSE: str
ATTR_SPEED: str

async def async_setup_entry(hass: HomeAssistant, config_entry: VictronGxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VictronDeviceTracker(VictronBaseEntity, TrackerEntity):
    _attr_source_type: Incomplete
    _altitude: float | None
    _course: float | None
    _speed: float | None
    def __init__(self, device: VictronVenusDevice, metric: VictronVenusMetric, device_info: DeviceInfo, installation_id: str) -> None: ...
    @callback
    def _on_update_cb(self, value: Any) -> None: ...
    _attr_latitude: Incomplete
    _attr_longitude: Incomplete
    def _update_from_location(self, value: GpsLocation | None) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, StateType]: ...
