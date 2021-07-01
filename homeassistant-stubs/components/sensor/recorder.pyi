import datetime
from . import DOMAIN as DOMAIN
from homeassistant.components.recorder import history as history, statistics as statistics
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_MONETARY as DEVICE_CLASS_MONETARY, DEVICE_CLASS_PRESSURE as DEVICE_CLASS_PRESSURE, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT
from homeassistant.const import ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, POWER_KILO_WATT as POWER_KILO_WATT, POWER_WATT as POWER_WATT, PRESSURE_BAR as PRESSURE_BAR, PRESSURE_HPA as PRESSURE_HPA, PRESSURE_INHG as PRESSURE_INHG, PRESSURE_MBAR as PRESSURE_MBAR, PRESSURE_PA as PRESSURE_PA, PRESSURE_PSI as PRESSURE_PSI, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TEMP_KELVIN as TEMP_KELVIN
from homeassistant.core import HomeAssistant as HomeAssistant, State as State
from typing import Any, Callable

_LOGGER: Any
DEVICE_CLASS_STATISTICS: Any
DEVICE_CLASS_UNITS: Any
UNIT_CONVERSIONS: dict[str, dict[str, Callable]]
WARN_UNSUPPORTED_UNIT: Any

def _get_entities(hass: HomeAssistant) -> list[tuple[str, str]]: ...
def _is_number(s: str) -> bool: ...
def _time_weighted_average(fstates: list[tuple[float, State]], start: datetime.datetime, end: datetime.datetime) -> float: ...
def _normalize_states(entity_history: list[State], device_class: str, entity_id: str) -> tuple[Union[str, None], list[tuple[float, State]]]: ...
def compile_statistics(hass: HomeAssistant, start: datetime.datetime, end: datetime.datetime) -> dict: ...
