import voluptuous as vol
from .const import DEFAULT_FAN_SPEED_AWAY as DEFAULT_FAN_SPEED_AWAY, DEFAULT_FAN_SPEED_BOOST as DEFAULT_FAN_SPEED_BOOST, DEFAULT_FAN_SPEED_HOME as DEFAULT_FAN_SPEED_HOME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, METRIC_KEY_PROFILE_FAN_SPEED_AWAY as METRIC_KEY_PROFILE_FAN_SPEED_AWAY, METRIC_KEY_PROFILE_FAN_SPEED_BOOST as METRIC_KEY_PROFILE_FAN_SPEED_BOOST, METRIC_KEY_PROFILE_FAN_SPEED_HOME as METRIC_KEY_PROFILE_FAN_SPEED_HOME, STATE_SCAN_INTERVAL as STATE_SCAN_INTERVAL, STR_TO_VALLOX_PROFILE_SETTABLE as STR_TO_VALLOX_PROFILE_SETTABLE
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, NamedTuple
from uuid import UUID
from vallox_websocket_api import PROFILE as VALLOX_PROFILE, Vallox

_LOGGER: Any
CONFIG_SCHEMA: Any
ATTR_PROFILE: str
ATTR_PROFILE_FAN_SPEED: str
SERVICE_SCHEMA_SET_PROFILE: Any
SERVICE_SCHEMA_SET_PROFILE_FAN_SPEED: Any

class ServiceMethodDetails(NamedTuple):
    method: str
    schema: vol.Schema

SERVICE_SET_PROFILE: str
SERVICE_SET_PROFILE_FAN_SPEED_HOME: str
SERVICE_SET_PROFILE_FAN_SPEED_AWAY: str
SERVICE_SET_PROFILE_FAN_SPEED_BOOST: str
SERVICE_TO_METHOD: Any

class ValloxState:
    metric_cache: dict[str, Any]
    profile: VALLOX_PROFILE
    def get_metric(self, metric_key: str) -> StateType: ...
    def get_uuid(self) -> Union[UUID, None]: ...

class ValloxDataUpdateCoordinator(DataUpdateCoordinator):
    data: ValloxState

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ValloxServiceHandler:
    _client: Any
    _coordinator: Any
    def __init__(self, client: Vallox, coordinator: DataUpdateCoordinator[ValloxState]) -> None: ...
    async def async_set_profile(self, profile: str = ...) -> bool: ...
    async def async_set_profile_fan_speed_home(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_away(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_boost(self, fan_speed: int = ...) -> bool: ...
    async def async_handle(self, call: ServiceCall) -> None: ...
