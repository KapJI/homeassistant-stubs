from _typeshed import Incomplete
from collections.abc import Callable as Callable
from functools import lru_cache
from homeassistant.const import CONCENTRATION_GRAMS_PER_CUBIC_METER as CONCENTRATION_GRAMS_PER_CUBIC_METER, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER as CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, PERCENTAGE as PERCENTAGE, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, UnitOfApparentPower as UnitOfApparentPower, UnitOfArea as UnitOfArea, UnitOfBloodGlucoseConcentration as UnitOfBloodGlucoseConcentration, UnitOfConductivity as UnitOfConductivity, UnitOfDataRate as UnitOfDataRate, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfEnergyDistance as UnitOfEnergyDistance, UnitOfInformation as UnitOfInformation, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPressure as UnitOfPressure, UnitOfReactiveEnergy as UnitOfReactiveEnergy, UnitOfReactivePower as UnitOfReactivePower, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.deprecation import deprecated_function as deprecated_function

_MM_TO_M: float
_CM_TO_M: float
_KM_TO_M: int
_IN_TO_M: float
_FOOT_TO_M: Incomplete
_YARD_TO_M: Incomplete
_MILE_TO_M: Incomplete
_NAUTICAL_MILE_TO_M: int
_CM2_TO_M2: Incomplete
_MM2_TO_M2: Incomplete
_KM2_TO_M2: Incomplete
_IN2_TO_M2: Incomplete
_FT2_TO_M2: Incomplete
_YD2_TO_M2: Incomplete
_MI2_TO_M2: Incomplete
_ACRE_TO_M2: Incomplete
_HECTARE_TO_M2: Incomplete
_MIN_TO_SEC: int
_HRS_TO_MINUTES: int
_HRS_TO_SECS: Incomplete
_DAYS_TO_HRS: int
_DAYS_TO_SECS: Incomplete
_WH_TO_J: int
_WH_TO_CAL: Incomplete
_POUND_TO_G: float
_OUNCE_TO_G: Incomplete
_STONE_TO_G: Incomplete
_STANDARD_GRAVITY: float
_MERCURY_DENSITY: float
_INH2O_TO_PA: float
_L_TO_CUBIC_METER: float
_ML_TO_CUBIC_METER: Incomplete
_GALLON_TO_CUBIC_METER: Incomplete
_FLUID_OUNCE_TO_CUBIC_METER: Incomplete
_CUBIC_FOOT_TO_CUBIC_METER: Incomplete
_IDEAL_GAS_CONSTANT: float
_AMBIENT_TEMPERATURE: float
_AMBIENT_PRESSURE: int
_AMBIENT_IDEAL_GAS_MOLAR_VOLUME: Incomplete
_CARBON_MONOXIDE_MOLAR_MASS: float

class BaseUnitConverter:
    UNIT_CLASS: str
    VALID_UNITS: set[str | None]
    _UNIT_CONVERSION: dict[str | None, float]
    _UNIT_INVERSES: set[str]
    @classmethod
    def convert(cls, value: float, from_unit: str | None, to_unit: str | None) -> float: ...
    @classmethod
    @lru_cache
    def converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    def _get_from_to_ratio(cls, from_unit: str | None, to_unit: str | None) -> tuple[float, float]: ...
    @classmethod
    @lru_cache
    def converter_factory_allow_none(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float | None], float | None]: ...
    @classmethod
    @lru_cache
    def get_unit_ratio(cls, from_unit: str | None, to_unit: str | None) -> float: ...
    @classmethod
    @lru_cache
    def get_unit_floored_log_ratio(cls, from_unit: str | None, to_unit: str | None) -> float: ...
    @classmethod
    @lru_cache
    def _are_unit_inverses(cls, from_unit: str | None, to_unit: str | None) -> bool: ...

class CarbonMonoxideConcentrationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class DataRateConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class AreaConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class DistanceConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class BloodGlucoseConcentrationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ConductivityConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ElectricCurrentConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ElectricPotentialConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class EnergyConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class EnergyDistanceConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    _UNIT_INVERSES: set[str]
    VALID_UNITS: Incomplete

class InformationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class MassConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ApparentPowerConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class PowerConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class PressureConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ReactiveEnergyConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class ReactivePowerConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class SpeedConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete
    @classmethod
    @lru_cache
    def converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    @lru_cache
    def converter_factory_allow_none(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float | None], float | None]: ...
    @classmethod
    def _converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    def _ms_to_beaufort(cls, ms: float) -> float: ...
    @classmethod
    def _beaufort_to_ms(cls, beaufort: float) -> float: ...

class TemperatureConverter(BaseUnitConverter):
    UNIT_CLASS: str
    VALID_UNITS: Incomplete
    _UNIT_CONVERSION: Incomplete
    @classmethod
    @lru_cache
    def converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    @lru_cache
    def converter_factory_allow_none(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float | None], float | None]: ...
    @classmethod
    def _converter_factory(cls, from_unit: str | None, to_unit: str | None) -> Callable[[float], float]: ...
    @classmethod
    def convert_interval(cls, interval: float, from_unit: str, to_unit: str) -> float: ...
    @classmethod
    def _kelvin_to_fahrenheit(cls, kelvin: float) -> float: ...
    @classmethod
    def _fahrenheit_to_kelvin(cls, fahrenheit: float) -> float: ...
    @classmethod
    def _fahrenheit_to_celsius(cls, fahrenheit: float) -> float: ...
    @classmethod
    def _kelvin_to_celsius(cls, kelvin: float) -> float: ...
    @classmethod
    def _celsius_to_fahrenheit(cls, celsius: float) -> float: ...
    @classmethod
    def _celsius_to_kelvin(cls, celsius: float) -> float: ...

class TemperatureDeltaConverter(BaseUnitConverter):
    UNIT_CLASS: str
    VALID_UNITS: Incomplete
    _UNIT_CONVERSION: Incomplete

class UnitlessRatioConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class MassVolumeConcentrationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class VolumeConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class VolumeFlowRateConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete

class DurationConverter(BaseUnitConverter):
    UNIT_CLASS: str
    _UNIT_CONVERSION: dict[str | None, float]
    VALID_UNITS: Incomplete
