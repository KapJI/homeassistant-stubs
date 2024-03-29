from .generic_cover import COMMANDS_CLOSE as COMMANDS_CLOSE, COMMANDS_OPEN as COMMANDS_OPEN, COMMANDS_STOP as COMMANDS_STOP, OverkizGenericCover as OverkizGenericCover
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverDeviceClass as CoverDeviceClass, CoverEntityFeature as CoverEntityFeature
from typing import Any

class Awning(OverkizGenericCover):
    _attr_device_class: Incomplete
    @property
    def supported_features(self) -> CoverEntityFeature: ...
    @property
    def current_cover_position(self) -> int | None: ...
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @property
    def is_opening(self) -> bool | None: ...
    @property
    def is_closing(self) -> bool | None: ...
