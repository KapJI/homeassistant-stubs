import datetime
from .const import INVALID_AUTH_ERRORS as INVALID_AUTH_ERRORS
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_TOKEN as CONF_TOKEN, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from pyenphase import Envoy as Envoy
from typing import Any

SCAN_INTERVAL: Incomplete
TOKEN_REFRESH_CHECK_INTERVAL: Incomplete
STALE_TOKEN_THRESHOLD: Incomplete
_LOGGER: Incomplete

class EnphaseUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    envoy_serial_number: str
    envoy: Incomplete
    entry: Incomplete
    username: Incomplete
    password: Incomplete
    _setup_complete: bool
    _cancel_token_refresh: Incomplete
    def __init__(self, hass: HomeAssistant, envoy: Envoy, entry: ConfigEntry) -> None: ...
    def _async_refresh_token_if_needed(self, now: datetime.datetime) -> None: ...
    async def _async_try_refresh_token(self) -> None: ...
    def _async_mark_setup_complete(self) -> None: ...
    async def _async_setup_and_authenticate(self) -> None: ...
    def _async_update_saved_token(self) -> None: ...
    async def _async_update_data(self) -> dict[str, Any]: ...
