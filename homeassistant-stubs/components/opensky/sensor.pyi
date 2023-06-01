from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_RADIUS as CONF_RADIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from python_opensky import BoundingBox as BoundingBox, OpenSky, StateVector as StateVector

CONF_ALTITUDE: str
ATTR_ICAO24: str
ATTR_CALLSIGN: str
ATTR_ALTITUDE: str
ATTR_ON_GROUND: str
ATTR_SENSOR: str
ATTR_STATES: str
DOMAIN: str
DEFAULT_ALTITUDE: int
EVENT_OPENSKY_ENTRY: Incomplete
EVENT_OPENSKY_EXIT: Incomplete
SCAN_INTERVAL: Incomplete
OPENSKY_API_URL: str
OPENSKY_API_FIELDS: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class OpenSkySensor(SensorEntity):
    _attr_attribution: str
    _altitude: Incomplete
    _state: int
    _hass: Incomplete
    _name: Incomplete
    _previously_tracked: Incomplete
    _opensky: Incomplete
    _bounding_box: Incomplete
    def __init__(self, hass: HomeAssistant, name: str, opensky: OpenSky, bounding_box: BoundingBox, altitude: float) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> int: ...
    def _handle_boundary(self, flights: set[str], event: str, metadata: dict[str, StateVector]) -> None: ...
    async def async_update(self) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def icon(self) -> str: ...
