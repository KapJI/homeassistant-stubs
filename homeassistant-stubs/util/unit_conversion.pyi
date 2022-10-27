from _typeshed import Incomplete
from homeassistant.const import UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, UnitOfEnergy as UnitOfEnergy, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolumetricFlux as UnitOfVolumetricFlux, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS, VOLUME_FLUID_OUNCE as VOLUME_FLUID_OUNCE, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS, VOLUME_MILLILITERS as VOLUME_MILLILITERS
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
_STANDARD_GRAVITY: float
_MERCURY_DENSITY: float
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
