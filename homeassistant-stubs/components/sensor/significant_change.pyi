from . import DEVICE_CLASS_AQI as DEVICE_CLASS_AQI, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CO as DEVICE_CLASS_CO, DEVICE_CLASS_CO2 as DEVICE_CLASS_CO2, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_PM10 as DEVICE_CLASS_PM10, DEVICE_CLASS_PM25 as DEVICE_CLASS_PM25, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS as DEVICE_CLASS_VOLATILE_ORGANIC_COMPOUNDS
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.significant_change import check_absolute_change as check_absolute_change, check_percentage_change as check_percentage_change
from typing import Any

def _absolute_and_relative_change(old_state: Union[int, float, None], new_state: Union[int, float, None], absolute_change: Union[int, float], percentage_change: Union[int, float]) -> bool: ...
def async_check_significant_change(hass: HomeAssistant, old_state: str, old_attrs: dict, new_state: str, new_attrs: dict, **kwargs: Any) -> Union[bool, None]: ...
