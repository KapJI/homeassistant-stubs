from collections.abc import Callable
from dataclasses import dataclass
from google_nest_sdm.device import Device
from google_nest_sdm.device_manager import DeviceManager as DeviceManager
from google_nest_sdm.google_nest_subscriber import GoogleNestSubscriber as GoogleNestSubscriber
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type DevicesAddedListener = Callable[[list[Device]], None]
@dataclass
class NestData:
    subscriber: GoogleNestSubscriber
    device_manager: DeviceManager
    register_devices_listener: Callable[[DevicesAddedListener], None]
type NestConfigEntry = ConfigEntry[NestData]
