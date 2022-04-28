from . import BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import DOMAIN as DOMAIN
from .coordinator import BMWDataUpdateCoordinator as BMWDataUpdateCoordinator
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

DOOR_LOCK_STATE: str
_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BMWLock(BMWConnectedDriveBaseEntity, LockEntity):
    _attribute: Any
    _attr_name: Any
    _attr_unique_id: Any
    _sensor_name: Any
    door_lock_state_available: Any
    def __init__(self, coordinator: BMWDataUpdateCoordinator, vehicle: ConnectedDriveVehicle, attribute: str, sensor_name: str) -> None: ...
    _attr_is_locked: bool
    def lock(self, **kwargs: Any) -> None: ...
    def unlock(self, **kwargs: Any) -> None: ...
    _attr_extra_state_attributes: Any
    def _handle_coordinator_update(self) -> None: ...
