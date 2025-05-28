import psutil_home_assistant as ha_psutil
from dataclasses import dataclass
from homeassistant.components import websocket_api as websocket_api
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from typing import Protocol

@dataclass
class HardwareData:
    hardware_platform: dict[str, HardwareProtocol]
    system_status: SystemStatus

@dataclass(slots=True)
class SystemStatus:
    ha_psutil: ha_psutil
    remove_periodic_timer: CALLBACK_TYPE | None
    subscribers: set[tuple[websocket_api.ActiveConnection, int]]

@dataclass(slots=True)
class BoardInfo:
    hassio_board_id: str | None
    manufacturer: str
    model: str | None
    revision: str | None

@dataclass(slots=True, frozen=True)
class USBInfo:
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None

@dataclass(slots=True, frozen=True)
class HardwareInfo:
    name: str | None
    board: BoardInfo | None
    config_entries: list[str] | None
    dongle: USBInfo | None
    url: str | None

class HardwareProtocol(Protocol):
    @callback
    def async_info(self, hass: HomeAssistant) -> list[HardwareInfo]: ...
