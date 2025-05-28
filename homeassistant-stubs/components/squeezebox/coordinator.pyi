from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import DOMAIN as DOMAIN, PLAYER_UPDATE_INTERVAL as PLAYER_UPDATE_INTERVAL, SENSOR_UPDATE_INTERVAL as SENSOR_UPDATE_INTERVAL, SIGNAL_PLAYER_REDISCOVERED as SIGNAL_PLAYER_REDISCOVERED, STATUS_API_TIMEOUT as STATUS_API_TIMEOUT
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pysqueezebox import Player as Player, Server as Server
from pysqueezebox.player import Alarm as Alarm
from typing import Any

_LOGGER: Incomplete

class LMSStatusDataUpdateCoordinator(DataUpdateCoordinator):
    config_entry: SqueezeboxConfigEntry
    lms: Incomplete
    can_server_restart: bool
    def __init__(self, hass: HomeAssistant, config_entry: SqueezeboxConfigEntry, lms: Server) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict: ...

class SqueezeBoxPlayerUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    config_entry: SqueezeboxConfigEntry
    player: Incomplete
    available: bool
    known_alarms: set[str]
    _remove_dispatcher: Callable | None
    player_uuid: Incomplete
    server_uuid: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: SqueezeboxConfigEntry, player: Player, server_uuid: str) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
    @callback
    def rediscovered(self, unique_id: str, connected: bool) -> None: ...
