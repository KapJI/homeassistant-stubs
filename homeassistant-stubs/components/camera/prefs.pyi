from .const import DOMAIN as DOMAIN, PREF_ORIENTATION as PREF_ORIENTATION, PREF_PRELOAD_STREAM as PREF_PRELOAD_STREAM
from _typeshed import Incomplete
from homeassistant.components.stream import Orientation as Orientation
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import UNDEFINED as UNDEFINED, UndefinedType as UndefinedType
from typing import Final

STORAGE_KEY: Final[Incomplete]
STORAGE_VERSION: Final[int]

class DynamicStreamSettings:
    preload_stream: bool
    orientation: Orientation
    def __init__(self, preload_stream, orientation) -> None: ...

class CameraPreferences:
    _hass: Incomplete
    _store: Incomplete
    _dynamic_stream_settings_by_entity_id: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_update(self, entity_id: str, *, preload_stream: bool | UndefinedType = ..., orientation: Orientation | UndefinedType = ...) -> dict[str, bool | Orientation]: ...
    async def get_dynamic_stream_settings(self, entity_id: str) -> DynamicStreamSettings: ...
