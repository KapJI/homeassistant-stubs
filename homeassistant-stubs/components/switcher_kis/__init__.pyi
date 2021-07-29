from .const import CONF_DEVICE_PASSWORD as CONF_DEVICE_PASSWORD, CONF_PHONE_ID as CONF_PHONE_ID, DATA_DEVICE as DATA_DEVICE, DATA_DISCOVERY as DATA_DISCOVERY, DOMAIN as DOMAIN, MAX_UPDATE_INTERVAL_SEC as MAX_UPDATE_INTERVAL_SEC, SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .utils import async_start_bridge as async_start_bridge, async_stop_bridge as async_stop_bridge
from aioswitcher.device import SwitcherBase as SwitcherBase
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry, update_coordinator as update_coordinator
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from typing import Any

PLATFORMS: Any
_LOGGER: Any
CCONFIG_SCHEMA: Any

async def async_setup(hass: HomeAssistant, config: dict) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SwitcherDeviceWrapper(update_coordinator.DataUpdateCoordinator):
    hass: Any
    entry: Any
    data: Any
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: SwitcherBase) -> None: ...
    async def _async_update_data(self) -> None: ...
    @property
    def model(self) -> str: ...
    @property
    def device_id(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    async def async_setup(self) -> None: ...

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
