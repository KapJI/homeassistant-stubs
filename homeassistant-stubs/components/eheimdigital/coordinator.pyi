from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from collections.abc import Callable
from eheimdigital.device import EheimDigitalDevice
from eheimdigital.types import EheimDeviceType as EheimDeviceType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_component import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed

type AsyncSetupDeviceEntitiesCallback = Callable[[dict[str, EheimDigitalDevice]], None]
type EheimDigitalConfigEntry = ConfigEntry[EheimDigitalUpdateCoordinator]
class EheimDigitalUpdateCoordinator(DataUpdateCoordinator[dict[str, EheimDigitalDevice]]):
    config_entry: EheimDigitalConfigEntry
    main_device_added_event: Incomplete
    hub: Incomplete
    known_devices: set[str]
    platform_callbacks: set[AsyncSetupDeviceEntitiesCallback]
    def __init__(self, hass: HomeAssistant, config_entry: EheimDigitalConfigEntry) -> None: ...
    def add_platform_callback(self, async_setup_device_entities: AsyncSetupDeviceEntitiesCallback) -> None: ...
    async def _async_device_found(self, device_address: str, device_type: EheimDeviceType) -> None: ...
    async def _async_receive_callback(self) -> None: ...
    async def _async_setup(self) -> None: ...
    async def _async_update_data(self) -> dict[str, EheimDigitalDevice]: ...
