from .const import DOMAIN as DOMAIN
from homeassistant.components.hardware.models import HardwareInfo as HardwareInfo, USBInfo as USBInfo
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

DOCUMENTATION_URL: str
DONGLE_NAME: str

def async_info(hass: HomeAssistant) -> list[HardwareInfo]: ...
