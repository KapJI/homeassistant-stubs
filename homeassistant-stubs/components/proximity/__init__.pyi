from .const import ATTR_DIR_OF_TRAVEL as ATTR_DIR_OF_TRAVEL, ATTR_DIST_TO as ATTR_DIST_TO, ATTR_NEAREST as ATTR_NEAREST, CONF_IGNORED_ZONES as CONF_IGNORED_ZONES, CONF_TOLERANCE as CONF_TOLERANCE, CONF_TRACKED_ENTITIES as CONF_TRACKED_ENTITIES, DEFAULT_PROXIMITY_ZONE as DEFAULT_PROXIMITY_ZONE, DEFAULT_TOLERANCE as DEFAULT_TOLERANCE, DOMAIN as DOMAIN, UNITS as UNITS
from .coordinator import ProximityConfigEntry as ProximityConfigEntry, ProximityDataUpdateCoordinator as ProximityDataUpdateCoordinator
from .helpers import entity_used_in as entity_used_in
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_DEVICES as CONF_DEVICES, CONF_NAME as CONF_NAME, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT, CONF_ZONE as CONF_ZONE, Platform as Platform, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.event import async_track_entity_registry_updated_event as async_track_entity_registry_updated_event, async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

_LOGGER: Incomplete
ZONE_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete

async def _async_setup_legacy(hass: HomeAssistant, entry: ProximityConfigEntry, coordinator: ProximityDataUpdateCoordinator) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ProximityConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None: ...

class Proximity(CoordinatorEntity[ProximityDataUpdateCoordinator]):
    _no_platform_reported: bool
    hass: Incomplete
    entity_id: Incomplete
    _attr_name: Incomplete
    _attr_unit_of_measurement: Incomplete
    def __init__(self, hass: HomeAssistant, friendly_name: str, coordinator: ProximityDataUpdateCoordinator) -> None: ...
    @property
    def data(self) -> dict[str, str | int | None]: ...
    @property
    def state(self) -> str | float: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
