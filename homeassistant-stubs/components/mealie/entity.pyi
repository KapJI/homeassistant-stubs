from .const import DOMAIN as DOMAIN
from .coordinator import MealieDataUpdateCoordinator as MealieDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class MealieEntity(CoordinatorEntity[MealieDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MealieDataUpdateCoordinator, key: str) -> None: ...
