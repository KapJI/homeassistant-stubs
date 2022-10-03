from .unit_conversion import DistanceConverter as DistanceConverter
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import LENGTH as LENGTH, LENGTH_CENTIMETERS as LENGTH_CENTIMETERS, LENGTH_FEET as LENGTH_FEET, LENGTH_INCHES as LENGTH_INCHES, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_METERS as LENGTH_METERS, LENGTH_MILES as LENGTH_MILES, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, LENGTH_YARD as LENGTH_YARD, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE
from homeassistant.helpers.frame import report as report

VALID_UNITS: Incomplete
TO_METERS: dict[str, Callable[[float], float]]
METERS_TO: dict[str, Callable[[float], float]]

def convert(value: float, from_unit: str, to_unit: str) -> float: ...
