from .const import CONF_PLAY_MEDIA_APP_ID as CONF_PLAY_MEDIA_APP_ID, DEFAULT_PLAY_MEDIA_APP_ID as DEFAULT_PLAY_MEDIA_APP_ID, DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.debounce import Debouncer as Debouncer
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from homeassistant.util.dt import utcnow as utcnow
from rokuecp import Roku
from rokuecp.models import Device

REQUEST_REFRESH_DELAY: float
SCAN_INTERVAL: Incomplete
_LOGGER: Incomplete
type RokuConfigEntry = ConfigEntry[RokuDataUpdateCoordinator]

class RokuDataUpdateCoordinator(DataUpdateCoordinator[Device]):
    config_entry: RokuConfigEntry
    last_full_update: datetime | None
    roku: Roku
    device_id: Incomplete
    play_media_app_id: Incomplete
    full_update_interval: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: RokuConfigEntry) -> None: ...
    async def _async_update_data(self) -> Device: ...
