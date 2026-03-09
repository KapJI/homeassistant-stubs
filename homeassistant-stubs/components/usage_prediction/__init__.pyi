from . import common_control as common_control
from .const import DATA_CACHE as DATA_CACHE, DOMAIN as DOMAIN
from .models import EntityUsageDataCache as EntityUsageDataCache, EntityUsagePredictions as EntityUsagePredictions
from _typeshed import Incomplete
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

CONFIG_SCHEMA: Incomplete
CACHE_DURATION: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@websocket_api.async_response
async def ws_common_control(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def get_cached_common_control(hass: HomeAssistant, user_id: str) -> EntityUsagePredictions: ...
