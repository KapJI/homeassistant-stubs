from .const import DOMAIN as DOMAIN
from .hardware import BOARD_NAMES as BOARD_NAMES, MODELS as MODELS
from homeassistant.components.hassio import HassioNotReadyError as HassioNotReadyError, get_os_info as get_os_info
from homeassistant.components.homeassistant_hardware.update import RaspberryPiFirmwareUpdateEntity as RaspberryPiFirmwareUpdateEntity
from homeassistant.components.homeassistant_hardware.util import BOARDS_WITH_RASPBERRYPI_FIRMWARE as BOARDS_WITH_RASPBERRYPI_FIRMWARE, async_get_raspberry_pi_firmware_info as async_get_raspberry_pi_firmware_info
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
