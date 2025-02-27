from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass, field
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_API_TOKEN as CONF_API_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from switchbot_api import Device, Remote, SwitchBotAPI

_LOGGER: Incomplete
PLATFORMS: list[Platform]

@dataclass
class SwitchbotDevices:
    buttons: list[Device] = field(default_factory=list)
    climates: list[Remote] = field(default_factory=list)
    switches: list[Device | Remote] = field(default_factory=list)
    sensors: list[Device] = field(default_factory=list)
    vacuums: list[Device] = field(default_factory=list)
    locks: list[Device] = field(default_factory=list)

@dataclass
class SwitchbotCloudData:
    api: SwitchBotAPI
    devices: SwitchbotDevices

async def coordinator_for_device(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, device: Device | Remote, coordinators_by_id: dict[str, SwitchBotCoordinator]) -> SwitchBotCoordinator: ...
async def make_switchbot_devices(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, devices: list[Device | Remote], coordinators_by_id: dict[str, SwitchBotCoordinator]) -> SwitchbotDevices: ...
async def make_device_data(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, device: Device | Remote, devices_data: SwitchbotDevices, coordinators_by_id: dict[str, SwitchBotCoordinator]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
