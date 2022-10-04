from _typeshed import Incomplete
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_MEGA_WATT_HOUR as ENERGY_MEGA_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, LENGTH_CENTIMETERS as LENGTH_CENTIMETERS, LENGTH_FEET as LENGTH_FEET, LENGTH_INCHES as LENGTH_INCHES, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_METERS as LENGTH_METERS, LENGTH_MILES as LENGTH_MILES, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, LENGTH_YARD as LENGTH_YARD, MASS_GRAMS as MASS_GRAMS, MASS_KILOGRAMS as MASS_KILOGRAMS, MASS_MICROGRAMS as MASS_MICROGRAMS, MASS_MILLIGRAMS as MASS_MILLIGRAMS, MASS_OUNCES as MASS_OUNCES, MASS_POUNDS as MASS_POUNDS, POWER_KILO_WATT as POWER_KILO_WATT, POWER_WATT as POWER_WATT, PRESSURE_BAR as PRESSURE_BAR, PRESSURE_CBAR as PRESSURE_CBAR, PRESSURE_HPA as PRESSURE_HPA, PRESSURE_INHG as PRESSURE_INHG, PRESSURE_KPA as PRESSURE_KPA, PRESSURE_MBAR as PRESSURE_MBAR, PRESSURE_MMHG as PRESSURE_MMHG, PRESSURE_PA as PRESSURE_PA, PRESSURE_PSI as PRESSURE_PSI, SPEED_FEET_PER_SECOND as SPEED_FEET_PER_SECOND, SPEED_INCHES_PER_DAY as SPEED_INCHES_PER_DAY, SPEED_INCHES_PER_HOUR as SPEED_INCHES_PER_HOUR, SPEED_KILOMETERS_PER_HOUR as SPEED_KILOMETERS_PER_HOUR, SPEED_KNOTS as SPEED_KNOTS, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, SPEED_MILLIMETERS_PER_DAY as SPEED_MILLIMETERS_PER_DAY, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, TEMP_KELVIN as TEMP_KELVIN, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS, VOLUME_FLUID_OUNCE as VOLUME_FLUID_OUNCE, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS, VOLUME_MILLILITERS as VOLUME_MILLILITERS
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_MM_TO_M: float
_CM_TO_M: float
_KM_TO_M: int
_IN_TO_M: float
_FOOT_TO_M: Incomplete
_YARD_TO_M: Incomplete
_MILE_TO_M: Incomplete
_NAUTICAL_MILE_TO_M: int
_HRS_TO_SECS: Incomplete
_DAYS_TO_SECS: Incomplete
_POUND_TO_G: float
_OUNCE_TO_G: Incomplete
_L_TO_CUBIC_METER: float
_ML_TO_CUBIC_METER: Incomplete
_GALLON_TO_CUBIC_METER: Incomplete
_FLUID_OUNCE_TO_CUBIC_METER: Incomplete
_CUBIC_FOOT_TO_CUBIC_METER: Incomplete

class BaseUnitConverter:
    UNIT_CLASS: str
    NORMALIZED_UNIT: str
    VALID_UNITS: set[str]
    _UNIT_CONVERSION: dict[str, float]
    @classmethod
    def convert(cls, value: float, from_unit: str, to_unit: str) -> float: ...
    @classmethod
    def get_unit_ratio(cls, from_unit: str, to_unit: str) -> float: ...

class DistanceConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete

class EnergyConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete

class MassConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete

class PowerConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete

class PressureConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete

class SpeedConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete

class TemperatureConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    VALID_UNITS: Incomplete
    _UNIT_CONVERSION: Incomplete
    @classmethod
    def convert(cls, value: float, from_unit: str, to_unit: str) -> float: ...
    @classmethod
    def convert_interval(cls, interval: float, from_unit: str, to_unit: str) -> float: ...
    @classmethod
    def _fahrenheit_to_celsius(cls, fahrenheit: float) -> float: ...
    @classmethod
    def _kelvin_to_celsius(cls, kelvin: float) -> float: ...
    @classmethod
    def _celsius_to_fahrenheit(cls, celsius: float) -> float: ...
    @classmethod
    def _celsius_to_kelvin(cls, celsius: float) -> float: ...

class VolumeConverter(BaseUnitConverter):
    UNIT_CLASS: str
    NORMALIZED_UNIT: Incomplete
    _UNIT_CONVERSION: dict[str, float]
    VALID_UNITS: Incomplete
