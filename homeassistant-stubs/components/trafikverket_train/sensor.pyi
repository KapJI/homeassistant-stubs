from .const import CONF_TIME as CONF_TIME, DOMAIN as DOMAIN
from .coordinator import TVDataUpdateCoordinator as TVDataUpdateCoordinator
from .util import create_unique_id as create_unique_id
from _typeshed import Incomplete
from datetime import time
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_WEEKDAY as CONF_WEEKDAY
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytrafikverket.trafikverket_train import StationInfo as StationInfo

ATTR_DEPARTURE_STATE: str
ATTR_CANCELED: str
ATTR_DELAY_TIME: str
ATTR_PLANNED_TIME: str
ATTR_ESTIMATED_TIME: str
ATTR_ACTUAL_TIME: str
ATTR_OTHER_INFORMATION: str
ATTR_DEVIATIONS: str
ICON: str
SCAN_INTERVAL: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TrainSensor(CoordinatorEntity[TVDataUpdateCoordinator], SensorEntity):
    _attr_icon = ICON
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: TVDataUpdateCoordinator, name: str, from_station: StationInfo, to_station: StationInfo, weekday: list, departuretime: time | None, entry_id: str) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_attr(self) -> None: ...
