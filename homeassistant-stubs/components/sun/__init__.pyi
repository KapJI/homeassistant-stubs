from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_ELEVATION as CONF_ELEVATION, EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, SUN_EVENT_SUNRISE as SUN_EVENT_SUNRISE, SUN_EVENT_SUNSET as SUN_EVENT_SUNSET
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import event as event
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.integration_platform import async_process_integration_platform_for_component as async_process_integration_platform_for_component
from homeassistant.helpers.sun import get_astral_location as get_astral_location, get_location_astral_event_next as get_location_astral_event_next
from homeassistant.helpers.typing import ConfigType as ConfigType

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

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class Sun(Entity):
    entity_id: Incomplete
    hass: Incomplete
    location: Incomplete
    elevation: float
    _state: Incomplete
    next_dawn: Incomplete
    next_midnight: Incomplete
    solar_elevation: Incomplete
    rising: Incomplete
    _next_change: Incomplete
    _config_listener: Incomplete
    _update_events_listener: Incomplete
    _update_sun_position_listener: Incomplete
    def __init__(self, hass) -> None: ...
    def update_location(self, *_) -> None: ...
    def remove_listeners(self) -> None: ...
    @property
    def name(self): ...
    @property
    def state(self): ...
    @property
    def extra_state_attributes(self): ...
    phase: Incomplete
    def _check_event(self, utc_point_in_time, sun_event, before): ...
    next_rising: Incomplete
    next_noon: Incomplete
    next_setting: Incomplete
    next_dusk: Incomplete
    def update_events(self, now: Incomplete | None = ...) -> None: ...
    solar_azimuth: Incomplete
    def update_sun_position(self, now: Incomplete | None = ...) -> None: ...
