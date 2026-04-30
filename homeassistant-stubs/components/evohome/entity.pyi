import evohomeasync2 as evo
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from evohomeasync2.schemas.typedefs import DayOfWeekDhwT as DayOfWeekDhwT
from homeassistant.core import callback as callback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

def is_valid_zone(zone: evo.Zone) -> bool: ...
def unique_zone_id(evo_device: evo.Zone) -> str: ...

class EvoEntity(CoordinatorEntity[EvoDataUpdateCoordinator]):
    _evo_device: evo.ControlSystem | evo.HotWater | evo.Zone
    _evo_id_attr: str
    _evo_state_attr_names: tuple[str, ...]
    _device_state_attrs: dict[str, Any]
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.ControlSystem | evo.HotWater | evo.Zone) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def update_attrs(self) -> None: ...

class EvoChild(EvoEntity):
    _evo_device: evo.HotWater | evo.Zone
    _evo_id: str
    _evo_tcs: Incomplete
    _schedule: list[DayOfWeekDhwT] | None
    _setpoints: dict[str, Any]
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.HotWater | evo.Zone) -> None: ...
    @property
    def current_temperature(self) -> float | None: ...
    @property
    def setpoints(self) -> Mapping[str, Any]: ...
    async def _update_schedule(self, force_refresh: bool = False) -> None: ...
    _device_state_attrs: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def update_attrs(self) -> None: ...
