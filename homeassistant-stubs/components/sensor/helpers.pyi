from . import SensorDeviceClass as SensorDeviceClass
from datetime import date, datetime
from homeassistant.core import callback as callback
from typing import Any

_LOGGER: Any

def async_parse_date_datetime(value: str, entity_id: str, device_class: Union[SensorDeviceClass, str, None]) -> Union[datetime, date, None]: ...
