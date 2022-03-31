from .renault_coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator, T as T
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class RenaultDataRequiredKeysMixin:
    coordinator: str
    def __init__(self, coordinator) -> None: ...

class RenaultDataEntityDescription(EntityDescription, RenaultDataRequiredKeysMixin):
    def __init__(self, coordinator, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement) -> None: ...

class RenaultEntity(Entity):
    entity_description: EntityDescription
    vehicle: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, vehicle: RenaultVehicleProxy, description: EntityDescription) -> None: ...
    @property
    def name(self) -> str: ...

class RenaultDataEntity(CoordinatorEntity[RenaultDataUpdateCoordinator[T]], RenaultEntity):
    def __init__(self, vehicle: RenaultVehicleProxy, description: RenaultDataEntityDescription) -> None: ...
    def _get_data_attr(self, key: str) -> StateType: ...
