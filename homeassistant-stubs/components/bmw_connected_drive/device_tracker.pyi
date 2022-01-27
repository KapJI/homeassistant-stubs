from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount, BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import ATTR_DIRECTION as ATTR_DIRECTION, CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from homeassistant.components.device_tracker import SOURCE_TYPE_GPS as SOURCE_TYPE_GPS
from homeassistant.components.device_tracker.config_entry import TrackerEntity as TrackerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Literal

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWDeviceTracker(BMWConnectedDriveBaseEntity, TrackerEntity):
    _attr_force_update: bool
    _attr_icon: str
    _attr_unique_id: Any
    _location: Any
    _attr_name: Any
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle) -> None: ...
    @property
    def latitude(self) -> Union[float, None]: ...
    @property
    def longitude(self) -> Union[float, None]: ...
    @property
    def source_type(self) -> Literal['gps']: ...
    _attr_extra_state_attributes: Any
    def update(self) -> None: ...
