from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from typing import Any, override

OVERKIZ_TO_PRESET_MODES: dict[str, str]
PRESET_MODES_TO_OVERKIZ: Incomplete
OVERKIZ_TO_HVAC_MODES: dict[str, HVACMode]
HVAC_MODES_TO_OVERKIZ: Incomplete
OVERKIZ_TO_HVAC_ACTION: dict[str, HVACAction]
MAP_PRESET_TEMPERATURES: dict[str, str]
SETPOINT_MODE_TO_OVERKIZ_COMMAND: dict[str, str]
TEMPERATURE_SENSOR_DEVICE_INDEX: int

class SomfyHeatingTemperatureInterface(OverkizEntity, ClimateEntity):
    _attr_temperature_unit: Incomplete
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_min_temp: float
    _attr_max_temp: float
    temperature_device: Incomplete
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @property
    @override
    def hvac_action(self) -> HVACAction | None: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
