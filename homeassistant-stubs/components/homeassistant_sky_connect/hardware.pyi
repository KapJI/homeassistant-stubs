from .config_flow import HomeAssistantSkyConnectConfigFlow as HomeAssistantSkyConnectConfigFlow
from .const import DOMAIN as DOMAIN
from .util import get_hardware_variant as get_hardware_variant
from _typeshed import Incomplete
from homeassistant.components.hardware.models import HardwareInfo as HardwareInfo, USBInfo as USBInfo
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

DOCUMENTATION_URL: str
EXPECTED_ENTRY_VERSION: Incomplete

@callback
def async_info(hass: HomeAssistant) -> list[HardwareInfo]: ...
