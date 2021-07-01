from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONF_DEVICES as CONF_DEVICES, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE, LENGTH_FEET as LENGTH_FEET, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_METERS as LENGTH_METERS, LENGTH_MILES as LENGTH_MILES, LENGTH_YARD as LENGTH_YARD
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import track_state_change as track_state_change
from homeassistant.util.distance import convert as convert
from homeassistant.util.location import distance as distance
from typing import Any

_LOGGER: Any
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
UNITS: Any
ZONE_SCHEMA: Any
CONFIG_SCHEMA: Any

def setup_proximity_component(hass, name, config): ...
def setup(hass, config): ...

class Proximity(Entity):
    hass: Any
    friendly_name: Any
    dist_to: Any
    dir_of_travel: Any
    nearest: Any
    ignored_zones: Any
    proximity_devices: Any
    tolerance: Any
    proximity_zone: Any
    _unit_of_measurement: Any
    def __init__(self, hass, zone_friendly_name, dist_to, dir_of_travel, nearest, ignored_zones, proximity_devices, tolerance, proximity_zone, unit_of_measurement) -> None: ...
    @property
    def name(self): ...
    @property
    def state(self): ...
    @property
    def unit_of_measurement(self): ...
    @property
    def extra_state_attributes(self): ...
    def check_proximity_state_change(self, entity, old_state, new_state) -> None: ...
