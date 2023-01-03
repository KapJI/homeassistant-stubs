from .. import mysensors as mysensors
from .const import ATTR_GATEWAY_ID as ATTR_GATEWAY_ID, DevId as DevId, DiscoveryInfo as DiscoveryInfo, GatewayId as GatewayId
from .helpers import on_unload as on_unload
from _typeshed import Incomplete
from homeassistant.components.device_tracker import AsyncSeeCallback as AsyncSeeCallback
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import slugify as slugify
from typing import Any

async def async_setup_scanner(hass: HomeAssistant, config: ConfigType, async_see: AsyncSeeCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> bool: ...

class MySensorsDeviceScanner(mysensors.device.MySensorsDevice):
    async_see: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, async_see: AsyncSeeCallback, *args: Any) -> None: ...
    async def _async_update_callback(self) -> None: ...
