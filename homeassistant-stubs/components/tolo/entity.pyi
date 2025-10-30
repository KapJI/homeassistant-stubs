from .const import DOMAIN as DOMAIN
from .coordinator import ToloConfigEntry as ToloConfigEntry, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ToloSaunaCoordinatorEntity(CoordinatorEntity[ToloSaunaUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ToloConfigEntry) -> None: ...
