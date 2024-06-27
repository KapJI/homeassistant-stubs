import evohomeasync2 as evo
from .const import ACCESS_TOKEN_EXPIRES as ACCESS_TOKEN_EXPIRES, ATTR_DURATION_DAYS as ATTR_DURATION_DAYS, ATTR_DURATION_HOURS as ATTR_DURATION_HOURS, ATTR_DURATION_UNTIL as ATTR_DURATION_UNTIL, ATTR_SYSTEM_MODE as ATTR_SYSTEM_MODE, ATTR_ZONE_TEMP as ATTR_ZONE_TEMP, CONF_LOCATION_IDX as CONF_LOCATION_IDX, DOMAIN as DOMAIN, EvoService as EvoService, GWS as GWS, SCAN_INTERVAL_DEFAULT as SCAN_INTERVAL_DEFAULT, SCAN_INTERVAL_MINIMUM as SCAN_INTERVAL_MINIMUM, STORAGE_KEY as STORAGE_KEY, STORAGE_VER as STORAGE_VER, TCS as TCS, USER_DATA as USER_DATA
from .coordinator import EvoBroker as EvoBroker
from .helpers import convert_dict as convert_dict, convert_until as convert_until, dt_aware_to_naive as dt_aware_to_naive, handle_evo_exception as handle_evo_exception
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Final

_LOGGER: Incomplete
CONFIG_SCHEMA: Final[Incomplete]
RESET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]
SET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def setup_service_functions(hass: HomeAssistant, broker: EvoBroker) -> None: ...

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
