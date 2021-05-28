import datetime
from . import DOMAIN as DOMAIN
from homeassistant.components.recorder import history as history, statistics as statistics
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from typing import Any

DEVICE_CLASS_STATISTICS: Any

def _get_entities(hass: HomeAssistant) -> list[tuple[str, str]]: ...
def _is_number(s: str) -> bool: ...
def _time_weighted_average(fstates: list[tuple[float, State]], start: datetime.datetime, end: datetime.datetime) -> float: ...
def compile_statistics(hass: HomeAssistant, start: datetime.datetime, end: datetime.datetime) -> dict: ...
