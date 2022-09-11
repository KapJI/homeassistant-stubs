from . import RidwellData as RidwellData, RidwellEntity as RidwellEntity
from .const import DOMAIN as DOMAIN, SENSOR_TYPE_NEXT_PICKUP as SENSOR_TYPE_NEXT_PICKUP
from _typeshed import Incomplete
from aioridwell.model import RidwellAccount as RidwellAccount, RidwellPickupEvent as RidwellPickupEvent
from collections.abc import Mapping
from datetime import date, datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_CATEGORY: str
ATTR_PICKUP_STATE: str
ATTR_PICKUP_TYPES: str
ATTR_QUANTITY: str
SENSOR_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RidwellSensor(RidwellEntity, SensorEntity):
    _attr_name: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, account: RidwellAccount, description: SensorEntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def native_value(self) -> Union[StateType, date, datetime]: ...
