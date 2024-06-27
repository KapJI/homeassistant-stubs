from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE_REACTIVE as POWER_VOLT_AMPERE_REACTIVE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfApparentPower as UnitOfApparentPower, UnitOfConductivity as UnitOfConductivity, UnitOfDataRate as UnitOfDataRate, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfInformation as UnitOfInformation, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.util.unit_conversion import BaseUnitConverter as BaseUnitConverter, TemperatureConverter as TemperatureConverter, VolumeFlowRateConverter as VolumeFlowRateConverter
from typing import Final

ATTR_VALUE: str
ATTR_MIN: str
ATTR_MAX: str
ATTR_STEP: str
ATTR_STEP_VALIDATION: str
DEFAULT_MIN_VALUE: float
DEFAULT_MAX_VALUE: float
DEFAULT_STEP: float
DOMAIN: str
SERVICE_SET_VALUE: str

class NumberMode(StrEnum):
    AUTO: str
    BOX: str
    SLIDER: str

_DEPRECATED_MODE_AUTO: Final[Incomplete]
_DEPRECATED_MODE_BOX: Final[Incomplete]
_DEPRECATED_MODE_SLIDER: Final[Incomplete]

class NumberDeviceClass(StrEnum):
    APPARENT_POWER: str
    AQI: str
    ATMOSPHERIC_PRESSURE: str
    BATTERY: str
    CO: str
    CO2: str
    CONDUCTIVITY: str
    CURRENT: str
    DATA_RATE: str
    DATA_SIZE: str
    DISTANCE: str
    DURATION: str
    ENERGY: str
    ENERGY_STORAGE: str
    FREQUENCY: str
    GAS: str
    HUMIDITY: str
    ILLUMINANCE: str
    IRRADIANCE: str
    MOISTURE: str
    MONETARY: str
    NITROGEN_DIOXIDE: str
    NITROGEN_MONOXIDE: str
    NITROUS_OXIDE: str
    OZONE: str
    PH: str
    PM1: str
    PM10: str
    PM25: str
    POWER_FACTOR: str
    POWER: str
    PRECIPITATION: str
    PRECIPITATION_INTENSITY: str
    PRESSURE: str
    REACTIVE_POWER: str
    SIGNAL_STRENGTH: str
    SOUND_PRESSURE: str
    SPEED: str
    SULPHUR_DIOXIDE: str
    TEMPERATURE: str
    VOLATILE_ORGANIC_COMPOUNDS: str
    VOLATILE_ORGANIC_COMPOUNDS_PARTS: str
    VOLTAGE: str
    VOLUME: str
    VOLUME_STORAGE: str
    VOLUME_FLOW_RATE: str
    WATER: str
    WEIGHT: str
    WIND_SPEED: str

DEVICE_CLASSES_SCHEMA: Final[Incomplete]
DEVICE_CLASS_UNITS: dict[NumberDeviceClass, set[type[StrEnum] | str | None]]
UNIT_CONVERTERS: dict[NumberDeviceClass, type[BaseUnitConverter]]
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
