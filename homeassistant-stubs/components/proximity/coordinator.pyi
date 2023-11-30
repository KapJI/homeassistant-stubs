from .const import CONF_IGNORED_ZONES as CONF_IGNORED_ZONES, CONF_TOLERANCE as CONF_TOLERANCE, DEFAULT_DIR_OF_TRAVEL as DEFAULT_DIR_OF_TRAVEL, DEFAULT_DIST_TO_ZONE as DEFAULT_DIST_TO_ZONE, DEFAULT_NEAREST as DEFAULT_NEAREST
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_DEVICES as CONF_DEVICES, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.location import distance as distance
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter
from typing import TypedDict

_LOGGER: Incomplete

@dataclass
class StateChangedData:
    entity_id: str
    old_state: State | None
    new_state: State | None
    def __init__(self, entity_id, old_state, new_state) -> None: ...

class ProximityData(TypedDict):
    dist_to_zone: str | float
    dir_of_travel: str | float
    nearest: str | float

class ProximityDataUpdateCoordinator(DataUpdateCoordinator[ProximityData]):
    ignored_zones: Incomplete
    proximity_devices: Incomplete
    tolerance: Incomplete
    proximity_zone: Incomplete
    unit_of_measurement: Incomplete
    friendly_name: Incomplete
    data: Incomplete
    state_change_data: Incomplete
    def __init__(self, hass: HomeAssistant, friendly_name: str, config: ConfigType) -> None: ...
    async def async_check_proximity_state_change(self, entity: str, old_state: State | None, new_state: State | None) -> None: ...
    async def _async_update_data(self) -> ProximityData: ...
