from .const import DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_ID as CONF_ID, CONF_LOCATION as CONF_LOCATION
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode, TextSelector as TextSelector
from pytrafikverket.trafikverket_camera import CameraInfo as CameraInfo
from typing import Any

class TVCameraConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    entry: config_entries.ConfigEntry | None
    cameras: list[CameraInfo]
    api_key: str
    async def validate_input(self, sensor_api: str, location: str) -> tuple[dict[str, str], list[CameraInfo] | None]: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
    async def async_step_multiple_cameras(self, user_input: dict[str, str] | None = None) -> FlowResult: ...
