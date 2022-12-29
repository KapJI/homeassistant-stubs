from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Protocol

class BoardInfo:
    hassio_board_id: Union[str, None]
    manufacturer: str
    model: Union[str, None]
    revision: Union[str, None]
    def __init__(self, hassio_board_id, manufacturer, model, revision) -> None: ...

class USBInfo:
    vid: str
    pid: str
    serial_number: Union[str, None]
    manufacturer: Union[str, None]
    description: Union[str, None]
    def __init__(self, vid, pid, serial_number, manufacturer, description) -> None: ...

class HardwareInfo:
    name: Union[str, None]
    board: Union[BoardInfo, None]
    config_entries: Union[list[str], None]
    dongle: Union[USBInfo, None]
    url: Union[str, None]
    def __init__(self, name, board, config_entries, dongle, url) -> None: ...

class HardwareProtocol(Protocol):
    def async_info(self, hass: HomeAssistant) -> list[HardwareInfo]: ...
