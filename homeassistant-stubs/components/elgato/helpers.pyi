from .const import DOMAIN as DOMAIN
from .coordinator import ElgatoData as ElgatoData
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Any, Concatenate

COLOR_TEMPERATURE_RANGE: Incomplete
COLOR_TEMPERATURE_RANGE_COLOR: Incomplete
COLOR_CAPABLE_PRODUCTS: Incomplete

def supports_color(data: ElgatoData) -> bool: ...
def color_temperature_range(data: ElgatoData) -> tuple[int, int]: ...
def elgato_device_action[_ElgatoEntityT: ElgatoEntity, **_P](func: Callable[Concatenate[_ElgatoEntityT, _P], Coroutine[Any, Any, Any]]) -> Callable[Concatenate[_ElgatoEntityT, _P], Coroutine[Any, Any, None]]: ...
