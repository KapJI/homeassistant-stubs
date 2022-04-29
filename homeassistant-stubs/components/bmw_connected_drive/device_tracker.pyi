from . import BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import ATTR_DIRECTION as ATTR_DIRECTION, DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from _typeshed import Incomplete
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from homeassistant.components.device_tracker import SOURCE_TYPE_GPS as SOURCE_TYPE_GPS
from homeassistant.components.device_tracker.config_entry import TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Literal

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWDeviceTracker(BMWConnectedDriveBaseEntity, TrackerEntity):
    _attr_force_update: bool
    _attr_icon: str
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: ConnectedDriveVehicle) -> None: ...
    @property
    def extra_state_attributes(self) -> dict: ...
    @property
    def latitude(self) -> Union[float, None]: ...
    @property
    def longitude(self) -> Union[float, None]: ...
    @property
    def source_type(self) -> Literal['gps']: ...
