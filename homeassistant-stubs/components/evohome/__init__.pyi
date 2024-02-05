import evohomeasync as ev1
import evohomeasync2 as evo
from .const import DOMAIN as DOMAIN, GWS as GWS, STORAGE_KEY as STORAGE_KEY, STORAGE_VER as STORAGE_VER, TCS as TCS, UTC_OFFSET as UTC_OFFSET
from _typeshed import Incomplete
from collections.abc import Awaitable
from datetime import datetime
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete
ACCESS_TOKEN: str
ACCESS_TOKEN_EXPIRES: str
REFRESH_TOKEN: str
USER_DATA: str
CONF_LOCATION_IDX: str
SCAN_INTERVAL_DEFAULT: Incomplete
SCAN_INTERVAL_MINIMUM: Incomplete
CONFIG_SCHEMA: Incomplete
ATTR_SYSTEM_MODE: str
ATTR_DURATION_DAYS: str
ATTR_DURATION_HOURS: str
ATTR_ZONE_TEMP: str
ATTR_DURATION_UNTIL: str
SVC_REFRESH_SYSTEM: str
SVC_SET_SYSTEM_MODE: str
SVC_RESET_SYSTEM: str
SVC_SET_ZONE_OVERRIDE: str
SVC_RESET_ZONE_OVERRIDE: str
RESET_ZONE_OVERRIDE_SCHEMA: Incomplete
SET_ZONE_OVERRIDE_SCHEMA: Incomplete

def _dt_local_to_aware(dt_naive: datetime) -> datetime: ...
def _dt_aware_to_naive(dt_aware: datetime) -> datetime: ...
def convert_until(status_dict: dict, until_key: str) -> None: ...
def convert_dict(dictionary: dict[str, Any]) -> dict[str, Any]: ...
def _handle_exception(err: evo.RequestFailed) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def setup_service_functions(hass: HomeAssistant, broker: EvoBroker) -> None: ...

class EvoBroker:
    hass: Incomplete
    client: Incomplete
    client_v1: Incomplete
    _store: Incomplete
    params: Incomplete
    _location: Incomplete
    config: Incomplete
    tcs: Incomplete
    tcs_utc_offset: Incomplete
    temps: Incomplete
    def __init__(self, hass: HomeAssistant, client: evo.EvohomeClient, client_v1: ev1.EvohomeClient | None, store: Store[dict[str, Any]], params: ConfigType) -> None: ...
    async def save_auth_tokens(self) -> None: ...
    async def call_client_api(self, client_api: Awaitable[dict[str, Any] | None], update_state: bool = True) -> dict[str, Any] | None: ...
    async def _update_v1_api_temps(self) -> None: ...
    async def _update_v2_api_state(self, *args: Any) -> None: ...
    async def async_update(self, *args: Any) -> None: ...

class EvoDevice(Entity):
    _attr_should_poll: bool
    _evo_device: Incomplete
    _evo_broker: Incomplete
    _evo_tcs: Incomplete
    _device_state_attrs: Incomplete
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.ControlSystem | evo.HotWater | evo.Zone) -> None: ...
    async def async_refresh(self, payload: dict | None = None) -> None: ...
    async def async_tcs_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    async def async_zone_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...

class EvoChild(EvoDevice):
    _evo_id: str
    _schedule: Incomplete
    _setpoints: Incomplete
    def __init__(self, evo_broker: EvoBroker, evo_device: evo.HotWater | evo.Zone) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def setpoints(self) -> dict[str, Any]: ...
    async def _update_schedule(self) -> None: ...
    _device_state_attrs: Incomplete
    async def async_update(self) -> None: ...
