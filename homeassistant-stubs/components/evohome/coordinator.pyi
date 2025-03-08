import evohomeasync as ec1
import evohomeasync2 as ec2
import logging
from _typeshed import Incomplete
from collections.abc import Awaitable
from datetime import timedelta
from evohomeasync2.schemas.typedefs import EvoLocStatusResponseT as EvoLocStatusResponseT, EvoTcsConfigResponseT as EvoTcsConfigResponseT
from homeassistant.const import CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any

class EvoDataUpdateCoordinator(DataUpdateCoordinator):
    loc: ec2.Location
    tcs: ec2.ControlSystem
    client: Incomplete
    client_v1: Incomplete
    loc_idx: Incomplete
    data: EvoLocStatusResponseT
    temps: dict[str, float | None]
    _first_refresh_done: bool
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, client_v2: ec2.EvohomeClient, *, name: str, update_interval: timedelta, location_idx: int, client_v1: ec1.EvohomeClient | None = None) -> None: ...
    async def async_first_refresh(self) -> None: ...
    async def _async_setup(self) -> None: ...
    async def call_client_api(self, client_api: Awaitable[dict[str, Any] | None], request_refresh: bool = True) -> dict[str, Any] | None: ...
    async def _update_v1_api_temps(self) -> None: ...
    async def _update_v2_api_state(self, *args: Any) -> None: ...
    async def _update_v2_schedules(self) -> None: ...
    async def _async_update_data(self) -> EvoLocStatusResponseT: ...
