import evohomeasync as ev1
import evohomeasync2 as evo
from .const import ACCESS_TOKEN as ACCESS_TOKEN, ACCESS_TOKEN_EXPIRES as ACCESS_TOKEN_EXPIRES, CONF_LOCATION_IDX as CONF_LOCATION_IDX, DOMAIN as DOMAIN, GWS as GWS, REFRESH_TOKEN as REFRESH_TOKEN, TCS as TCS, USER_DATA as USER_DATA, UTC_OFFSET as UTC_OFFSET
from .helpers import dt_local_to_aware as dt_local_to_aware, handle_evo_exception as handle_evo_exception
from _typeshed import Incomplete
from collections.abc import Awaitable
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

_LOGGER: Incomplete

class EvoBroker:
    hass: Incomplete
    client: Incomplete
    client_v1: Incomplete
    _store: Incomplete
    params: Incomplete
    _location: Incomplete
    config: Incomplete
    tcs: Incomplete
    loc_utc_offset: Incomplete
    temps: Incomplete
    def __init__(self, hass: HomeAssistant, client: evo.EvohomeClient, client_v1: ev1.EvohomeClient | None, store: Store[dict[str, Any]], params: ConfigType) -> None: ...
    async def save_auth_tokens(self) -> None: ...
    async def call_client_api(self, client_api: Awaitable[dict[str, Any] | None], update_state: bool = True) -> dict[str, Any] | None: ...
    async def _update_v1_api_temps(self) -> None: ...
    async def _update_v2_api_state(self, *args: Any) -> None: ...
    async def async_update(self, *args: Any) -> None: ...
