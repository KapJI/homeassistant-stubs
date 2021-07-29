from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DOMAIN: str
DATA_UPDATED: Any
_LOGGER: Any
CONF_MANUAL: str
DEFAULT_INTERVAL: Any
CONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class SpeedtestData:
    data: Any
    _hass: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    def update(self) -> None: ...
