from .const import DOMAIN as DOMAIN
from .renault_coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable, Coroutine
from datetime import datetime, timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from renault_api.kamereon import models as models
from renault_api.renault_vehicle import RenaultVehicle as RenaultVehicle
from typing import Any, Concatenate, TypeVar

LOGGER: Incomplete
_T = TypeVar('_T')
_P: Incomplete

def with_error_wrapping(func: Callable[Concatenate[RenaultVehicleProxy, _P], Awaitable[_T]]) -> Callable[Concatenate[RenaultVehicleProxy, _P], Coroutine[Any, Any, _T]]: ...

class RenaultCoordinatorDescription:
    endpoint: str
    key: str
    update_method: Callable[[RenaultVehicle], Callable[[], Awaitable[models.KamereonVehicleDataAttributes]]]
    requires_electricity: bool
    def __init__(self, endpoint, key, update_method, requires_electricity) -> None: ...

class RenaultVehicleProxy:
    hass: Incomplete
    _vehicle: Incomplete
    _details: Incomplete
    _device_info: Incomplete
    coordinators: Incomplete
    hvac_target_temperature: int
    _scan_interval: Incomplete
    def __init__(self, hass: HomeAssistant, vehicle: RenaultVehicle, details: models.KamereonVehicleDetails, scan_interval: timedelta) -> None: ...
    @property
    def details(self) -> models.KamereonVehicleDetails: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    async def async_initialise(self) -> None: ...
    async def set_charge_mode(self, charge_mode: str) -> models.KamereonVehicleChargeModeActionData: ...
    async def set_charge_start(self) -> models.KamereonVehicleChargingStartActionData: ...
    async def set_ac_stop(self) -> models.KamereonVehicleHvacStartActionData: ...
    async def set_ac_start(self, temperature: float, when: Union[datetime, None] = ...) -> models.KamereonVehicleHvacStartActionData: ...
    async def get_charging_settings(self) -> models.KamereonVehicleChargingSettingsData: ...
    async def set_charge_schedules(self, schedules: list[models.ChargeSchedule]) -> models.KamereonVehicleChargeScheduleActionData: ...

COORDINATORS: tuple[RenaultCoordinatorDescription, ...]
