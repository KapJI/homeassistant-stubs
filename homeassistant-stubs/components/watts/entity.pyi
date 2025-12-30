from .const import DOMAIN as DOMAIN
from .coordinator import WattsVisionThermostatCoordinator as WattsVisionThermostatCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from visionpluspython.models import ThermostatDevice as ThermostatDevice

class WattsVisionThermostatEntity(CoordinatorEntity[WattsVisionThermostatCoordinator]):
    _attr_has_entity_name: bool
    device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: WattsVisionThermostatCoordinator, device_id: str) -> None: ...
    @property
    def thermostat(self) -> ThermostatDevice: ...
    @property
    def available(self) -> bool: ...
