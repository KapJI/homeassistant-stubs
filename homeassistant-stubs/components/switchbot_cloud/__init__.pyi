from .const import DOMAIN as DOMAIN, ENTRY_TITLE as ENTRY_TITLE
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass, field
from homeassistant.components import webhook as webhook
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_API_TOKEN as CONF_API_TOKEN, CONF_WEBHOOK_ID as CONF_WEBHOOK_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from switchbot_api import Device, Remote, SwitchBotAPI

_LOGGER: Incomplete
PLATFORMS: list[Platform]

@dataclass
class SwitchbotDevices:
    binary_sensors: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    buttons: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    climates: list[tuple[Remote | Device, SwitchBotCoordinator]] = field(default_factory=list)
    covers: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    switches: list[tuple[Device | Remote, SwitchBotCoordinator]] = field(default_factory=list)
    sensors: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    vacuums: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    locks: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    fans: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    lights: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)
    humidifiers: list[tuple[Device, SwitchBotCoordinator]] = field(default_factory=list)

@dataclass
class SwitchbotCloudData:
    api: SwitchBotAPI
    devices: SwitchbotDevices

async def coordinator_for_device(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, device: Device | Remote, coordinators_by_id: dict[str, SwitchBotCoordinator], manageable_by_webhook: bool = False) -> SwitchBotCoordinator: ...
async def make_switchbot_devices(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, devices: list[Device | Remote], coordinators_by_id: dict[str, SwitchBotCoordinator]) -> SwitchbotDevices: ...
async def make_device_data(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, device: Device | Remote, devices_data: SwitchbotDevices, coordinators_by_id: dict[str, SwitchBotCoordinator]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _initialize_webhook(hass: HomeAssistant, entry: ConfigEntry, api: SwitchBotAPI, coordinators_by_id: dict[str, SwitchBotCoordinator]) -> None: ...
def _create_handle_webhook(coordinators_by_id: dict[str, SwitchBotCoordinator]) -> Callable[[HomeAssistant, str, web.Request], Awaitable[None]]: ...
