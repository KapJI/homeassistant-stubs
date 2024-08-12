from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from aionotion.bridge.models import Bridge as Bridge
from aionotion.client import Client as Client
from aionotion.listener.models import Listener as Listener
from aionotion.sensor.models import Sensor as Sensor
from aionotion.user.models import UserPreferences as UserPreferences
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

DATA_BRIDGES: str
DATA_LISTENERS: str
DATA_SENSORS: str
DATA_USER_PREFERENCES: str
DEFAULT_SCAN_INTERVAL: Incomplete

def _async_register_new_bridge(hass: HomeAssistant, entry: ConfigEntry, bridge: Bridge) -> None: ...

@dataclass
class NotionData:
    hass: HomeAssistant
    entry: ConfigEntry
    bridges: dict[int, Bridge] = ...
    listeners: dict[str, Listener] = ...
    sensors: dict[str, Sensor] = ...
    user_preferences: UserPreferences | None = ...
    def update_bridges(self, bridges: list[Bridge]) -> None: ...
    def update_listeners(self, listeners: list[Listener]) -> None: ...
    def update_sensors(self, sensors: list[Sensor]) -> None: ...
    def update_user_preferences(self, user_preferences: UserPreferences) -> None: ...
    def asdict(self) -> dict[str, Any]: ...
    def __init__(self, hass, entry, bridges=..., listeners=..., sensors=..., user_preferences=...) -> None: ...

class NotionDataUpdateCoordinator(DataUpdateCoordinator[NotionData]):
    config_entry: ConfigEntry
    _client: Incomplete
    _entry: Incomplete
    def __init__(self, hass: HomeAssistant, *, entry: ConfigEntry, client: Client) -> None: ...
    async def _async_update_data(self) -> NotionData: ...
