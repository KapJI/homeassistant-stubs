from .const import CONF_DEVICE_PASSWORD as CONF_DEVICE_PASSWORD, CONF_PHONE_ID as CONF_PHONE_ID, DATA_DEVICE as DATA_DEVICE, DATA_DISCOVERY as DATA_DISCOVERY, DOMAIN as DOMAIN, MAX_UPDATE_INTERVAL_SEC as MAX_UPDATE_INTERVAL_SEC, SIGNAL_DEVICE_ADD as SIGNAL_DEVICE_ADD
from .utils import async_start_bridge as async_start_bridge, async_stop_bridge as async_stop_bridge
from _typeshed import Incomplete
from aioswitcher.device import SwitcherBase
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import update_coordinator as update_coordinator
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.typing import ConfigType as ConfigType

PLATFORMS: Incomplete
_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class SwitcherDataUpdateCoordinator(update_coordinator.DataUpdateCoordinator[SwitcherBase]):
    entry: Incomplete
    data: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, device: SwitcherBase) -> None: ...
    async def _async_update_data(self) -> SwitcherBase: ...
    @property
    def model(self) -> str: ...
    @property
    def device_id(self) -> str: ...
    @property
    def mac_address(self) -> str: ...
    def async_setup(self) -> None: ...

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
