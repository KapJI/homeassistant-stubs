from .coordinator import FumisConfigEntry as FumisConfigEntry, FumisDataUpdateCoordinator as FumisDataUpdateCoordinator
from .entity import FumisEntity as FumisEntity
from .helpers import fumis_exception_handler as fumis_exception_handler
from _typeshed import Incomplete
from fumis import StoveStatus
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
STOVE_STATUS_TO_HVAC_ACTION: dict[StoveStatus, HVACAction | None]

async def async_setup_entry(hass: HomeAssistant, entry: FumisConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FumisClimateEntity(FumisEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_max_temp: float
    _attr_min_temp: float
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step: float
    _attr_temperature_unit: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FumisDataUpdateCoordinator) -> None: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def hvac_action(self) -> HVACAction | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @fumis_exception_handler
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @fumis_exception_handler
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @fumis_exception_handler
    async def async_turn_on(self) -> None: ...
    @fumis_exception_handler
    async def async_turn_off(self) -> None: ...
