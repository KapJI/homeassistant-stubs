from .const import DOMAIN as DOMAIN, SIGNAL_EVENTS_CHANGED as SIGNAL_EVENTS_CHANGED, SIGNAL_POSITION_CHANGED as SIGNAL_POSITION_CHANGED
from _typeshed import Incomplete
from astral.location import Elevation as Elevation, Location as Location
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, Platform as Platform, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.sun import get_astral_location as get_astral_location, get_location_astral_event_next as get_location_astral_event_next
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
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
_PHASE_UPDATES: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class Sun(Entity):
    _unrecorded_attributes: Incomplete
    _attr_name: str
    entity_id = ENTITY_ID
    _no_platform_reported: bool
    location: Location
    elevation: Elevation
    next_rising: datetime
    next_setting: datetime
    next_dawn: datetime
    next_dusk: datetime
    next_midnight: datetime
    next_noon: datetime
    solar_elevation: float
    solar_azimuth: float
    rising: bool
    _next_change: datetime
    hass: Incomplete
    phase: Incomplete
    _state_info: Incomplete
    _config_listener: Incomplete
    _update_events_listener: Incomplete
    _update_sun_position_listener: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def update_location(self, _: Event | None = ..., initial: bool = ...) -> None: ...
    def remove_listeners(self) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def _check_event(self, utc_point_in_time: datetime, sun_event: str, before: str | None) -> datetime: ...
    def update_events(self, now: datetime | None = ...) -> None: ...
    def update_sun_position(self, now: datetime | None = ...) -> None: ...
