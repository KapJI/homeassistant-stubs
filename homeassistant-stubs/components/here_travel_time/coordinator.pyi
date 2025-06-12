from .const import CONF_ARRIVAL_TIME as CONF_ARRIVAL_TIME, CONF_DEPARTURE_TIME as CONF_DEPARTURE_TIME, CONF_DESTINATION_ENTITY_ID as CONF_DESTINATION_ENTITY_ID, CONF_DESTINATION_LATITUDE as CONF_DESTINATION_LATITUDE, CONF_DESTINATION_LONGITUDE as CONF_DESTINATION_LONGITUDE, CONF_ORIGIN_ENTITY_ID as CONF_ORIGIN_ENTITY_ID, CONF_ORIGIN_LATITUDE as CONF_ORIGIN_LATITUDE, CONF_ORIGIN_LONGITUDE as CONF_ORIGIN_LONGITUDE, CONF_ROUTE_MODE as CONF_ROUTE_MODE, DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL, DOMAIN as DOMAIN, ROUTE_MODE_FASTEST as ROUTE_MODE_FASTEST
from .model import HERETravelTimeAPIParams as HERETravelTimeAPIParams, HERETravelTimeData as HERETravelTimeData
from _typeshed import Incomplete
from datetime import datetime, time
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MODE as CONF_MODE, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.location import find_coordinates as find_coordinates
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter
from typing import Any

BACKOFF_MULTIPLIER: float
_LOGGER: Incomplete
type HereConfigEntry = ConfigEntry[HERETransitDataUpdateCoordinator | HERERoutingDataUpdateCoordinator]

class HERERoutingDataUpdateCoordinator(DataUpdateCoordinator[HERETravelTimeData]):
    config_entry: HereConfigEntry
    _api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HereConfigEntry, api_key: str) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> HERETravelTimeData: ...
    def _parse_routing_response(self, response: dict[str, Any]) -> HERETravelTimeData: ...

class HERETransitDataUpdateCoordinator(DataUpdateCoordinator[HERETravelTimeData | None]):
    config_entry: HereConfigEntry
    _api: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: HereConfigEntry, api_key: str) -> None: ...
    update_interval: Incomplete
    async def _async_update_data(self) -> HERETravelTimeData | None: ...
    def _parse_transit_response(self, response: dict[str, Any]) -> HERETravelTimeData: ...

def prepare_parameters(hass: HomeAssistant, config_entry: HereConfigEntry) -> HERETravelTimeAPIParams: ...
def build_hass_attribution(sections: list[dict[str, Any]]) -> str | None: ...
def next_datetime(simple_time: time) -> datetime: ...
