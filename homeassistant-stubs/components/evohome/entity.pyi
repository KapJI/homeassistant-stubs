import evohomeasync2 as evo
from .const import DOMAIN as DOMAIN, EvoService as EvoService
from .coordinator import EvoDataUpdateCoordinator as EvoDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Mapping
from evohomeasync2.schemas.typedefs import DayOfWeekDhwT as DayOfWeekDhwT
from homeassistant.core import callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGER: Incomplete

class EvoEntity(CoordinatorEntity[EvoDataUpdateCoordinator]):
    _evo_device: evo.ControlSystem | evo.HotWater | evo.Zone
    _evo_id_attr: str
    _evo_state_attr_names: tuple[str, ...]
    _device_state_attrs: dict[str, Any]
    def __init__(self, coordinator: EvoDataUpdateCoordinator, evo_device: evo.ControlSystem | evo.HotWater | evo.Zone) -> None: ...
    async def process_signal(self, payload: dict | None = None) -> None: ...
    async def async_tcs_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    async def async_zone_svc_request(self, service: str, data: dict[str, Any]) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any]: ...
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...

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
