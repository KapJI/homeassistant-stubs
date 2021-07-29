from .const import DOMAIN as DOMAIN
from .renault_coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator
from datetime import timedelta
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from renault_api.kamereon import models as models
from renault_api.renault_vehicle import RenaultVehicle as RenaultVehicle
from typing import Any

LOGGER: Any

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
    async def async_initialise(self) -> None: ...
    async def endpoint_available(self, endpoint: str) -> bool: ...
    async def get_battery_status(self) -> models.KamereonVehicleBatteryStatusData: ...
    async def get_charge_mode(self) -> models.KamereonVehicleChargeModeData: ...
    async def get_cockpit(self) -> models.KamereonVehicleCockpitData: ...
    async def get_hvac_status(self) -> models.KamereonVehicleHvacStatusData: ...
