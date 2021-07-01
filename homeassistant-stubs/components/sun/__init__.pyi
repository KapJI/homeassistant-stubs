from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.sun import get_astral_location as get_astral_location, get_location_astral_event_next as get_location_astral_event_next
from typing import Any

_LOGGER: Any
DOMAIN: str
ENTITY_ID: str
STATE_ABOVE_HORIZON: str
STATE_BELOW_HORIZON: str
STATE_ATTR_AZIMUTH: str
STATE_ATTR_ELEVATION: str
STATE_ATTR_RISING: str
STATE_ATTR_NEXT_DAWN: str
STATE_ATTR_NEXT_DUSK: str
STATE_ATTR_NEXT_MIDNIGHT: str
STATE_ATTR_NEXT_NOON: str
STATE_ATTR_NEXT_RISING: str
STATE_ATTR_NEXT_SETTING: str
PHASE_NIGHT: str
PHASE_ASTRONOMICAL_TWILIGHT: str
PHASE_NAUTICAL_TWILIGHT: str
PHASE_TWILIGHT: str
PHASE_SMALL_DAY: str
PHASE_DAY: str
_PHASE_UPDATES: Any

async def async_setup(hass, config): ...

class Sun(Entity):
    entity_id: Any
    hass: Any
    location: Any
    elevation: float
    _state: Any
    next_dawn: Any
    next_midnight: Any
    solar_elevation: Any
    rising: Any
    _next_change: Any
    def __init__(self, hass) -> None: ...
    @property
    def name(self): ...
    @property
    def state(self): ...
    @property
    def extra_state_attributes(self): ...
    phase: Any
    def _check_event(self, utc_point_in_time, sun_event, before): ...
    next_rising: Any
    next_noon: Any
    next_setting: Any
    next_dusk: Any
    def update_events(self, now: Any | None = ...) -> None: ...
    solar_azimuth: Any
    def update_sun_position(self, now: Any | None = ...) -> None: ...
