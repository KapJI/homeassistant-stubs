from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from typing import Final, NamedTuple, TypedDict

DOMAIN: Final[str]
SolarNetId = str
SOLAR_NET_DISCOVERY_NEW: Final[str]
SOLAR_NET_ID_POWER_FLOW: SolarNetId
SOLAR_NET_ID_SYSTEM: SolarNetId
SOLAR_NET_RESCAN_TIMER: Final[int]

class FroniusConfigEntryData(TypedDict):
    host: str
    is_logger: bool

class FroniusDeviceInfo(NamedTuple):
    device_info: DeviceInfo
    solar_net_id: SolarNetId
    unique_id: str
