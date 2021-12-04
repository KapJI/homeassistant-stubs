from homeassistant.const import ACCUMULATED_PRECIPITATION as ACCUMULATED_PRECIPITATION, CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, CONF_UNIT_SYSTEM_METRIC as CONF_UNIT_SYSTEM_METRIC, LENGTH as LENGTH, LENGTH_INCHES as LENGTH_INCHES, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, MASS as MASS, MASS_GRAMS as MASS_GRAMS, MASS_KILOGRAMS as MASS_KILOGRAMS, MASS_OUNCES as MASS_OUNCES, MASS_POUNDS as MASS_POUNDS, PRESSURE as PRESSURE, PRESSURE_PA as PRESSURE_PA, PRESSURE_PSI as PRESSURE_PSI, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMPERATURE as TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, VOLUME as VOLUME, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS, WIND_SPEED as WIND_SPEED
from typing import Any

LENGTH_UNITS: Any
MASS_UNITS: tuple[str, ...]
PRESSURE_UNITS: Any
VOLUME_UNITS: Any
WIND_SPEED_UNITS: Any
TEMPERATURE_UNITS: tuple[str, ...]

def is_valid_unit(unit: str, unit_type: str) -> bool: ...

class UnitSystem:
    name: Any
    accumulated_precipitation_unit: Any
    temperature_unit: Any
    length_unit: Any
    mass_unit: Any
    pressure_unit: Any
    volume_unit: Any
    wind_speed_unit: Any
    def __init__(self, name: str, temperature: str, length: str, wind_speed: str, volume: str, mass: str, pressure: str, accumulated_precipitation: str) -> None: ...
    @property
    def is_metric(self) -> bool: ...
    def temperature(self, temperature: float, from_unit: str) -> float: ...
    def length(self, length: Union[float, None], from_unit: str) -> float: ...
    def accumulated_precipitation(self, precip: Union[float, None], from_unit: str) -> float: ...
    def pressure(self, pressure: Union[float, None], from_unit: str) -> float: ...
    def wind_speed(self, wind_speed: Union[float, None], from_unit: str) -> float: ...
    def volume(self, volume: Union[float, None], from_unit: str) -> float: ...
    def as_dict(self) -> dict[str, str]: ...

METRIC_SYSTEM: Any
IMPERIAL_SYSTEM: Any
