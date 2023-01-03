from _typeshed import Incomplete
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_DEVICES as CONF_DEVICES, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE, UnitOfLength as UnitOfLength
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import track_state_change as track_state_change
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.location import distance as distance
from homeassistant.util.unit_conversion import DistanceConverter as DistanceConverter

_LOGGER: Incomplete
ATTR_DIR_OF_TRAVEL: str
ATTR_DIST_FROM: str
ATTR_NEAREST: str
CONF_IGNORED_ZONES: str
CONF_TOLERANCE: str
DEFAULT_DIR_OF_TRAVEL: str
DEFAULT_DIST_TO_ZONE: str
DEFAULT_NEAREST: str
DEFAULT_PROXIMITY_ZONE: str
DEFAULT_TOLERANCE: int
DOMAIN: str
UNITS: Incomplete
ZONE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

def setup_proximity_component(hass: HomeAssistant, name: str, config: ConfigType) -> bool: ...
def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class Proximity(Entity):
    hass: Incomplete
    friendly_name: Incomplete
    dist_to: Incomplete
    dir_of_travel: Incomplete
    nearest: Incomplete
    ignored_zones: Incomplete
    proximity_devices: Incomplete
    tolerance: Incomplete
    proximity_zone: Incomplete
    _unit_of_measurement: Incomplete
    def __init__(self, hass: HomeAssistant, zone_friendly_name: str, dist_to: str, dir_of_travel: str, nearest: str, ignored_zones: list[str], proximity_devices: list[str], tolerance: int, proximity_zone: str, unit_of_measurement: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def state(self) -> Union[str, int]: ...
    @property
    def unit_of_measurement(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    def check_proximity_state_change(self, entity: str, old_state: Union[State, None], new_state: Union[State, None]) -> None: ...
