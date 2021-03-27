from homeassistant.const import PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Optional

def display_temp(hass: HomeAssistant, temperature: Optional[float], unit: str, precision: float) -> Optional[float]: ...
