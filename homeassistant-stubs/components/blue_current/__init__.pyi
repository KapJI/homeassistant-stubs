from .const import CHARGEPOINT_SETTINGS as CHARGEPOINT_SETTINGS, CHARGEPOINT_STATUS as CHARGEPOINT_STATUS, DOMAIN as DOMAIN, EVSE_ID as EVSE_ID, LOGGER as LOGGER, PLUG_AND_CHARGE as PLUG_AND_CHARGE, VALUE as VALUE
from _typeshed import Incomplete
from bluecurrent_api import Client
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_TOKEN as CONF_API_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

type BlueCurrentConfigEntry = ConfigEntry[Connector]
PLATFORMS: Incomplete
CHARGE_POINTS: str
DATA: str
DELAY: int
GRID: str
OBJECT: str
VALUE_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: BlueCurrentConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, config_entry: BlueCurrentConfigEntry) -> bool: ...

class Connector:
    config: Incomplete
    hass: Incomplete
    client: Incomplete
    charge_points: dict[str, dict]
    grid: dict[str, Any]
    def __init__(self, hass: HomeAssistant, config: BlueCurrentConfigEntry, client: Client) -> None: ...
    async def on_data(self, message: dict) -> None: ...
    async def handle_charge_point_data(self, charge_points_data: list) -> None: ...
    async def handle_charge_point(self, evse_id: str, charge_point: dict[str, Any]) -> None: ...
    def add_charge_point(self, evse_id: str, charge_point: dict[str, Any]) -> None: ...
    def update_charge_point(self, evse_id: str, update_type: str, data: dict) -> None: ...
    def dispatch_charge_point_update_signal(self, evse_id: str) -> None: ...
    def dispatch_grid_update_signal(self) -> None: ...
    async def on_open(self) -> None: ...
    async def run_task(self) -> None: ...
    def _on_disconnect(self) -> None: ...
    async def _disconnect(self) -> None: ...
    @property
    def connected(self) -> bool: ...
