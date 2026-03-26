from .const import CONFIG_DEFAULT_MAX_TEMP as CONFIG_DEFAULT_MAX_TEMP, CONFIG_DEFAULT_MIN_TEMP as CONFIG_DEFAULT_MIN_TEMP
from .coordinator import HuumConfigEntry as HuumConfigEntry, HuumDataUpdateCoordinator as HuumDataUpdateCoordinator
from .entity import HuumBaseEntity as HuumBaseEntity
from _typeshed import Incomplete
from homeassistant.components.climate import ClimateEntity as ClimateEntity, ClimateEntityFeature as ClimateEntityFeature, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: HuumConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HuumDevice(HuumBaseEntity, ClimateEntity):
    _attr_hvac_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: HuumDataUpdateCoordinator) -> None: ...
    @property
    def min_temp(self) -> int: ...
    @property
    def max_temp(self) -> int: ...
    @property
    def hvac_mode(self) -> HVACMode: ...
    @property
    def current_temperature(self) -> int | None: ...
    @property
    def target_temperature(self) -> int: ...
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def _turn_on(self, temperature: int) -> None: ...
