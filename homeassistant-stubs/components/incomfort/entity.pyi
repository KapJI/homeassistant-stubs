from .const import DOMAIN as DOMAIN
from .coordinator import InComfortDataCoordinator as InComfortDataCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from incomfortclient import Heater as Heater

class IncomfortEntity(CoordinatorEntity[InComfortDataCoordinator]):
    _attr_has_entity_name: bool

class IncomfortBoilerEntity(IncomfortEntity):
    _heater: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: InComfortDataCoordinator, heater: Heater) -> None: ...
