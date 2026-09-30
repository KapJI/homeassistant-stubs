from .const import CONF_SERIAL as CONF_SERIAL, DOMAIN as DOMAIN
from .util import normalize_serial as normalize_serial
from _typeshed import Incomplete
from collections.abc import Collection, Iterable
from homeassistant import config_entries as config_entries
from homeassistant.components import network as network
from homeassistant.const import CONF_HOST as CONF_HOST, EVENT_HOMEASSISTANT_STARTED as EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HassJob as HassJob, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import discovery_flow as discovery_flow
from homeassistant.helpers.event import async_call_later as async_call_later, async_track_time_interval as async_track_time_interval
from lifx import DiscoveredDevice as DiscoveredDevice
from typing import Any

_LOGGER: Incomplete
DEFAULT_TIMEOUT: float
DISCOVERY_INTERVAL: Incomplete
DISCOVERY_COOLDOWN: int

async def async_discover_devices(hass: HomeAssistant) -> Collection[DiscoveredDevice]: ...
@callback
def async_init_discovery_flow(hass: HomeAssistant, host: str, serial: str) -> None: ...
@callback
def async_trigger_discovery(hass: HomeAssistant, discovered_devices: Iterable[DiscoveredDevice]) -> None: ...

class LIFXDiscoveryManager:
    hass: Incomplete
    lock: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_discovery(self, *_: Any) -> None: ...

@callback
def async_setup_discovery(hass: HomeAssistant) -> None: ...
