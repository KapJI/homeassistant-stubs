from . import STATE_ATTR_AZIMUTH as STATE_ATTR_AZIMUTH, STATE_ATTR_ELEVATION as STATE_ATTR_ELEVATION, STATE_ATTR_NEXT_DAWN as STATE_ATTR_NEXT_DAWN, STATE_ATTR_NEXT_DUSK as STATE_ATTR_NEXT_DUSK, STATE_ATTR_NEXT_MIDNIGHT as STATE_ATTR_NEXT_MIDNIGHT, STATE_ATTR_NEXT_NOON as STATE_ATTR_NEXT_NOON, STATE_ATTR_NEXT_RISING as STATE_ATTR_NEXT_RISING, STATE_ATTR_NEXT_SETTING as STATE_ATTR_NEXT_SETTING, STATE_ATTR_RISING as STATE_ATTR_RISING
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

def exclude_attributes(hass: HomeAssistant) -> set[str]: ...