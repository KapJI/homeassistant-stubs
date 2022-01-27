from . import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_percentage_change as check_percentage_change
from typing import Any

def _absolute_and_relative_change(old_state: Union[int, float, None], new_state: Union[int, float, None], absolute_change: Union[int, float], percentage_change: Union[int, float]) -> bool: ...
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> Union[bool, None]: ...
