from .unit_conversion import SpeedConverter as SpeedConverter
from _typeshed import Incomplete
from homeassistant.const import SPEED as SPEED, SPEED_FEET_PER_SECOND as SPEED_FEET_PER_SECOND, SPEED_INCHES_PER_DAY as SPEED_INCHES_PER_DAY, SPEED_INCHES_PER_HOUR as SPEED_INCHES_PER_HOUR, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, SPEED_KNOTS as SPEED_KNOTS, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, SPEED_MILLIMETERS_PER_DAY as SPEED_MILLIMETERS_PER_DAY, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE
from homeassistant.helpers.frame import report as report

UNIT_CONVERSION: dict[Union[str, None], float]
VALID_UNITS: Incomplete

def convert(value: float, from_unit: str, to_unit: str) -> float: ...
