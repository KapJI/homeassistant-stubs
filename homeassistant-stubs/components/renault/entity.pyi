from .coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator, T as T
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class RenaultDataRequiredKeysMixin:
    coordinator: str
    def __init__(self, coordinator) -> None: ...

class RenaultDataEntityDescription(EntityDescription, RenaultDataRequiredKeysMixin):
    def __init__(self, coordinator, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class RenaultEntity(Entity):
    _attr_has_entity_name: bool
    entity_description: EntityDescription
    vehicle: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, vehicle: RenaultVehicleProxy, description: EntityDescription) -> None: ...

class RenaultDataEntity(CoordinatorEntity[RenaultDataUpdateCoordinator[T]], RenaultEntity):
    def __init__(self, vehicle: RenaultVehicleProxy, description: RenaultDataEntityDescription) -> None: ...
    def _get_data_attr(self, key: str) -> StateType: ...
