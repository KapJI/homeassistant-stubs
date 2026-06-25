from ..coordinator import OverkizDataUpdateCoordinator as OverkizDataUpdateCoordinator
from ..executor import OverkizExecutor as OverkizExecutor
from .atlantic_pass_apc_heating_zone import AtlanticPassAPCHeatingZone as AtlanticPassAPCHeatingZone
from _typeshed import Incomplete
from homeassistant.components.climate import ATTR_TARGET_TEMP_HIGH as ATTR_TARGET_TEMP_HIGH, ATTR_TARGET_TEMP_LOW as ATTR_TARGET_TEMP_LOW, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_NONE as PRESET_NONE
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES
from propcache.api import cached_property
from pyoverkiz.enums import OverkizCommandParam, OverkizState
from typing import Any, override

PRESET_SCHEDULE: str
PRESET_MANUAL: str
OVERKIZ_MODE_TO_PRESET_MODES: dict[str, str]
PRESET_MODES_TO_OVERKIZ: Incomplete
OVERKIZ_TO_HVAC_ACTION: dict[str, HVACAction]
HVAC_ACTION_TO_OVERKIZ_PROFILE_STATE: dict[HVACAction, OverkizState]
HVAC_ACTION_TO_OVERKIZ_MODE_STATE: dict[HVACAction, OverkizState]
TEMPERATURE_ZONECONTROL_DEVICE_INDEX: int
SUPPORTED_FEATURES: ClimateEntityFeature
OVERKIZ_THERMAL_CONFIGURATION_TO_HVAC_MODE: dict[OverkizCommandParam, tuple[HVACMode, ClimateEntityFeature]]

class AtlanticPassAPCZoneControlZone(AtlanticPassAPCHeatingZone):
    _attr_target_temperature_step = PRECISION_HALVES
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    zone_control_executor: OverkizExecutor | None
    def __init__(self, device_url: str, coordinator: OverkizDataUpdateCoordinator) -> None: ...
    @cached_property
    def thermal_configuration(self) -> tuple[HVACMode, ClimateEntityFeature] | None: ...
    @cached_property
    def device_hvac_mode(self) -> HVACMode | None: ...
    @property
    def is_using_derogated_temperature_fallback(self) -> bool: ...
    @property
    def zone_control_hvac_action(self) -> HVACAction: ...
    @property
    @override
    def hvac_action(self) -> HVACAction | None: ...
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
    def target_temperature(self) -> float | None: ...
    @property
    @override
    def target_temperature_high(self) -> float | None: ...
    @property
    @override
    def target_temperature_low(self) -> float | None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_refresh_modes(self) -> None: ...
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
