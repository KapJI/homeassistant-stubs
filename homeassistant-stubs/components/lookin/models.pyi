from aiolookin import Device as Device, LookInHttpProtocol as LookInHttpProtocol, LookinUDPSubscriptions as LookinUDPSubscriptions
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class LookinData:
    lookin_udp_subs: LookinUDPSubscriptions
    lookin_device: Device
    meteo_coordinator: DataUpdateCoordinator
    devices: list[dict[str, Any]]
    lookin_protocol: LookInHttpProtocol
