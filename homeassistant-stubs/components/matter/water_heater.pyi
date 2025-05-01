from .entity import MatterEntity as MatterEntity
from .helpers import get_matter as get_matter
from .models import MatterDiscoverySchema as MatterDiscoverySchema
from _typeshed import Incomplete
from chip.clusters import Objects as clusters
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_HIGH_DEMAND as STATE_HIGH_DEMAND, STATE_OFF as STATE_OFF, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityDescription as WaterHeaterEntityDescription, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_WHOLE as PRECISION_WHOLE, Platform as Platform, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

TEMPERATURE_SCALING_FACTOR: int
WATER_HEATER_SYSTEM_MODE_MAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MatterWaterHeater(MatterEntity, WaterHeaterEntity):
    _attr_current_temperature: float | None
    _attr_current_operation: str
    _attr_operation_list: Incomplete
    _attr_precision = PRECISION_WHOLE
    _attr_supported_features: Incomplete
    _attr_target_temperature: float | None
    _attr_temperature_unit: Incomplete
    _platform_translation_key: str
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_temperature: Incomplete
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    @callback
    def _update_from_device(self) -> None: ...
    @callback
    def _get_temperature_in_degrees(self, attribute: type[clusters.ClusterAttributeDescriptor]) -> float | None: ...

DISCOVERY_SCHEMAS: Incomplete
