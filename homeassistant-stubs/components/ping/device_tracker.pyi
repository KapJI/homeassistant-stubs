from .const import DOMAIN as DOMAIN, ICMP_TIMEOUT as ICMP_TIMEOUT, PING_ATTEMPTS_COUNT as PING_ATTEMPTS_COUNT, PING_PRIVS as PING_PRIVS, PING_TIMEOUT as PING_TIMEOUT
from _typeshed import Incomplete
from homeassistant.components.device_tracker import AsyncSeeCallback as AsyncSeeCallback, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, SCAN_INTERVAL as SCAN_INTERVAL, SourceType as SourceType
from homeassistant.const import CONF_HOSTS as CONF_HOSTS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.async_ import gather_with_concurrency as gather_with_concurrency
from homeassistant.util.process import kill_subprocess as kill_subprocess

_LOGGER: Incomplete
PARALLEL_UPDATES: int
CONF_PING_COUNT: str
CONCURRENT_PING_LIMIT: int
PLATFORM_SCHEMA: Incomplete

class HostSubProcess:
    hass: Incomplete
    ip_address: Incomplete
    dev_id: Incomplete
    _count: Incomplete
    _ping_cmd: Incomplete
    def __init__(self, ip_address: str, dev_id: str, hass: HomeAssistant, config: ConfigType, privileged: bool | None) -> None: ...
    def ping(self) -> bool | None: ...
    def update(self) -> bool: ...

async def async_setup_scanner(hass: HomeAssistant, config: ConfigType, async_see: AsyncSeeCallback, discovery_info: DiscoveryInfoType | None = ...) -> bool: ...
