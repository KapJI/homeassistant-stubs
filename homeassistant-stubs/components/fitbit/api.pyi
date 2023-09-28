from .const import FitbitUnitSystem as FitbitUnitSystem
from .model import FitbitDevice as FitbitDevice, FitbitProfile as FitbitProfile
from _typeshed import Incomplete
from fitbit import Fitbit as Fitbit
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any

_LOGGER: Incomplete

class FitbitApi:
    _hass: Incomplete
    _profile: Incomplete
    _client: Incomplete
    _unit_system: Incomplete
    def __init__(self, hass: HomeAssistant, client: Fitbit, unit_system: FitbitUnitSystem | None = ...) -> None: ...
    @property
    def client(self) -> Fitbit: ...
    async def async_get_user_profile(self) -> FitbitProfile: ...
    async def async_get_unit_system(self) -> FitbitUnitSystem: ...
    async def async_get_devices(self) -> list[FitbitDevice]: ...
    async def async_get_latest_time_series(self, resource_type: str) -> dict[str, Any]: ...
