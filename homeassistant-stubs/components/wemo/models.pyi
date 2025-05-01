import pywemo
from . import HostPortTuple as HostPortTuple, WemoDiscovery as WemoDiscovery, WemoDispatcher as WemoDispatcher
from .const import DOMAIN as DOMAIN
from .coordinator import DeviceCoordinator as DeviceCoordinator
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.util.hass_dict import HassKey as HassKey

DATA_WEMO: HassKey[WemoData]

@dataclass
class WemoConfigEntryData:
    device_coordinators: dict[str, DeviceCoordinator]
    discovery: WemoDiscovery
    dispatcher: WemoDispatcher

@dataclass
class WemoData:
    discovery_enabled: bool
    static_config: Sequence[HostPortTuple]
    registry: pywemo.SubscriptionRegistry
    config_entry_data: WemoConfigEntryData = ...
