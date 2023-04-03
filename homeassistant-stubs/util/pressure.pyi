from .unit_conversion import PressureConverter as PressureConverter
from _typeshed import Incomplete
from homeassistant.const import PRESSURE as PRESSURE, PRESSURE_BAR as PRESSURE_BAR, PRESSURE_CBAR as PRESSURE_CBAR, PRESSURE_HPA as PRESSURE_HPA, PRESSURE_INHG as PRESSURE_INHG, PRESSURE_KPA as PRESSURE_KPA, PRESSURE_MBAR as PRESSURE_MBAR, PRESSURE_MMHG as PRESSURE_MMHG, PRESSURE_PA as PRESSURE_PA, PRESSURE_PSI as PRESSURE_PSI, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE
from homeassistant.helpers.frame import report as report

UNIT_CONVERSION: dict[str | None, float]
VALID_UNITS: Incomplete

def convert(value: float, from_unit: str, to_unit: str) -> float: ...
