from .const import DOMAIN as DOMAIN, SIGNAL_GW as SIGNAL_GW
from collections.abc import Callable as Callable
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from pytradfri.device.air_purifier import AirPurifier as AirPurifier
from pytradfri.device.air_purifier_control import AirPurifierControl as AirPurifierControl
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
    _attr_name: Any
    _device: Any
    _device_control: Any
    _device_data: Any
    _gateway_id: Any
    def __init__(self, device: Device, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    _attr_available: bool
    async def _async_run_observe(self, cmd: Command) -> None: ...
    def _async_start_observe(self, exc: Union[Exception, None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _observe_update(self, device: Device) -> None: ...
    def _refresh(self, device: Device, write_ha: bool = ...) -> None: ...

class TradfriBaseDevice(TradfriBaseClass):
    _attr_available: Any
    _hub_available: bool
    def __init__(self, device: Device, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def set_hub_available(self, available: bool) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def _refresh(self, device: Device, write_ha: bool = ...) -> None: ...
