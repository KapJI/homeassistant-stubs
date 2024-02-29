from .entity import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from _typeshed import Incomplete
from aioesphomeapi import CameraInfo, CameraState
from aiohttp import web as web
from collections.abc import Callable as Callable
from homeassistant.components import camera as camera
from homeassistant.components.camera import Camera as Camera
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeCamera(Camera, EsphomeEntity[CameraInfo, CameraState]):
    _loop: Incomplete
    _image_futures: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _set_futures(self, result: bool) -> None: ...
    def _on_device_update(self) -> None: ...
    def _on_state_update(self) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    async def _async_request_image(self, request_method: Callable[[], None]) -> bytes | None: ...
    async def handle_async_mjpeg_stream(self, request: web.Request) -> web.StreamResponse: ...
