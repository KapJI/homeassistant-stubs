from . import HomeAssistantYellowConfigEntry as HomeAssistantYellowConfigEntry
from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MODEL as MODEL
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.coordinator import FirmwareUpdateCoordinator as FirmwareUpdateCoordinator
from homeassistant.components.homeassistant_hardware.switch import BaseBetaFirmwareSwitch as BaseBetaFirmwareSwitch
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeAssistantYellowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BetaFirmwareSwitch(BaseBetaFirmwareSwitch):
    _attr_unique_id: str
    _attr_device_info: Incomplete
    def __init__(self, coordinator: FirmwareUpdateCoordinator, config_entry: HomeAssistantYellowConfigEntry) -> None: ...
