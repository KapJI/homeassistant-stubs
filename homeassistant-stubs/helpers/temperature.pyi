from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS
from homeassistant.core import HomeAssistant as HomeAssistant

def display_temp(hass: HomeAssistant, temperature: Union[float, None], unit: str, precision: float) -> Union[float, None]: ...
