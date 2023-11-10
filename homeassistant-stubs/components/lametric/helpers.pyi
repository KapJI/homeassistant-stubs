from .const import DOMAIN as DOMAIN
from .coordinator import LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from collections.abc import Callable as Callable, Coroutine
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate, ParamSpec, TypeVar

_LaMetricEntityT = TypeVar('_LaMetricEntityT', bound=LaMetricEntity)
_P = ParamSpec('_P')

def lametric_exception_handler(func: Callable[Concatenate[_LaMetricEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_LaMetricEntityT, _P], Coroutine[Any, Any, None]]: ...
def async_get_coordinator_by_device_id(hass: HomeAssistant, device_id: str) -> LaMetricDataUpdateCoordinator: ...
