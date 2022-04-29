from _typeshed import Incomplete
from homeassistant.const import ACCUMULATED_PRECIPITATION as ACCUMULATED_PRECIPITATION, CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, CONF_UNIT_SYSTEM_METRIC as CONF_UNIT_SYSTEM_METRIC, LENGTH as LENGTH, LENGTH_INCHES as LENGTH_INCHES, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, MASS as MASS, MASS_GRAMS as MASS_GRAMS, MASS_KILOGRAMS as MASS_KILOGRAMS, MASS_OUNCES as MASS_OUNCES, MASS_POUNDS as MASS_POUNDS, PRESSURE as PRESSURE, PRESSURE_PA as PRESSURE_PA, PRESSURE_PSI as PRESSURE_PSI, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, SPEED_MILES_PER_HOUR as SPEED_MILES_PER_HOUR, TEMPERATURE as TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, VOLUME as VOLUME, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS, WIND_SPEED as WIND_SPEED

LENGTH_UNITS: Incomplete
MASS_UNITS: tuple[str, ...]
PRESSURE_UNITS: Incomplete
VOLUME_UNITS: Incomplete
WIND_SPEED_UNITS: Incomplete
TEMPERATURE_UNITS: tuple[str, ...]

def is_valid_unit(unit: str, unit_type: str) -> bool: ...

class UnitSystem:
    name: Incomplete
    accumulated_precipitation_unit: Incomplete
    temperature_unit: Incomplete
    length_unit: Incomplete
    mass_unit: Incomplete
    pressure_unit: Incomplete
    volume_unit: Incomplete
    wind_speed_unit: Incomplete
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

METRIC_SYSTEM: Incomplete
IMPERIAL_SYSTEM: Incomplete
