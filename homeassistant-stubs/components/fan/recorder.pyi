from . import ATTR_PRESET_MODES as ATTR_PRESET_MODES
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...
