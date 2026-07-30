from ..const import DOMAIN as DOMAIN
from ..entity import OverkizEntity as OverkizEntity
from _typeshed import Incomplete
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_PERFORMANCE as STATE_PERFORMANCE, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from typing import Any, override

DEFAULT_MIN_TEMP: float
DEFAULT_MAX_TEMP: float
TARGET_TEMPERATURE_STEP: float
BOOST_MODE_DURATION: int
STATE_AUTO: str
STATE_MANUAL: str
OVERKIZ_TO_OPERATION_MODE: dict[str, str]
OPERATION_MODE_TO_OVERKIZ: Incomplete

class AtlanticDomesticHotWaterProductionIOComponent(OverkizEntity, WaterHeaterEntity):
    _attr_temperature_unit: Incomplete
    _attr_translation_key = DOMAIN
    _attr_target_temperature_step = TARGET_TEMPERATURE_STEP
    _attr_supported_features: Incomplete
    _attr_operation_list: Incomplete
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @property
    def is_boost_mode_on(self) -> bool: ...
    @property
    @override
    def is_away_mode_on(self) -> bool: ...
    @property
    @override
    def current_operation(self) -> str | None: ...
    @override
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    @override
    async def async_turn_away_mode_on(self, refresh_afterwards: bool = True) -> None: ...
    @override
    async def async_turn_away_mode_off(self, refresh_afterwards: bool = True) -> None: ...
    async def _async_turn_boost_mode_on(self) -> None: ...
    async def _async_turn_boost_mode_off(self) -> None: ...
