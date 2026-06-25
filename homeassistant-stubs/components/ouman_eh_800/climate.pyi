from .const import OumanDevice as OumanDevice
from .coordinator import OumanEh800ConfigEntry as OumanEh800ConfigEntry, OumanEh800Coordinator as OumanEh800Coordinator
from .entity import OumanEh800Entity as OumanEh800Entity, OumanEh800EntityDescription as OumanEh800EntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.climate import ATTR_HVAC_MODE as ATTR_HVAC_MODE, ClimateEntity as ClimateEntity, ClimateEntityDescription as ClimateEntityDescription, ClimateEntityFeature as ClimateEntityFeature, HVACAction as HVACAction, HVACMode as HVACMode
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ouman_eh_800_api import EnumControlOumanEndpoint as EnumControlOumanEndpoint, FloatControlOumanEndpoint as FloatControlOumanEndpoint, NumberOumanEndpoint as NumberOumanEndpoint, OperationMode
from typing import Any, override

PARALLEL_UPDATES: int
_HEAT_OPERATION_MODES: tuple[OperationMode, ...]
_PRESET_TO_OPERATION_MODE: dict[str, OperationMode]
_DEFAULT_HEAT_OPERATION_MODE: Incomplete

@dataclass(frozen=True, kw_only=True)
class OumanEh800ClimateEntityDescription(OumanEh800EntityDescription, ClimateEntityDescription):
    operation_mode_endpoint: EnumControlOumanEndpoint
    current_temperature_endpoint: NumberOumanEndpoint
    target_temperature_endpoint: FloatControlOumanEndpoint
    valve_position_endpoint: NumberOumanEndpoint

CLIMATE_DESCRIPTIONS: tuple[OumanEh800ClimateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OumanEh800ClimateEntity(OumanEh800Entity, ClimateEntity):
    entity_description: OumanEh800ClimateEntityDescription
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_target_temperature_step: float
    _attr_hvac_modes: Incomplete
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def __init__(self, coordinator: OumanEh800Coordinator, description: OumanEh800ClimateEntityDescription) -> None: ...
    @property
    def _operation_mode(self) -> OperationMode: ...
    @property
    @override
    def hvac_mode(self) -> HVACMode: ...
    @property
    @override
    def hvac_action(self) -> HVACAction: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @property
    @override
    def current_temperature(self) -> float: ...
    @property
    @override
    def target_temperature(self) -> float: ...
    @override
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    @override
    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None: ...
    @override
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
