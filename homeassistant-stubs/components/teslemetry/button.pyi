from . import TeslemetryConfigEntry as TeslemetryConfigEntry
from .entity import TeslemetryVehicleStreamEntity as TeslemetryVehicleStreamEntity
from .helpers import handle_command as handle_command, handle_vehicle_command as handle_vehicle_command
from .models import TeslemetryVehicleData as TeslemetryVehicleData
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tesla_fleet_api.teslemetry import Vehicle as Vehicle
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TeslemetryButtonEntityDescription(ButtonEntityDescription):
    func: Callable[[TeslemetryButtonEntity], Awaitable[Any]]

DESCRIPTIONS: tuple[TeslemetryButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TeslemetryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TeslemetryButtonEntity(TeslemetryVehicleStreamEntity, ButtonEntity):
    api: Vehicle
    entity_description: TeslemetryButtonEntityDescription
    def __init__(self, data: TeslemetryVehicleData, description: TeslemetryButtonEntityDescription) -> None: ...
    def _async_update_attrs(self) -> None: ...
    async def async_press(self) -> None: ...
