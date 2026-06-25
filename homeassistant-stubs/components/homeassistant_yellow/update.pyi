from . import HomeAssistantYellowConfigEntry as HomeAssistantYellowConfigEntry
from .const import DOMAIN as DOMAIN, FIRMWARE as FIRMWARE, FIRMWARE_VERSION as FIRMWARE_VERSION, MANUFACTURER as MANUFACTURER, MODEL as MODEL, RADIO_DEVICE as RADIO_DEVICE
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from homeassistant.components.homeassistant_hardware.update import BaseFirmwareUpdateEntity as BaseFirmwareUpdateEntity, FirmwareUpdateEntityDescription as FirmwareUpdateEntityDescription, RaspberryPiFirmwareUpdateEntity as RaspberryPiFirmwareUpdateEntity
from homeassistant.components.homeassistant_hardware.util import ApplicationType as ApplicationType, FirmwareInfo as FirmwareInfo, async_get_raspberry_pi_firmware_info as async_get_raspberry_pi_firmware_info
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override
from universal_silabs_flasher.flasher import YellowFlasher

_LOGGER: Incomplete
FIRMWARE_ENTITY_DESCRIPTIONS: dict[ApplicationType | None, FirmwareUpdateEntityDescription]

def _async_create_update_entity(hass: HomeAssistant, config_entry: HomeAssistantYellowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> FirmwareUpdateEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: HomeAssistantYellowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FirmwareUpdateEntity(BaseFirmwareUpdateEntity):
    _flasher_cls = YellowFlasher
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _current_firmware_info: Incomplete
    def __init__(self, device: str, config_entry: HomeAssistantYellowConfigEntry, update_coordinator: FirmwareUpdateCoordinator, entity_description: FirmwareUpdateEntityDescription) -> None: ...
    @callback
    @override
    def _firmware_info_callback(self, firmware_info: FirmwareInfo) -> None: ...
