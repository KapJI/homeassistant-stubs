from .const import DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from pytradfri.device.blind import Blind as Blind
from pytradfri.device.blind_control import BlindControl as BlindControl
from pytradfri.device.light import Light as Light
from pytradfri.device.light_control import LightControl as LightControl
from pytradfri.device.signal_repeater_control import SignalRepeaterControl as SignalRepeaterControl
from pytradfri.device.socket import Socket as Socket
from pytradfri.device.socket_control import SocketControl as SocketControl
from typing import Any

_LOGGER: Any

def handle_error(func: Callable[[Union[Command, list[Command]]], Any]) -> Callable[[str], Any]: ...

class TradfriBaseClass(Entity):
    _attr_should_poll: bool
    _api: Any
    _device: Any
    _device_control: Any
    _device_data: Any
    _gateway_id: Any
    def __init__(self, device: Device, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    def _async_start_observe(self, exc: Union[Exception, None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _observe_update(self, device: Device) -> None: ...
    _attr_name: Any
    def _refresh(self, device: Device) -> None: ...

class TradfriBaseDevice(TradfriBaseClass):
    @property
    def device_info(self) -> DeviceInfo: ...
    _attr_available: Any
    def _refresh(self, device: Device) -> None: ...
