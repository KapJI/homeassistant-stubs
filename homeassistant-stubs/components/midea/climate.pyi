from .const import DOMAIN as DOMAIN, FanSpeed as FanSpeed
from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, FAN_AUTO as FAN_AUTO, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE, PRESET_SLEEP as PRESET_SLEEP, SWING_BOTH as SWING_BOTH, SWING_HORIZONTAL as SWING_HORIZONTAL, SWING_OFF as SWING_OFF, SWING_ON as SWING_ON, SWING_VERTICAL as SWING_VERTICAL
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from midealocal.devices.ac import MideaACDevice
from midealocal.devices.c3 import DeviceAttributes as C3Attributes, MideaC3Device
from midealocal.devices.cc import MideaCCDevice
from midealocal.devices.cf import MideaCFDevice
from midealocal.devices.fb import MideaFBDevice
from typing import Any, override

PARALLEL_UPDATES: int
TEMPERATURE_MAX: int
TEMPERATURE_MIN: int
TEMPERATURE_MAX_C3: int
TEMPERATURE_MIN_C3: int
FAN_SILENT: str
FAN_FULL_SPEED: str
FEATURES_TARGET_AND_POWER: Incomplete
type MideaClimateDevice = MideaACDevice | MideaCCDevice | MideaCFDevice | MideaC3Device | MideaFBDevice

@dataclass(kw_only=True, frozen=True)
class MideaClimateEntityDescription(ClimateEntityDescription):
    models: list[DeviceType]
    zone: int | None = ...

CLIMATE_ENTITIES: list[MideaClimateEntityDescription]
_PRESET_TO_ATTR: dict[str, str]
_ATTR_TO_PRESET: dict[str, str]
_SWING_MODE_MAP: dict[str, tuple[bool, bool]]
_SWING_STATE_MAP: dict[tuple[bool, bool], str]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaClimate(MideaEntity, ClimateEntity):
    _device: MideaClimateDevice
    _attr_supported_features: Incomplete
    _attr_max_temp = TEMPERATURE_MAX
    _attr_min_temp = TEMPERATURE_MIN
    _attr_temperature_unit: Incomplete
    _zone: int | None
    _protocol_hvac_modes: dict[int, HVACMode]
    def __init__(self, device: MideaClimateDevice, description: MideaClimateEntityDescription) -> None: ...
    def _float_attribute(self, attr: str) -> float | None: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode | None: ...
    def _protocol_mode_to_hvac(self, mode: int) -> HVACMode | None: ...
    def _hvac_to_protocol_mode(self, hvac_mode: HVACMode) -> int: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @override
    def set_temperature(self, **kwargs: Any) -> None: ...
    @override
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    def set_preset_mode(self, preset_mode: str) -> None: ...

class MideaACClimate(MideaClimate):
    _device: MideaACDevice
    _fan_thresholds: tuple[tuple[int, str], ...]
    _fan_speeds: dict[str, int]
    _attr_fan_modes: list[str]
    _attr_swing_modes: list[str]
    _attr_preset_modes: Incomplete
    _protocol_hvac_modes: Incomplete
    _attr_target_temperature_step: Incomplete
    def __init__(self, device: MideaACDevice, description: MideaClimateEntityDescription) -> None: ...
    @property
    @override
    def hvac_modes(self) -> list[HVACMode]: ...
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @property
    @override
    def fan_mode(self) -> str | None: ...
    @property
    @override
    def swing_mode(self) -> str | None: ...
    @property
    @override
    def current_humidity(self) -> float | None: ...
    @override
    def set_fan_mode(self, fan_mode: str) -> None: ...
    @override
    def set_swing_mode(self, swing_mode: str) -> None: ...

class MideaCCClimate(MideaClimate):
    _device: MideaCCDevice
    _attr_hvac_modes: Incomplete
    _attr_swing_modes: Incomplete
    _attr_preset_modes: Incomplete
    _protocol_hvac_modes: Incomplete
    def __init__(self, device: MideaCCDevice, description: MideaClimateEntityDescription) -> None: ...
    @property
    @override
    def fan_modes(self) -> list[str] | None: ...
    @property
    @override
    def fan_mode(self) -> str | None: ...
    @property
    @override
    def target_temperature_step(self) -> float | None: ...
    @property
    @override
    def swing_mode(self) -> str | None: ...
    @override
    def set_fan_mode(self, fan_mode: str) -> None: ...
    @override
    def set_swing_mode(self, swing_mode: str) -> None: ...

class MideaCFClimate(MideaClimate):
    _device: MideaCFDevice
    _attr_hvac_modes: Incomplete
    _attr_target_temperature_step: float | None
    _attr_supported_features = FEATURES_TARGET_AND_POWER
    _protocol_hvac_modes: Incomplete
    def __init__(self, device: MideaCFDevice, description: MideaClimateEntityDescription) -> None: ...
    @override
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...

class MideaC3Climate(MideaClimate):
    _device: MideaC3Device
    _zone: int
    _powers: tuple[C3Attributes, ...]
    _attr_hvac_modes: Incomplete
    _protocol_hvac_modes: Incomplete
    _power_attr: Incomplete
    def __init__(self, device: MideaC3Device, description: MideaClimateEntityDescription, zone: int) -> None: ...
    def _temperature(self, *, minimum: bool) -> list[float]: ...
    _attr_supported_features = FEATURES_TARGET_AND_POWER
    @property
    @override
    def target_temperature_step(self) -> float: ...
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @override
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...

class MideaFBClimate(MideaClimate):
    _device: MideaFBDevice
    _attr_hvac_modes: Incomplete
    _attr_max_temp: int
    _attr_min_temp: int
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_preset_modes: list[str]
    def __init__(self, device: MideaFBDevice, description: MideaClimateEntityDescription) -> None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @override
    def set_temperature(self, **kwargs: Any) -> None: ...
    @override
    def set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    def set_preset_mode(self, preset_mode: str) -> None: ...
