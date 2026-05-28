from .const import DEFAULT_SCAN_INTERVAL_SECONDS as DEFAULT_SCAN_INTERVAL_SECONDS, DOMAIN as DOMAIN, OumanDevice as OumanDevice
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_URL as CONF_URL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from ouman_eh_800_api import ControllableEndpoint as ControllableEndpoint, OumanEh800Client, OumanEndpoint, OumanRegistrySet as OumanRegistrySet, OumanValues

_LOGGER: Incomplete
type OumanEh800ConfigEntry = ConfigEntry[OumanEh800Coordinator]

class OumanEh800Coordinator(DataUpdateCoordinator[dict[OumanEndpoint, OumanValues]]):
    _registry_set: OumanRegistrySet
    config_entry: OumanEh800ConfigEntry
    client: OumanEh800Client
    device_info: dict[OumanDevice, DeviceInfo]
    def __init__(self, hass: HomeAssistant, config_entry: OumanEh800ConfigEntry) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[OumanEndpoint, OumanValues]: ...
    async def async_set_endpoint_value(self, endpoint: ControllableEndpoint, value: OumanValues | int) -> None: ...
    def sync_circuit_device_names(self) -> None: ...
