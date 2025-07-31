from . import IronOSConfigEntry as IronOSConfigEntry
from .const import MAX_TEMP as MAX_TEMP, MAX_TEMP_F as MAX_TEMP_F, MIN_BOOST_TEMP as MIN_BOOST_TEMP, MIN_BOOST_TEMP_F as MIN_BOOST_TEMP_F, MIN_TEMP as MIN_TEMP, MIN_TEMP_F as MIN_TEMP_F
from .coordinator import IronOSCoordinators as IronOSCoordinators
from .entity import IronOSBaseEntity as IronOSBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from enum import StrEnum
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from pynecil import CharSetting, LiveDataResponse as LiveDataResponse, SettingsDataResponse as SettingsDataResponse

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class IronOSNumberEntityDescription(NumberEntityDescription):
    value_fn: Callable[[LiveDataResponse, SettingsDataResponse], float | int | None]
    characteristic: CharSetting
    raw_value_fn: Callable[[float], float | int] | None = ...
    native_max_value_f: float | None = ...
    native_min_value_f: float | None = ...

class PinecilNumber(StrEnum):
    SETPOINT_TEMP = 'setpoint_temperature'
    SLEEP_TEMP = 'sleep_temperature'
    SLEEP_TIMEOUT = 'sleep_timeout'
    QC_MAX_VOLTAGE = 'qc_max_voltage'
    PD_TIMEOUT = 'pd_timeout'
    BOOST_TEMP = 'boost_temp'
    SHUTDOWN_TIMEOUT = 'shutdown_timeout'
    DISPLAY_BRIGHTNESS = 'display_brightness'
    POWER_LIMIT = 'power_limit'
    CALIBRATION_OFFSET = 'calibration_offset'
    HALL_SENSITIVITY = 'hall_sensitivity'
    MIN_VOLTAGE_PER_CELL = 'min_voltage_per_cell'
    ACCEL_SENSITIVITY = 'accel_sensitivity'
    KEEP_AWAKE_PULSE_POWER = 'keep_awake_pulse_power'
    KEEP_AWAKE_PULSE_DELAY = 'keep_awake_pulse_delay'
    KEEP_AWAKE_PULSE_DURATION = 'keep_awake_pulse_duration'
    VOLTAGE_DIV = 'voltage_div'
    TEMP_INCREMENT_SHORT = 'temp_increment_short'
    TEMP_INCREMENT_LONG = 'temp_increment_long'
    HALL_EFFECT_SLEEP_TIME = 'hall_effect_sleep_time'

def multiply(value: float | None, multiplier: float) -> float | None: ...

PINECIL_NUMBER_DESCRIPTIONS: tuple[IronOSNumberEntityDescription, ...]
PINECIL_NUMBER_DESCRIPTIONS_V223: tuple[IronOSNumberEntityDescription, ...]
PINECIL_TEMP_NUMBER_DESCRIPTIONS: tuple[IronOSNumberEntityDescription, ...]
PINECIL_SETPOINT_NUMBER_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: IronOSConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IronOSNumberEntity(IronOSBaseEntity, NumberEntity):
    entity_description: IronOSNumberEntityDescription
    settings: Incomplete
    def __init__(self, coordinators: IronOSCoordinators, entity_description: IronOSNumberEntityDescription) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
    @property
    def native_value(self) -> float | int | None: ...
    async def async_added_to_hass(self) -> None: ...

class IronOSTemperatureNumberEntity(IronOSNumberEntity):
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_min_value(self) -> float: ...
    @property
    def native_max_value(self) -> float: ...
    @property
    def available(self) -> bool: ...

class IronOSSetpointNumberEntity(IronOSTemperatureNumberEntity):
    @property
    def native_max_value(self) -> float: ...
