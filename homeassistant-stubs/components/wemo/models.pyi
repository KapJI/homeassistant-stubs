import pywemo
from . import HostPortTuple as HostPortTuple, WemoDiscovery as WemoDiscovery, WemoDispatcher as WemoDispatcher
from .const import DOMAIN as DOMAIN
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@dataclass
class WemoConfigEntryData:
    device_coordinators: dict[str, 'DeviceCoordinator']
    discovery: WemoDiscovery
    dispatcher: WemoDispatcher
    def __init__(self, device_coordinators, discovery, dispatcher) -> None: ...

@dataclass
class WemoData:
    discovery_enabled: bool
    static_config: Sequence['HostPortTuple']
    registry: pywemo.SubscriptionRegistry
    config_entry_data: WemoConfigEntryData = ...
    def __init__(self, discovery_enabled, static_config, registry, config_entry_data) -> None: ...

def async_wemo_data(hass: HomeAssistant) -> WemoData: ...
