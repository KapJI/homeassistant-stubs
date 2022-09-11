from . import local_auth as local_auth
from .const import DATA_NEST as DATA_NEST, DATA_NEST_CONFIG as DATA_NEST_CONFIG, DOMAIN as DOMAIN, SIGNAL_NEST_UPDATE as SIGNAL_NEST_UPDATE
from _typeshed import Incomplete
from collections.abc import Generator
from homeassistant import config_entries as config_entries
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET, CONF_FILENAME as CONF_FILENAME, CONF_STRUCTURE as CONF_STRUCTURE, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, dispatcher_send as dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity

_CONFIGURING: Incomplete
_LOGGER: Incomplete
PLATFORMS: Incomplete
SERVICE_CANCEL_ETA: str
SERVICE_SET_ETA: str
NEST_CONFIG_FILE: str
ATTR_ETA: str
ATTR_ETA_WINDOW: str
ATTR_STRUCTURE: str
ATTR_TRIP_ID: str
AWAY_MODE_AWAY: str
AWAY_MODE_HOME: str
ATTR_AWAY_MODE: str
SERVICE_SET_AWAY_MODE: str
SET_AWAY_MODE_SCHEMA: Incomplete
SET_ETA_SCHEMA: Incomplete
CANCEL_ETA_SCHEMA: Incomplete

def nest_update_event_broker(hass, nest) -> None: ...
async def async_setup_legacy(hass: HomeAssistant, config: dict) -> bool: ...
async def async_setup_legacy_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NestLegacyDevice:
    hass: Incomplete
    nest: Incomplete
    local_structure: Incomplete
    def __init__(self, hass, conf, nest) -> None: ...
    def initialize(self): ...
    def structures(self) -> Generator[Incomplete, None, None]: ...
    def thermostats(self): ...
    def smoke_co_alarms(self): ...
    def cameras(self): ...
    def _devices(self, device_type) -> Generator[Incomplete, None, None]: ...

class NestSensorDevice(Entity):
    _attr_should_poll: bool
    structure: Incomplete
    variable: Incomplete
    device: Incomplete
    _name: Incomplete
    _state: Incomplete
    _unit: Incomplete
    def __init__(self, structure, device, variable) -> None: ...
    @property
    def name(self): ...
    @property
    def unique_id(self): ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
