from .analytics import Analytics as Analytics
from .const import ATTR_ONBOARDED as ATTR_ONBOARDED, ATTR_PREFERENCES as ATTR_PREFERENCES, DOMAIN as DOMAIN, INTERVAL as INTERVAL, PREFERENCE_SCHEMA as PREFERENCE_SCHEMA
from homeassistant.components import websocket_api as websocket_api
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

async def async_setup(hass: HomeAssistant, _: ConfigType) -> bool: ...
def websocket_analytics(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
async def websocket_analytics_preferences(hass: HomeAssistant, connection: websocket_api.connection.ActiveConnection, msg: dict[str, Any]) -> None: ...
