from homeassistant.components.sensor import PLATFORM_SCHEMA as PLATFORM_SCHEMA, SensorEntity as SensorEntity
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, CONF_METHOD as CONF_METHOD, CONF_NAME as CONF_NAME, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN, TIME_DAYS as TIME_DAYS, TIME_HOURS as TIME_HOURS, TIME_MINUTES as TIME_MINUTES, TIME_SECONDS as TIME_SECONDS
from homeassistant.core import callback as callback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any, Optional

ATTR_SOURCE_ID: str
CONF_SOURCE_SENSOR: str
CONF_ROUND_DIGITS: str
CONF_UNIT_PREFIX: str
CONF_UNIT_TIME: str
CONF_UNIT_OF_MEASUREMENT: str
TRAPEZOIDAL_METHOD: str
LEFT_METHOD: str
RIGHT_METHOD: str
INTEGRATION_METHOD: Any
UNIT_PREFIXES: Any
UNIT_TIME: Any
ICON: str
DEFAULT_ROUND: int

async def async_setup_platform(hass: Any, config: Any, async_add_entities: Any, discovery_info: Optional[Any] = ...) -> None: ...

class IntegrationSensor(RestoreEntity, SensorEntity):
    def __init__(self, source_entity: Any, name: Any, round_digits: Any, unit_prefix: Any, unit_time: Any, unit_of_measurement: Any, integration_method: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def name(self): ...
    @property
    def state(self): ...
    @property
    def unit_of_measurement(self): ...
    @property
    def should_poll(self): ...
    @property
    def extra_state_attributes(self): ...
    @property
    def icon(self): ...