from collections.abc import Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from typing import TypeVar

_T = TypeVar('_T')
FUNC = Callable[[HomeAssistant], _T]

def singleton(data_key: str) -> Callable[[FUNC], FUNC]: ...
