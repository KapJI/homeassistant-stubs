from .const import DATA_ACCOUNT as DATA_ACCOUNT, DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN
from aioridwell.client import RidwellAccount as RidwellAccount, RidwellPickupEvent as RidwellPickupEvent
from collections.abc import Mapping
from datetime import date, datetime
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_DATE as DEVICE_CLASS_DATE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_CATEGORY: str
ATTR_PICKUP_STATE: str
ATTR_PICKUP_TYPES: str
ATTR_QUANTITY: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RidwellSensor(CoordinatorEntity, SensorEntity):
    _attr_device_class: Any
    _account: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, account: RidwellAccount) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @property
    def native_value(self) -> Union[StateType, date, datetime]: ...
