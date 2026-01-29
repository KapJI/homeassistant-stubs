from . import LeilSaunaConfigEntry as LeilSaunaConfigEntry, LeilSaunaCoordinator as LeilSaunaCoordinator
from .const import DEFAULT_PRESET_NAME_TYPE_1 as DEFAULT_PRESET_NAME_TYPE_1, DEFAULT_PRESET_NAME_TYPE_2 as DEFAULT_PRESET_NAME_TYPE_2, DEFAULT_PRESET_NAME_TYPE_3 as DEFAULT_PRESET_NAME_TYPE_3, DELAYED_REFRESH_SECONDS as DELAYED_REFRESH_SECONDS, DOMAIN as DOMAIN, OPT_PRESET_NAME_TYPE_1 as OPT_PRESET_NAME_TYPE_1, OPT_PRESET_NAME_TYPE_2 as OPT_PRESET_NAME_TYPE_2, OPT_PRESET_NAME_TYPE_3 as OPT_PRESET_NAME_TYPE_3
from .entity import LeilSaunaEntity as LeilSaunaEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, FAN_HIGH as FAN_HIGH, FAN_LOW as FAN_LOW, FAN_MEDIUM as FAN_MEDIUM, FAN_OFF as FAN_OFF, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pysaunum import MAX_TEMPERATURE, MIN_TEMPERATURE
from typing import Any

PARALLEL_UPDATES: int
FAN_SPEED_TO_MODE: Incomplete
FAN_MODE_TO_SPEED: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: LeilSaunaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LeilSaunaClimate(LeilSaunaEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_precision = PRECISION_WHOLE
    _attr_target_temperature_step: float
    _attr_min_temp = MIN_TEMPERATURE
    _attr_max_temp = MAX_TEMPERATURE
    _attr_fan_modes: Incomplete
    _preset_name_map: dict[int, str]
    def __init__(self, coordinator: LeilSaunaCoordinator) -> None: ...
    _attr_preset_modes: Incomplete
    def _update_preset_names(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def _async_update_listener(self, hass: HomeAssistant, entry: LeilSaunaConfigEntry) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def fan_mode(self) -> str | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_fan_mode(self, fan_mode: str) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
