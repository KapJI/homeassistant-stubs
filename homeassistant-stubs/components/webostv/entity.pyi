from .const import DOMAIN as DOMAIN, WEBOSTV_EXCEPTIONS as WEBOSTV_EXCEPTIONS
from .coordinator import WebOsTvConfigEntry as WebOsTvConfigEntry, WebOsTvDataUpdateCoordinator as WebOsTvDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Concatenate

class WebOsTvEntity(CoordinatorEntity[WebOsTvDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: DeviceInfo
    _client: Incomplete
    def __init__(self, entry: WebOsTvConfigEntry) -> None: ...

def cmd[_EntityT: WebOsTvEntity, _R, **_P](func: Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, _R]]) -> Callable[Concatenate[_EntityT, _P], Coroutine[Any, Any, _R]]: ...
