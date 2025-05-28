from . import websocket_api as websocket_api
from .const import DATA_HARDWARE as DATA_HARDWARE, DOMAIN as DOMAIN
from .hardware import async_process_hardware_platforms as async_process_hardware_platforms
from .models import HardwareData as HardwareData, SystemStatus as SystemStatus
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
