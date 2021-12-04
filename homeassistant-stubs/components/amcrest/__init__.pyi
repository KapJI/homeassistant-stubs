import aiohttp
import threading
from .binary_sensor import BINARY_SENSORS as BINARY_SENSORS, BINARY_SENSOR_KEYS as BINARY_SENSOR_KEYS, check_binary_sensors as check_binary_sensors
from .camera import CAMERA_SERVICES as CAMERA_SERVICES, STREAM_SOURCE_LIST as STREAM_SOURCE_LIST
from .const import CAMERAS as CAMERAS, COMM_RETRIES as COMM_RETRIES, COMM_TIMEOUT as COMM_TIMEOUT, DATA_AMCREST as DATA_AMCREST, DEVICES as DEVICES, DOMAIN as DOMAIN, SERVICE_EVENT as SERVICE_EVENT, SERVICE_UPDATE as SERVICE_UPDATE
from .helpers import service_signal as service_signal
from .sensor import SENSOR_KEYS as SENSOR_KEYS
from .switch import SWITCH_KEYS as SWITCH_KEYS
from amcrest import ApiWrapper
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.auth.models import User as User
from homeassistant.auth.permissions.const import POLICY_CONTROL as POLICY_CONTROL
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_SENSORS as CONF_SENSORS, CONF_SWITCHES as CONF_SWITCHES, CONF_USERNAME as CONF_USERNAME, ENTITY_MATCH_ALL as ENTITY_MATCH_ALL, ENTITY_MATCH_NONE as ENTITY_MATCH_NONE, HTTP_BASIC_AUTHENTICATION as HTTP_BASIC_AUTHENTICATION
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import Unauthorized as Unauthorized, UnknownUser as UnknownUser
from homeassistant.helpers import discovery as discovery
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send, dispatcher_send as dispatcher_send
from homeassistant.helpers.event import track_time_interval as track_time_interval
from homeassistant.helpers.service import async_extract_entity_ids as async_extract_entity_ids
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Any
CONF_RESOLUTION: str
CONF_STREAM_SOURCE: str
CONF_FFMPEG_ARGUMENTS: str
CONF_CONTROL_LIGHT: str
DEFAULT_NAME: str
DEFAULT_PORT: int
DEFAULT_RESOLUTION: str
DEFAULT_ARGUMENTS: str
MAX_ERRORS: int
RECHECK_INTERVAL: Any
NOTIFICATION_ID: str
NOTIFICATION_TITLE: str
RESOLUTION_LIST: Any
SCAN_INTERVAL: Any
AUTHENTICATION_LIST: Any

def _has_unique_names(devices: list[dict[str, Any]]) -> list[dict[str, Any]]: ...

AMCREST_SCHEMA: Any
CONFIG_SCHEMA: Any

class AmcrestChecker(ApiWrapper):
    _hass: Any
    _wrap_name: Any
    _wrap_errors: int
    _wrap_lock: Any
    _wrap_login_err: bool
    _wrap_event_flag: Any
    _unsub_recheck: Any
    def __init__(self, hass: HomeAssistant, name: str, host: str, port: int, user: str, password: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def available_flag(self) -> threading.Event: ...
    def _start_recovery(self) -> None: ...
    def command(self, *args: Any, **kwargs: Any) -> Any: ...
    def _wrap_test_online(self, now: datetime) -> None: ...

def _monitor_events(hass: HomeAssistant, name: str, api: AmcrestChecker, event_codes: set[str]) -> None: ...
def _start_event_monitor(hass: HomeAssistant, name: str, api: AmcrestChecker, event_codes: set[str]) -> None: ...
def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class AmcrestDevice:
    api: AmcrestChecker
    authentication: Union[aiohttp.BasicAuth, None]
    ffmpeg_arguments: list[str]
    stream_source: str
    resolution: int
    control_light: bool
    channel: int
