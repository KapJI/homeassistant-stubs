from .const import DOMAIN as DOMAIN, PREF_PRELOAD_STREAM as PREF_PRELOAD_STREAM
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Any, Final

STORAGE_KEY: Final[Any]
STORAGE_VERSION: Final[int]

class CameraEntityPreferences:
    _prefs: Any
    def __init__(self, prefs: dict[str, bool]) -> None: ...
    def as_dict(self) -> dict[str, bool]: ...
    @property
    def preload_stream(self) -> bool: ...

class CameraPreferences:
    _hass: Any
    _store: Any
    _prefs: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_update(self, entity_id: str, *, preload_stream: Union[bool, UndefinedType] = ..., stream_options: Union[dict[str, str], UndefinedType] = ...) -> None: ...
    def get(self, entity_id: str) -> CameraEntityPreferences: ...
