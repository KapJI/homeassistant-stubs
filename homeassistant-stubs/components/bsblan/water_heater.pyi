from . import BSBLanConfigEntry as BSBLanConfigEntry, BSBLanData as BSBLanData
from .const import DOMAIN as DOMAIN
from .entity import BSBLanDualCoordinatorEntity as BSBLanDualCoordinatorEntity
from _typeshed import Incomplete
from homeassistant.components.water_heater import STATE_ECO as STATE_ECO, STATE_OFF as STATE_OFF, STATE_PERFORMANCE as STATE_PERFORMANCE, WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
BSBLAN_TO_HA_OPERATION_MODE: dict[int, str]
HA_TO_BSBLAN_OPERATION_MODE: dict[str, int]

async def async_setup_entry(hass: HomeAssistant, entry: BSBLanConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BSBLANWaterHeater(BSBLanDualCoordinatorEntity, WaterHeaterEntity):
    _attr_name: Incomplete
    _attr_operation_list: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_available: bool
    _attr_min_temp: Incomplete
    _attr_max_temp: Incomplete
    def __init__(self, data: BSBLanData) -> None: ...
    @property
    def current_operation(self) -> str | None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def target_temperature(self) -> float | None: ...
    async def async_set_temperature(self, **kwargs: Any) -> None: ...
    async def async_set_operation_mode(self, operation_mode: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
