from .const import DOMAIN as DOMAIN
from .renault_coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from renault_api.kamereon import models as models
from renault_api.renault_vehicle import RenaultVehicle as RenaultVehicle

LOGGER: Incomplete

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
    @property
    def vehicle(self) -> RenaultVehicle: ...
    async def async_initialise(self) -> None: ...

COORDINATORS: tuple[RenaultCoordinatorDescription, ...]
