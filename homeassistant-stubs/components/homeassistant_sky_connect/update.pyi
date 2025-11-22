from . import HomeAssistantSkyConnectConfigEntry as HomeAssistantSkyConnectConfigEntry
from .config_flow import SkyConnectFirmwareMixin as SkyConnectFirmwareMixin
from .const import DOMAIN as DOMAIN, FIRMWARE as FIRMWARE, FIRMWARE_VERSION as FIRMWARE_VERSION, HardwareVariant as HardwareVariant, PRODUCT as PRODUCT, SERIAL_NUMBER as SERIAL_NUMBER
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from homeassistant.components.homeassistant_hardware.update import BaseFirmwareUpdateEntity as BaseFirmwareUpdateEntity, FirmwareUpdateEntityDescription as FirmwareUpdateEntityDescription
from homeassistant.components.homeassistant_hardware.util import ApplicationType as ApplicationType, FirmwareInfo as FirmwareInfo
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete
FIRMWARE_ENTITY_DESCRIPTIONS: dict[ApplicationType | None, FirmwareUpdateEntityDescription]

def _async_create_update_entity(hass: HomeAssistant, config_entry: HomeAssistantSkyConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> FirmwareUpdateEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeAssistantSkyConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FirmwareUpdateEntity(BaseFirmwareUpdateEntity):
    BOOTLOADER_RESET_METHODS: Incomplete
    APPLICATION_PROBE_METHODS: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _current_firmware_info: Incomplete
    def __init__(self, device: str, config_entry: HomeAssistantSkyConnectConfigEntry, update_coordinator: FirmwareUpdateCoordinator, entity_description: FirmwareUpdateEntityDescription) -> None: ...
    def _update_attributes(self) -> None: ...
    @callback
    def _firmware_info_callback(self, firmware_info: FirmwareInfo) -> None: ...
