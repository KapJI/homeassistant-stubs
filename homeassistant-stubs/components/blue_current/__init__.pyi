from .const import DOMAIN as DOMAIN, EVSE_ID as EVSE_ID, LOGGER as LOGGER, MODEL_TYPE as MODEL_TYPE
from _typeshed import Incomplete
from bluecurrent_api import Client
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME, CONF_API_TOKEN as CONF_API_TOKEN, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later

PLATFORMS: Incomplete
CHARGE_POINTS: str
DATA: str
SMALL_DELAY: int
LARGE_DELAY: int
GRID: str
OBJECT: str
VALUE_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool: ...

class Connector:
    config: Incomplete
    hass: Incomplete
    client: Incomplete
    charge_points: Incomplete
    grid: Incomplete
    available: bool
    def __init__(self, hass: HomeAssistant, config: ConfigEntry, client: Client) -> None: ...
    async def connect(self, token: str) -> None: ...
    async def on_data(self, message: dict) -> None: ...
    async def handle_charge_point_data(self, charge_points_data: list) -> None: ...
    async def handle_charge_point(self, evse_id: str, model: str, name: str) -> None: ...
    def add_charge_point(self, evse_id: str, model: str, name: str) -> None: ...
    def update_charge_point(self, evse_id: str, data: dict) -> None: ...
    def dispatch_value_update_signal(self, evse_id: str) -> None: ...
    def dispatch_grid_update_signal(self) -> None: ...
    async def start_loop(self) -> None: ...
    async def reconnect(self, _event_time: datetime | None = None) -> None: ...
    async def disconnect(self) -> None: ...
