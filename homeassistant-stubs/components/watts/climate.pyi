from . import WattsVisionConfigEntry as WattsVisionConfigEntry
from .const import DOMAIN as DOMAIN, HVAC_ACTION_TO_HA as HVAC_ACTION_TO_HA, HVAC_MODE_TO_THERMOSTAT as HVAC_MODE_TO_THERMOSTAT, PRESET_MODES as PRESET_MODES, PRESET_MODE_TO_THERMOSTAT as PRESET_MODE_TO_THERMOSTAT, THERMOSTAT_MODE_TO_HVAC as THERMOSTAT_MODE_TO_HVAC, THERMOSTAT_MODE_TO_PRESET as THERMOSTAT_MODE_TO_PRESET
from .coordinator import WattsVisionDeviceCoordinator as WattsVisionDeviceCoordinator
from .entity import WattsVisionEntity as WattsVisionEntity
from _typeshed import Incomplete
from datetime import timedelta
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override
from visionpluspython.models import ThermostatDevice, ThermostatMode

_LOGGER: Incomplete
PARALLEL_UPDATES: int

def _parse_thermostat_mode(mode: str) -> ThermostatMode: ...
async def async_setup_entry(hass: HomeAssistant, entry: WattsVisionConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WattsVisionClimate(WattsVisionEntity[ThermostatDevice], ClimateEntity):
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_preset_modes = PRESET_MODES
    _attr_name: Incomplete
    _attr_translation_key: str
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, coordinator: WattsVisionDeviceCoordinator, thermostat: ThermostatDevice) -> None: ...
    @property
    @override
    def current_temperature(self) -> float | None: ...
    @property
    @override
    def target_temperature(self) -> float | None: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode | None: ...
    @property
    @override
    def hvac_action(self) -> HVACAction | None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_activate_timer_mode(self, temperature: float, duration: timedelta) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
