from .const import ATTR_ALTITUDE as ATTR_ALTITUDE, ATTR_CALLSIGN as ATTR_CALLSIGN, ATTR_ICAO24 as ATTR_ICAO24, ATTR_SENSOR as ATTR_SENSOR, CLIENT as CLIENT, CONF_ALTITUDE as CONF_ALTITUDE, DEFAULT_ALTITUDE as DEFAULT_ALTITUDE, DOMAIN as DOMAIN, EVENT_OPENSKY_ENTRY as EVENT_OPENSKY_ENTRY, EVENT_OPENSKY_EXIT as EVENT_OPENSKY_EXIT
from _typeshed import Incomplete
from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE, CONF_NAME as CONF_NAME, CONF_RADIUS as CONF_RADIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from python_opensky import BoundingBox as BoundingBox, OpenSky, StateVector as StateVector

SCAN_INTERVAL: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OpenSkySensor(SensorEntity):
    _attr_attribution: str
    _altitude: Incomplete
    _state: int
    _name: Incomplete
    _previously_tracked: Incomplete
    _opensky: Incomplete
    _bounding_box: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, opensky: OpenSky, bounding_box: BoundingBox, altitude: float, entry_id: str) -> None: ...
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
