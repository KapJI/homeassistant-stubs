from homeassistant.const import LENGTH as LENGTH, LENGTH_CENTIMETERS as LENGTH_CENTIMETERS, LENGTH_FEET as LENGTH_FEET, LENGTH_INCHES as LENGTH_INCHES, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_METERS as LENGTH_METERS, LENGTH_MILES as LENGTH_MILES, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, LENGTH_YARD as LENGTH_YARD, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE
from typing import Any, Callable

VALID_UNITS: Any
TO_METERS: dict[str, Callable[[float], float]]
METERS_TO: dict[str, Callable[[float], float]]

def convert(value: float, unit_1: str, unit_2: str) -> float: ...
