from _typeshed import Incomplete
from datetime import datetime
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import dispatcher_send as dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from homeassistant.helpers.typing import ConfigType as ConfigType

DOMAIN: str
DATA_UPDATED: Incomplete
_LOGGER: Incomplete
CONF_MANUAL: str
DEFAULT_INTERVAL: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class SpeedtestData:
    data: Incomplete
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def update(self, now: datetime | None = ...) -> None: ...
