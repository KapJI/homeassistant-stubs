from homeassistant.const import RESTART_EXIT_CODE as RESTART_EXIT_CODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from types import FrameType as FrameType
from typing import Any

_LOGGER: Any

def async_register_signal_handling(hass: HomeAssistant) -> None: ...
