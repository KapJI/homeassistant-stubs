from .coordinator import LookinDataUpdateCoordinator as LookinDataUpdateCoordinator
from aiolookin import Device as Device, LookInHttpProtocol as LookInHttpProtocol, LookinUDPSubscriptions as LookinUDPSubscriptions, MeteoSensor as MeteoSensor, Remote as Remote
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from typing import Any

type LookinConfigEntry = ConfigEntry[LookinData]
@dataclass
class LookinData:
    host: str
    lookin_udp_subs: LookinUDPSubscriptions
    lookin_device: Device
    meteo_coordinator: LookinDataUpdateCoordinator[MeteoSensor] | None
    devices: list[dict[str, Any]]
    lookin_protocol: LookInHttpProtocol
    device_coordinators: dict[str, LookinDataUpdateCoordinator[Remote]]
