from .const import ATTR_DIR_OF_TRAVEL as ATTR_DIR_OF_TRAVEL, ATTR_DIST_TO as ATTR_DIST_TO, ATTR_IN_IGNORED_ZONE as ATTR_IN_IGNORED_ZONE, ATTR_NEAREST as ATTR_NEAREST, CONF_IGNORED_ZONES as CONF_IGNORED_ZONES, CONF_TOLERANCE as CONF_TOLERANCE, CONF_TRACKED_ENTITIES as CONF_TRACKED_ENTITIES, DEFAULT_DIR_OF_TRAVEL as DEFAULT_DIR_OF_TRAVEL, DEFAULT_DIST_TO_ZONE as DEFAULT_DIST_TO_ZONE, DEFAULT_NEAREST as DEFAULT_NEAREST, DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, ATTR_NAME as ATTR_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, EventType as EventType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from homeassistant.util.location import distance as distance
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter

_LOGGER: Incomplete

@dataclass
class StateChangedData:
    entity_id: str
    old_state: State | None
    new_state: State | None
    def __init__(self, entity_id, old_state, new_state) -> None: ...

@dataclass
class ProximityData:
    proximity: dict[str, str | int | None]
    entities: dict[str, dict[str, str | int | None]]
    def __init__(self, proximity, entities) -> None: ...

DEFAULT_PROXIMITY_DATA: dict[str, str | int | None]

class ProximityDataUpdateCoordinator(DataUpdateCoordinator[ProximityData]):
    config_entry: ConfigEntry
    ignored_zone_ids: Incomplete
    tracked_entities: Incomplete
    tolerance: Incomplete
    proximity_zone_id: Incomplete
    proximity_zone_name: Incomplete
    unit_of_measurement: Incomplete
    entity_mapping: Incomplete
    data: Incomplete
    state_change_data: Incomplete
    def __init__(self, hass: HomeAssistant, friendly_name: str, config: ConfigType) -> None: ...
    def async_add_entity_mapping(self, tracked_entity_id: str, entity_id: str) -> None: ...
    async def async_check_proximity_state_change(self, entity: str, old_state: State | None, new_state: State | None) -> None: ...
    async def async_check_tracked_entity_change(self, event: EventType[er.EventEntityRegistryUpdatedData]) -> None: ...
    def convert_legacy(self, value: float | str) -> float | str: ...
    def _calc_distance_to_zone(self, zone: State, device: State, latitude: float | None, longitude: float | None) -> int | None: ...
    def _calc_direction_of_travel(self, zone: State, device: State, old_latitude: float | None, old_longitude: float | None, new_latitude: float | None, new_longitude: float | None) -> str | None: ...
    async def _async_update_data(self) -> ProximityData: ...
    def _create_removed_tracked_entity_issue(self, entity_id: str) -> None: ...
