from .unit_conversion import DistanceConverter as DistanceConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter, VolumeConverter as VolumeConverter
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import ACCUMULATED_PRECIPITATION as ACCUMULATED_PRECIPITATION, LENGTH as LENGTH, MASS as MASS, PRESSURE as PRESSURE, TEMPERATURE as TEMPERATURE, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfVolume as UnitOfVolume, VOLUME as VOLUME, WIND_SPEED as WIND_SPEED
from homeassistant.helpers.frame import report as report
from typing import Final

_CONF_UNIT_SYSTEM_IMPERIAL: Final[str]
_CONF_UNIT_SYSTEM_METRIC: Final[str]
_CONF_UNIT_SYSTEM_US_CUSTOMARY: Final[str]
LENGTH_UNITS: Incomplete
MASS_UNITS: set[str]
PRESSURE_UNITS: Incomplete
VOLUME_UNITS: Incomplete
WIND_SPEED_UNITS: Incomplete
TEMPERATURE_UNITS: set[str]

def _is_valid_unit(unit: str, unit_type: str) -> bool: ...

class UnitSystem:
    _name: Incomplete
    accumulated_precipitation_unit: Incomplete
    temperature_unit: Incomplete
    length_unit: Incomplete
    mass_unit: Incomplete
    pressure_unit: Incomplete
    volume_unit: Incomplete
    wind_speed_unit: Incomplete
    _conversions: Incomplete
    def __init__(self, name: str, *, accumulated_precipitation: str, conversions: dict[tuple[Union[SensorDeviceClass, str, None], Union[str, None]], str], length: str, mass: str, pressure: str, temperature: str, volume: str, wind_speed: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def is_metric(self) -> bool: ...
    def temperature(self, temperature: float, from_unit: str) -> float: ...
    def length(self, length: Union[float, None], from_unit: str) -> float: ...
    def accumulated_precipitation(self, precip: Union[float, None], from_unit: str) -> float: ...
    def pressure(self, pressure: Union[float, None], from_unit: str) -> float: ...
    def wind_speed(self, wind_speed: Union[float, None], from_unit: str) -> float: ...
    def volume(self, volume: Union[float, None], from_unit: str) -> float: ...
    def as_dict(self) -> dict[str, str]: ...
    def get_converted_unit(self, device_class: Union[SensorDeviceClass, str, None], original_unit: Union[str, None]) -> Union[str, None]: ...

def get_unit_system(key: str) -> UnitSystem: ...
def _deprecated_unit_system(value: str) -> str: ...

validate_unit_system: Incomplete
METRIC_SYSTEM: Incomplete
US_CUSTOMARY_SYSTEM: Incomplete
IMPERIAL_SYSTEM = US_CUSTOMARY_SYSTEM
