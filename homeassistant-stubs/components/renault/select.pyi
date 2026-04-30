from . import RenaultConfigEntry as RenaultConfigEntry
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleDataAttributes as KamereonVehicleDataAttributes
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultSelectEntityDescription[T: KamereonVehicleDataAttributes](SelectEntityDescription, RenaultDataEntityDescription):
    value_fn: Callable[[RenaultSelectEntity[T]], str | None]
    update_fn: Callable[[RenaultSelectEntity[T], str], Coroutine[Any, Any, Any]]

async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RenaultSelectEntity[T: KamereonVehicleDataAttributes](RenaultDataEntity[T], SelectEntity):
    entity_description: RenaultSelectEntityDescription[T]
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

SENSOR_TYPES: tuple[RenaultSelectEntityDescription, ...]
