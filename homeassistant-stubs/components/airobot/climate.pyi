from . import AirobotConfigEntry as AirobotConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AirobotDataUpdateCoordinator as AirobotDataUpdateCoordinator
from .entity import AirobotEntity as AirobotEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode, PRESET_AWAY as PRESET_AWAY, PRESET_BOOST as PRESET_BOOST, PRESET_HOME as PRESET_HOME
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyairobotrest.const import SETPOINT_TEMP_MAX, SETPOINT_TEMP_MIN
from pyairobotrest.models import ThermostatSettings as ThermostatSettings, ThermostatStatus as ThermostatStatus
from typing import Any

PARALLEL_UPDATES: int
_PRESET_MODE_2_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AirobotConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class AirobotClimate(AirobotEntity, ClimateEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_temperature_unit: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_min_temp = SETPOINT_TEMP_MIN
    _attr_max_temp = SETPOINT_TEMP_MAX
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: AirobotDataUpdateCoordinator) -> None: ...
    @property
    def _status(self) -> ThermostatStatus: ...
    @property
    def _settings(self) -> ThermostatSettings: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def current_humidity(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction: ...
    @property
    def preset_mode(self) -> str | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
