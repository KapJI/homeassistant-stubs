from .const import DOMAIN as DOMAIN
from .renault_coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator
from collections.abc import Awaitable, Callable as Callable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from renault_api.kamereon import models as models
from renault_api.renault_vehicle import RenaultVehicle as RenaultVehicle
from typing import Any

LOGGER: Any

class RenaultCoordinatorDescription:
    endpoint: str
    key: str
    update_method: Callable[[RenaultVehicle], Callable[[], Awaitable[models.KamereonVehicleDataAttributes]]]
    requires_electricity: bool

class RenaultVehicleProxy:
    hass: Any
    _vehicle: Any
    _details: Any
    _device_info: Any
    coordinators: Any
    hvac_target_temperature: int
    _scan_interval: Any
    def __init__(self, hass: HomeAssistant, vehicle: RenaultVehicle, details: models.KamereonVehicleDetails, scan_interval: timedelta) -> None: ...
    @property
    def details(self) -> models.KamereonVehicleDetails: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def vehicle(self) -> RenaultVehicle: ...
    async def async_initialise(self) -> None: ...

COORDINATORS: tuple[RenaultCoordinatorDescription, ...]
