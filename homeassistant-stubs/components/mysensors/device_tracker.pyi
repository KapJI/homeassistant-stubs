from .helpers import on_unload as on_unload
from homeassistant.components import mysensors as mysensors
from homeassistant.components.device_tracker import DOMAIN as DOMAIN
from homeassistant.components.mysensors import DevId as DevId
from homeassistant.components.mysensors.const import ATTR_GATEWAY_ID as ATTR_GATEWAY_ID, DiscoveryInfo as DiscoveryInfo, GatewayId as GatewayId
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.util import slugify as slugify
from typing import Any, Callable

async def async_setup_scanner(hass: HomeAssistant, config: dict[str, Any], async_see: Callable, discovery_info: Union[DiscoveryInfo, None] = ...) -> bool: ...

class MySensorsDeviceScanner(mysensors.device.MySensorsDevice):
    async_see: Any
    hass: Any
    def __init__(self, hass: HomeAssistant, async_see: Callable, *args: Any) -> None: ...
    async def _async_update_callback(self) -> None: ...
