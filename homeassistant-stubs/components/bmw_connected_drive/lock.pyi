from . import BMWConnectedDriveAccount as BMWConnectedDriveAccount, BMWConnectedDriveBaseEntity as BMWConnectedDriveBaseEntity
from .const import CONF_ACCOUNT as CONF_ACCOUNT, DATA_ENTRIES as DATA_ENTRIES
from bimmer_connected.vehicle import ConnectedDriveVehicle as ConnectedDriveVehicle
from homeassistant.components.lock import LockEntity as LockEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
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
    def __init__(self, account: BMWConnectedDriveAccount, vehicle: ConnectedDriveVehicle, attribute: str, sensor_name: str) -> None: ...
    _attr_is_locked: bool
    def lock(self, **kwargs: Any) -> None: ...
    def unlock(self, **kwargs: Any) -> None: ...
    _attr_extra_state_attributes: Any
    def update(self) -> None: ...
