from .const import ATTR_DIR_OF_TRAVEL as ATTR_DIR_OF_TRAVEL, ATTR_NEAREST as ATTR_NEAREST, CONF_IGNORED_ZONES as CONF_IGNORED_ZONES, CONF_TOLERANCE as CONF_TOLERANCE, DEFAULT_PROXIMITY_ZONE as DEFAULT_PROXIMITY_ZONE, DEFAULT_TOLERANCE as DEFAULT_TOLERANCE, DOMAIN as DOMAIN, UNITS as UNITS
from .coordinator import ProximityDataUpdateCoordinator as ProximityDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.const import CONF_DEVICES as CONF_DEVICES, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.event import async_track_state_change as async_track_state_change
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ZONE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class Proximity(CoordinatorEntity[ProximityDataUpdateCoordinator]):
    _no_platform_reported: bool
    hass: Incomplete
    entity_id: Incomplete
    _attr_name: Incomplete
    _attr_unit_of_measurement: Incomplete
    def __init__(self, hass: HomeAssistant, friendly_name: str, coordinator: ProximityDataUpdateCoordinator) -> None: ...
    @property
    def state(self) -> str | int | float: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
