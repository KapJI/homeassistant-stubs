from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntry as DeviceEntry

def get_device(hass: HomeAssistant | None, unique_id: str) -> DeviceEntry | None: ...
