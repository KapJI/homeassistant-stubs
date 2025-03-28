from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from flexit_bacnet import FlexitBACnet
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_IP_ADDRESS as CONF_IP_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator

_LOGGER: Incomplete
type FlexitConfigEntry = ConfigEntry[FlexitCoordinator]

class FlexitCoordinator(DataUpdateCoordinator[FlexitBACnet]):
    config_entry: FlexitConfigEntry
    device: Incomplete
    def __init__(self, hass: HomeAssistant, config_entry: FlexitConfigEntry) -> None: ...
    async def _async_update_data(self) -> FlexitBACnet: ...
