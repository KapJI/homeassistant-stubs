from .coordinator import InComfortConfigEntry as InComfortConfigEntry, InComfortDataCoordinator as InComfortDataCoordinator
from .entity import IncomfortBoilerEntity as IncomfortBoilerEntity
from _typeshed import Incomplete
from homeassistant.components.water_heater import WaterHeaterEntity as WaterHeaterEntity
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from incomfortclient import Heater as InComfortHeater
from typing import Any

_LOGGER: Incomplete
HEATER_ATTRS: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: InComfortConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IncomfortWaterHeater(IncomfortBoilerEntity, WaterHeaterEntity):
    _attr_entity_category: Incomplete
    _attr_min_temp: float
    _attr_max_temp: float
    _attr_name: Incomplete
    _attr_temperature_unit: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: InComfortDataCoordinator, heater: InComfortHeater) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def current_operation(self) -> str | None: ...
