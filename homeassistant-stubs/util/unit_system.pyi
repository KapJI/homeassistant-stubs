from homeassistant.const import CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, CONF_UNIT_SYSTEM_METRIC as CONF_UNIT_SYSTEM_METRIC, LENGTH as LENGTH, LENGTH_KILOMETERS as LENGTH_KILOMETERS, LENGTH_MILES as LENGTH_MILES, MASS as MASS, MASS_GRAMS as MASS_GRAMS, MASS_KILOGRAMS as MASS_KILOGRAMS, MASS_OUNCES as MASS_OUNCES, MASS_POUNDS as MASS_POUNDS, PRESSURE as PRESSURE, PRESSURE_PA as PRESSURE_PA, PRESSURE_PSI as PRESSURE_PSI, TEMPERATURE as TEMPERATURE, TEMP_CELSIUS as TEMP_CELSIUS, TEMP_FAHRENHEIT as TEMP_FAHRENHEIT, UNIT_NOT_RECOGNIZED_TEMPLATE as UNIT_NOT_RECOGNIZED_TEMPLATE, VOLUME as VOLUME, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from typing import Any

LENGTH_UNITS: Any
MASS_UNITS: Any
PRESSURE_UNITS: Any
VOLUME_UNITS: Any
TEMPERATURE_UNITS: Any

def is_valid_unit(unit: str, unit_type: str) -> bool: ...

class UnitSystem:
    name: Any
    temperature_unit: Any
    length_unit: Any
    mass_unit: Any
    pressure_unit: Any
    volume_unit: Any
    def __init__(self, name: str, temperature: str, length: str, volume: str, mass: str, pressure: str) -> None: ...
    @property
    def is_metric(self) -> bool: ...
    def temperature(self, temperature: float, from_unit: str) -> float: ...
    def length(self, length: Union[float, None], from_unit: str) -> float: ...
    def pressure(self, pressure: Union[float, None], from_unit: str) -> float: ...
    def volume(self, volume: Union[float, None], from_unit: str) -> float: ...
    def as_dict(self) -> dict[str, str]: ...

METRIC_SYSTEM: Any
IMPERIAL_SYSTEM: Any
