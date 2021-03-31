from .dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from .typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant import core as core, setup as setup
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE
from homeassistant.loader import bind_hass as bind_hass
from typing import Any, Callable, TypedDict

SIGNAL_PLATFORM_DISCOVERED: str
EVENT_LOAD_PLATFORM: str
ATTR_PLATFORM: str
ATTR_DISCOVERED: str

class DiscoveryDict(TypedDict):
    service: str
    platform: Union[str, None]
    discovered: Union[DiscoveryInfoType, None]

def async_listen(hass: core.HomeAssistant, service: str, callback: CALLBACK_TYPE) -> None: ...
def discover(hass: core.HomeAssistant, service: str, discovered: DiscoveryInfoType, component: str, hass_config: ConfigType) -> None: ...
async def async_discover(hass: core.HomeAssistant, service: str, discovered: Union[DiscoveryInfoType, None], component: Union[str, None], hass_config: ConfigType) -> None: ...
def async_listen_platform(hass: core.HomeAssistant, component: str, callback: Callable[[str, Union[dict[str, Any], None]], Any]) -> None: ...
def load_platform(hass: core.HomeAssistant, component: str, platform: str, discovered: DiscoveryInfoType, hass_config: ConfigType) -> None: ...
async def async_load_platform(hass: core.HomeAssistant, component: str, platform: str, discovered: DiscoveryInfoType, hass_config: ConfigType) -> None: ...
