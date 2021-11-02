from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, CONF_APP_KEY as CONF_APP_KEY, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN, LOGGER as LOGGER, TYPE_SOLARRADIATION as TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX as TYPE_SOLARRADIATION_LX
from aioambient import Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION, ATTR_NAME as ATTR_NAME, CONF_API_KEY as CONF_API_KEY, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.event import async_call_later as async_call_later
from typing import Any

PLATFORMS: Any
DATA_CONFIG: str
DEFAULT_SOCKET_MIN_RETRY: int
CONFIG_SCHEMA: Any

def async_wm2_to_lx(value: float) -> int: ...
def async_hydrate_station_data(data: dict[str, Any]) -> dict[str, Any]: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class AmbientStation:
    _config_entry: Any
    _entry_setup_complete: bool
    _hass: Any
    _ws_reconnect_delay: Any
    client: Any
    stations: Any
    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry, client: Client) -> None: ...
    async def _attempt_connect(self) -> None: ...
    async def ws_connect(self) -> None: ...
    async def ws_disconnect(self) -> None: ...

class AmbientWeatherEntity(Entity):
    _attr_should_poll: bool
    _ambient: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    _mac_address: Any
    entity_description: Any
    def __init__(self, ambient: AmbientStation, mac_address: str, station_name: str, description: EntityDescription) -> None: ...
    _attr_available: Any
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...
