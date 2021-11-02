from .const import DEFAULT_FAN_SPEED_AWAY as DEFAULT_FAN_SPEED_AWAY, DEFAULT_FAN_SPEED_BOOST as DEFAULT_FAN_SPEED_BOOST, DEFAULT_FAN_SPEED_HOME as DEFAULT_FAN_SPEED_HOME, DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN, METRIC_KEY_PROFILE_FAN_SPEED_AWAY as METRIC_KEY_PROFILE_FAN_SPEED_AWAY, METRIC_KEY_PROFILE_FAN_SPEED_BOOST as METRIC_KEY_PROFILE_FAN_SPEED_BOOST, METRIC_KEY_PROFILE_FAN_SPEED_HOME as METRIC_KEY_PROFILE_FAN_SPEED_HOME, SIGNAL_VALLOX_STATE_UPDATE as SIGNAL_VALLOX_STATE_UPDATE, STATE_PROXY_SCAN_INTERVAL as STATE_PROXY_SCAN_INTERVAL, STR_TO_VALLOX_PROFILE_SETTABLE as STR_TO_VALLOX_PROFILE_SETTABLE
from datetime import datetime
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any
from vallox_websocket_api import PROFILE as VALLOX_PROFILE, Vallox

_LOGGER: Any
CONFIG_SCHEMA: Any
ATTR_PROFILE: str
ATTR_PROFILE_FAN_SPEED: str
SERVICE_SCHEMA_SET_PROFILE: Any
SERVICE_SCHEMA_SET_PROFILE_FAN_SPEED: Any
SERVICE_SET_PROFILE: str
SERVICE_SET_PROFILE_FAN_SPEED_HOME: str
SERVICE_SET_PROFILE_FAN_SPEED_AWAY: str
SERVICE_SET_PROFILE_FAN_SPEED_BOOST: str
SERVICE_TO_METHOD: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class ValloxStateProxy:
    _hass: Any
    _client: Any
    _metric_cache: Any
    _profile: Any
    _valid: bool
    def __init__(self, hass: HomeAssistant, client: Vallox) -> None: ...
    def fetch_metric(self, metric_key: str) -> StateType: ...
    def get_profile(self) -> VALLOX_PROFILE: ...
    async def async_update(self, time: Union[datetime, None] = ...) -> None: ...

class ValloxServiceHandler:
    _client: Any
    _state_proxy: Any
    def __init__(self, client: Vallox, state_proxy: ValloxStateProxy) -> None: ...
    async def async_set_profile(self, profile: str = ...) -> bool: ...
    async def async_set_profile_fan_speed_home(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_away(self, fan_speed: int = ...) -> bool: ...
    async def async_set_profile_fan_speed_boost(self, fan_speed: int = ...) -> bool: ...
    async def async_handle(self, call: ServiceCall) -> None: ...
