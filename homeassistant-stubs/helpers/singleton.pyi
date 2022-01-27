from collections.abc import Callable
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.loader import bind_hass as bind_hass
from typing import TypeVar

T = TypeVar('T')
FUNC = Callable[[HomeAssistant], T]

def singleton(data_key: str) -> Callable[[FUNC], FUNC]: ...
