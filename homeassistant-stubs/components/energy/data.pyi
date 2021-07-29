from .const import DOMAIN as DOMAIN
from collections.abc import Awaitable
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import singleton as singleton, storage as storage
from typing import Any, Callable, Literal, TypedDict, Union

STORAGE_VERSION: int
STORAGE_KEY = DOMAIN

async def async_get_manager(hass: HomeAssistant) -> EnergyManager: ...

class FlowFromGridSourceType(TypedDict):
    stat_energy_from: str
    stat_cost: Union[str, None]
    entity_energy_from: Union[str, None]
    entity_energy_price: Union[str, None]
    number_energy_price: Union[float, None]

class FlowToGridSourceType(TypedDict):
    stat_energy_to: str
    stat_compensation: Union[str, None]
    entity_energy_from: Union[str, None]
    entity_energy_price: Union[str, None]
    number_energy_price: Union[float, None]

class GridSourceType(TypedDict):
    type: Literal[grid]
    flow_from: list[FlowFromGridSourceType]
    flow_to: list[FlowToGridSourceType]
    cost_adjustment_day: float

class SolarSourceType(TypedDict):
    type: Literal[solar]
    stat_energy_from: str
    config_entry_solar_forecast: Union[list[str], None]
SourceType = Union[GridSourceType, SolarSourceType]

class DeviceConsumption(TypedDict):
    stat_consumption: str

class EnergyPreferences(TypedDict):
    energy_sources: list[SourceType]
    device_consumption: list[DeviceConsumption]

class EnergyPreferencesUpdate(EnergyPreferences): ...

def _flow_from_ensure_single_price(val: FlowFromGridSourceType) -> FlowFromGridSourceType: ...

FLOW_FROM_GRID_SOURCE_SCHEMA: Any
FLOW_TO_GRID_SOURCE_SCHEMA: Any

def _generate_unique_value_validator(key: str) -> Callable[[list[dict]], list[dict]]: ...

GRID_SOURCE_SCHEMA: Any
SOLAR_SOURCE_SCHEMA: Any

def check_type_limits(value: list[SourceType]) -> list[SourceType]: ...

ENERGY_SOURCE_SCHEMA: Any
DEVICE_CONSUMPTION_SCHEMA: Any

class EnergyManager:
    _hass: Any
    _store: Any
    data: Any
    _update_listeners: Any
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_initialize(self) -> None: ...
    @staticmethod
    def default_preferences() -> EnergyPreferences: ...
    async def async_update(self, update: EnergyPreferencesUpdate) -> None: ...
    def async_listen_updates(self, update_listener: Callable[[], Awaitable]) -> None: ...
