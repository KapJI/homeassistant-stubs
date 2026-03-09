from .const import DOMAIN as DOMAIN, SUPPORTED_DEVICE_TYPES as SUPPORTED_DEVICE_TYPES
from .coordinator import WattsVisionDeviceCoordinator as WattsVisionDeviceCoordinator, WattsVisionDeviceData as WattsVisionDeviceData, WattsVisionHubCoordinator as WattsVisionHubCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import aiohttp_client as aiohttp_client, config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from visionpluspython.auth import WattsVisionAuth
from visionpluspython.client import WattsVisionClient

_LOGGER: Incomplete
PLATFORMS: list[Platform]

@dataclass
class WattsVisionRuntimeData:
    auth: WattsVisionAuth
    hub_coordinator: WattsVisionHubCoordinator
    device_coordinators: dict[str, WattsVisionDeviceCoordinator]
    client: WattsVisionClient
type WattsVisionConfigEntry = ConfigEntry[WattsVisionRuntimeData]

@callback
def _handle_new_devices(hass: HomeAssistant, entry: WattsVisionConfigEntry, hub_coordinator: WattsVisionHubCoordinator) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: WattsVisionConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: WattsVisionConfigEntry) -> bool: ...
