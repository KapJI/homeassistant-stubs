from .const import DOMAIN as DOMAIN
from .coordinator import SwitchBotCoordinator as SwitchBotCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY, CONF_API_TOKEN as CONF_API_TOKEN, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from switchbot_api import Device, Remote, SwitchBotAPI

_LOGGER: Incomplete
PLATFORMS: list[Platform]

class SwitchbotDevices:
    switches: list[Device | Remote]
    def __init__(self, switches) -> None: ...

class SwitchbotCloudData:
    api: SwitchBotAPI
    devices: SwitchbotDevices
    def __init__(self, api, devices) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
