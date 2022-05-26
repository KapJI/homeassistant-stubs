from .const import DOMAIN as DOMAIN, PREF_PRELOAD_STREAM as PREF_PRELOAD_STREAM
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Final

STORAGE_KEY: Final[Incomplete]
STORAGE_VERSION: Final[int]

class CameraEntityPreferences:
    _prefs: Incomplete
    def __init__(self, prefs: dict[str, bool]) -> None: ...
    def as_dict(self) -> dict[str, bool]: ...
    @property
    def preload_stream(self) -> bool: ...

class CameraPreferences:
    _hass: Incomplete
    _store: Incomplete
    _prefs: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    async def async_update(self, entity_id: str, *, preload_stream: Union[bool, UndefinedType] = ..., stream_options: Union[dict[str, str], UndefinedType] = ...) -> None: ...
    def get(self, entity_id: str) -> CameraEntityPreferences: ...
