from . import WattsVisionConfigEntry as WattsVisionConfigEntry
from .const import DOMAIN as DOMAIN, HVAC_MODE_TO_THERMOSTAT as HVAC_MODE_TO_THERMOSTAT, THERMOSTAT_MODE_TO_HVAC as THERMOSTAT_MODE_TO_HVAC
from .coordinator import WattsVisionThermostatCoordinator as WattsVisionThermostatCoordinator
from .entity import WattsVisionThermostatEntity as WattsVisionThermostatEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from visionpluspython.models import ThermostatDevice as ThermostatDevice

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WattsVisionConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WattsVisionClimate(WattsVisionThermostatEntity, ClimateEntity):
    _attr_supported_features: Incomplete
    _attr_hvac_modes: Incomplete
    _attr_name: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, coordinator: WattsVisionThermostatCoordinator, thermostat: ThermostatDevice) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def hvac_mode(self) -> HVACMode | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
