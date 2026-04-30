from . import RenaultConfigEntry as RenaultConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from renault_api.kamereon.models import KamereonVehicleBatterySocData, KamereonVehicleDataAttributes as KamereonVehicleDataAttributes
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RenaultNumberEntityDescription[T: KamereonVehicleDataAttributes](NumberEntityDescription, RenaultDataEntityDescription):
    value_fn: Callable[[RenaultNumberEntity[T]], float | None]
    update_fn: Callable[[RenaultNumberEntity[T], float], Coroutine[Any, Any, None]]

async def _set_charge_limit_min(entity: RenaultNumberEntity[KamereonVehicleBatterySocData], value: float) -> None: ...
async def _set_charge_limit_target(entity: RenaultNumberEntity[KamereonVehicleBatterySocData], value: float) -> None: ...
async def _set_charge_limits(entity: RenaultNumberEntity[KamereonVehicleBatterySocData], min_soc: int, target_soc: int) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: RenaultConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RenaultNumberEntity[T: KamereonVehicleDataAttributes](RenaultDataEntity[T], NumberEntity):
    entity_description: RenaultNumberEntityDescription[T]
    @property
    def native_value(self) -> float | None: ...
    async def async_set_native_value(self, value: float) -> None: ...

NUMBER_TYPES: tuple[RenaultNumberEntityDescription, ...]
