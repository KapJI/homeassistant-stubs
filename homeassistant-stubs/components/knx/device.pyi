from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from xknx import XKNX as XKNX
from xknx.core import XknxConnectionState
from xknx.io.gateway_scanner import GatewayDescriptor as GatewayDescriptor

class KNXInterfaceDevice:
    device_registry: Incomplete
    gateway_descriptor: Incomplete
    xknx: Incomplete
    device: Incomplete
    device_info: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, xknx: XKNX) -> None: ...
    async def update(self) -> None: ...
    async def connection_state_changed_cb(self, state: XknxConnectionState) -> None: ...
