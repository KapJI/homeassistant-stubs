from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Protocol

class BoardInfo:
    hassio_board_id: str | None
    manufacturer: str
    model: str | None
    revision: str | None
    def __init__(self, hassio_board_id, manufacturer, model, revision) -> None: ...

class USBInfo:
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None
    def __init__(self, vid, pid, serial_number, manufacturer, description) -> None: ...

class HardwareInfo:
    name: str | None
    board: BoardInfo | None
    config_entries: list[str] | None
    dongle: USBInfo | None
    url: str | None
    def __init__(self, name, board, config_entries, dongle, url) -> None: ...

class HardwareProtocol(Protocol):
    def async_info(self, hass: HomeAssistant) -> list[HardwareInfo]: ...
