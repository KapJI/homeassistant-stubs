from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from pathlib import Path

class LocalTodoListStore:
    _hass: Incomplete
    _path: Incomplete
    _lock: Incomplete
    def __init__(self, hass: HomeAssistant, path: Path) -> None: ...
    async def async_load(self) -> str: ...
    def _load(self) -> str: ...
    async def async_store(self, ics_content: str) -> None: ...
    def _store(self, ics_content: str) -> None: ...
