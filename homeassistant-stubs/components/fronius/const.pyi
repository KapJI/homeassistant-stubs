from enum import StrEnum
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.typing import StateType as StateType
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

class InverterStatusCodeOption(StrEnum):
    STARTUP: str
    RUNNING: str
    STANDBY: str
    BOOTLOADING: str
    ERROR: str
    IDLE: str
    READY: str
    SLEEPING: str
    UNKNOWN: str
    INVALID: str

_INVERTER_STATUS_CODES: Final[dict[int, InverterStatusCodeOption]]

def get_inverter_status_message(code: StateType) -> InverterStatusCodeOption: ...

class MeterLocationCodeOption(StrEnum):
    FEED_IN: str
    CONSUMPTION_PATH: str
    GENERATOR: str
    EXT_BATTERY: str
    SUBLOAD: str

def get_meter_location_description(code: StateType) -> MeterLocationCodeOption | None: ...

class OhmPilotStateCodeOption(StrEnum):
    UP_AND_RUNNING: str
    KEEP_MINIMUM_TEMPERATURE: str
    LEGIONELLA_PROTECTION: str
    CRITICAL_FAULT: str
    FAULT: str
    BOOST_MODE: str

_OHMPILOT_STATE_CODES: Final[dict[int, OhmPilotStateCodeOption]]

def get_ohmpilot_state_message(code: StateType) -> OhmPilotStateCodeOption | None: ...
