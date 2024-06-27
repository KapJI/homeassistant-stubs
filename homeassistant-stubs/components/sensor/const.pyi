from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, CONCENTRATION_PARTS_PER_MILLION as CONCENTRATION_PARTS_PER_MILLION, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_VOLT_AMPERE_REACTIVE as POWER_VOLT_AMPERE_REACTIVE, SIGNAL_STRENGTH_DECIBELS as SIGNAL_STRENGTH_DECIBELS, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfApparentPower as UnitOfApparentPower, UnitOfConductivity as UnitOfConductivity, UnitOfDataRate as UnitOfDataRate, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfEnergy as UnitOfEnergy, UnitOfFrequency as UnitOfFrequency, UnitOfInformation as UnitOfInformation, UnitOfIrradiance as UnitOfIrradiance, UnitOfLength as UnitOfLength, UnitOfMass as UnitOfMass, UnitOfPower as UnitOfPower, UnitOfPrecipitationDepth as UnitOfPrecipitationDepth, UnitOfPressure as UnitOfPressure, UnitOfSoundPressure as UnitOfSoundPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume, UnitOfVolumeFlowRate as UnitOfVolumeFlowRate, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.helpers.deprecation import DeprecatedConstantEnum as DeprecatedConstantEnum, all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.util.unit_conversion import BaseUnitConverter as BaseUnitConverter, ConductivityConverter as ConductivityConverter, DataRateConverter as DataRateConverter, DistanceConverter as DistanceConverter, DurationConverter as DurationConverter, ElectricCurrentConverter as ElectricCurrentConverter, ElectricPotentialConverter as ElectricPotentialConverter, EnergyConverter as EnergyConverter, InformationConverter as InformationConverter, MassConverter as MassConverter, PowerConverter as PowerConverter, PressureConverter as PressureConverter, SpeedConverter as SpeedConverter, TemperatureConverter as TemperatureConverter, UnitlessRatioConverter as UnitlessRatioConverter, VolumeConverter as VolumeConverter, VolumeFlowRateConverter as VolumeFlowRateConverter
from typing import Final

DOMAIN: Final[str]
CONF_STATE_CLASS: Final[str]
ATTR_LAST_RESET: Final[str]
ATTR_STATE_CLASS: Final[str]
ATTR_OPTIONS: Final[str]

class SensorDeviceClass(StrEnum):
    DATE: str
    ENUM: str
    TIMESTAMP: str
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

NON_NUMERIC_DEVICE_CLASSES: Incomplete
DEVICE_CLASSES_SCHEMA: Final[Incomplete]
DEVICE_CLASSES: Final[list[str]]

class SensorStateClass(StrEnum):
    MEASUREMENT: str
    TOTAL: str
    TOTAL_INCREASING: str

STATE_CLASSES_SCHEMA: Final[Incomplete]
_DEPRECATED_STATE_CLASS_MEASUREMENT: Final[Incomplete]
_DEPRECATED_STATE_CLASS_TOTAL: Final[Incomplete]
_DEPRECATED_STATE_CLASS_TOTAL_INCREASING: Final[Incomplete]
STATE_CLASSES: Final[list[str]]
UNIT_CONVERTERS: dict[SensorDeviceClass | str | None, type[BaseUnitConverter]]
DEVICE_CLASS_UNITS: dict[SensorDeviceClass, set[type[StrEnum] | str | None]]
DEVICE_CLASS_STATE_CLASSES: dict[SensorDeviceClass, set[SensorStateClass]]
__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
