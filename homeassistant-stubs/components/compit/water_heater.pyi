from .const import DOMAIN as DOMAIN, MANUFACTURER_NAME as MANUFACTURER_NAME
from .coordinator import CompitConfigEntry as CompitConfigEntry, CompitDataUpdateCoordinator as CompitDataUpdateCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_PERFORMANCE as STATE_PERFORMANCE, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityDescription as WaterHeaterEntityDescription, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from propcache.api import cached_property
from typing import Any

PARALLEL_UPDATES: int
STATE_SCHEDULE: str
COMPIT_STATE_TO_HA: Incomplete
HA_STATE_TO_COMPIT: Incomplete

@dataclass(frozen=True, kw_only=True)
class CompitWaterHeaterEntityDescription(WaterHeaterEntityDescription):
    min_temp: float
    max_temp: float
    supported_features: WaterHeaterEntityFeature
    supports_current_temperature: bool = ...

DEVICE_DEFINITIONS: dict[int, CompitWaterHeaterEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: CompitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CompitWaterHeater(CoordinatorEntity[CompitDataUpdateCoordinator], WaterHeaterEntity):
    _attr_target_temperature_step = PRECISION_WHOLE
    _attr_temperature_unit: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    entity_description: CompitWaterHeaterEntityDescription
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CompitDataUpdateCoordinator, device_id: int, entity_description: CompitWaterHeaterEntityDescription) -> None: ...
    @property
    def available(self) -> bool: ...
    @cached_property
    def min_temp(self) -> float: ...
    @cached_property
    def max_temp(self) -> float: ...
    @cached_property
    def supported_features(self) -> WaterHeaterEntityFeature: ...
    @cached_property
    def operation_list(self) -> list[str] | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    _attr_target_temperature: Incomplete
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    @property
    def current_operation(self) -> str | None: ...
