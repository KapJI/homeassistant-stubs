from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, CONF_APP_KEY as CONF_APP_KEY, DOMAIN as DOMAIN, LOGGER as LOGGER, TYPE_SOLARRADIATION as TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX as TYPE_SOLARRADIATION_LX
from _typeshed import Incomplete
from aioambient import Websocket
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION, ATTR_NAME as ATTR_NAME, CONF_API_KEY as CONF_API_KEY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from typing import Any

PLATFORMS: Incomplete
DATA_CONFIG: str
DEFAULT_SOCKET_MIN_RETRY: int
CONFIG_SCHEMA: Incomplete

def async_wm2_to_lx(value: float) -> int: ...
def async_hydrate_station_data(data: dict[str, Any]) -> dict[str, Any]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AmbientStation:
    _entry: Incomplete
    _entry_setup_complete: bool
    _hass: Incomplete
    _ws_reconnect_delay: Incomplete
    stations: Incomplete
    websocket: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, websocket: Websocket) -> None: ...
    async def ws_connect(self) -> None: ...
    async def ws_disconnect(self) -> None: ...

class AmbientWeatherEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _ambient: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _mac_address: Incomplete
    entity_description: Incomplete
    def __init__(self, ambient: AmbientStation, mac_address: str, station_name: str, description: EntityDescription) -> None: ...
    _attr_available: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
