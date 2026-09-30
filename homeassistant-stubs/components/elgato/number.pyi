from .coordinator import ElgatoConfigEntry as ElgatoConfigEntry, ElgatoData as ElgatoData, ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from .helpers import color_temperature_range as color_temperature_range, elgato_device_action as elgato_device_action
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from elgato import Elgato as Elgato
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.color import color_temperature_kelvin_to_mired as color_temperature_kelvin_to_mired, color_temperature_mired_to_kelvin as color_temperature_mired_to_kelvin
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ElgatoNumberEntityDescription(NumberEntityDescription):
    has_fn: Callable[[ElgatoData], bool] = ...
    range_fn: Callable[[ElgatoData], tuple[int, int]] | None = ...
    value_fn: Callable[[ElgatoData], float | None]
    set_fn: Callable[[Elgato, float], Awaitable[Any]]

NUMBERS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElgatoNumberEntity(ElgatoEntity, NumberEntity):
    entity_description: ElgatoNumberEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoNumberEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @elgato_device_action
    @override
    async def async_set_native_value(self, value: float) -> None: ...
