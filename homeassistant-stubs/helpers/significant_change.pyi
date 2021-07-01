from .integration_platform import async_process_integration_platforms as async_process_integration_platforms
from homeassistant.const import STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from types import MappingProxyType
from typing import Any, Callable, Optional, Union

PLATFORM: str
DATA_FUNCTIONS: str
CheckTypeFunc = Callable[[HomeAssistant, str, Union[dict, MappingProxyType], str, Union[dict, MappingProxyType]], Optional[bool]]
ExtraCheckTypeFunc = Callable[[HomeAssistant, str, Union[dict, MappingProxyType], Any, str, Union[dict, MappingProxyType], Any], Optional[bool]]

async def create_checker(hass: HomeAssistant, _domain: str, extra_significant_check: Union[ExtraCheckTypeFunc, None] = ...) -> SignificantlyChangedChecker: ...
async def _initialize(hass: HomeAssistant) -> None: ...
def either_one_none(val1: Union[Any, None], val2: Union[Any, None]) -> bool: ...
def check_numeric_changed(val1: Union[int, float, None], val2: Union[int, float, None], change: Union[int, float]) -> bool: ...

class SignificantlyChangedChecker:
    hass: Any
    last_approved_entities: Any
    extra_significant_check: Any
    def __init__(self, hass: HomeAssistant, extra_significant_check: Union[ExtraCheckTypeFunc, None] = ...) -> None: ...
    def async_is_significant_change(self, new_state: State, *, extra_arg: Union[Any, None] = ...) -> bool: ...
