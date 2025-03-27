import aiohttp
from .const import FIRMWARE as FIRMWARE, FIRMWARE_VERSION as FIRMWARE_VERSION, NABU_CASA_FIRMWARE_RELEASES_URL as NABU_CASA_FIRMWARE_RELEASES_URL, RADIO_DEVICE as RADIO_DEVICE
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from homeassistant.components.homeassistant_hardware.update import BaseFirmwareUpdateEntity as BaseFirmwareUpdateEntity, FirmwareUpdateEntityDescription as FirmwareUpdateEntityDescription
from homeassistant.components.homeassistant_hardware.util import ApplicationType as ApplicationType, FirmwareInfo as FirmwareInfo
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
FIRMWARE_ENTITY_DESCRIPTIONS: dict[ApplicationType | None, FirmwareUpdateEntityDescription]

def _async_create_update_entity(hass: HomeAssistant, config_entry: ConfigEntry, session: aiohttp.ClientSession, async_add_entities: AddConfigEntryEntitiesCallback) -> FirmwareUpdateEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FirmwareUpdateEntity(BaseFirmwareUpdateEntity):
    bootloader_reset_type: str
    _attr_unique_id: Incomplete
    _current_firmware_info: Incomplete
    def __init__(self, device: str, config_entry: ConfigEntry, update_coordinator: FirmwareUpdateCoordinator, entity_description: FirmwareUpdateEntityDescription) -> None: ...
    @callback
    def _firmware_info_callback(self, firmware_info: FirmwareInfo) -> None: ...
