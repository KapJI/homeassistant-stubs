from .renault_coordinator import T as T
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Optional

class RenaultDataRequiredKeysMixin:
    coordinator: str

class RenaultDataEntityDescription(EntityDescription, RenaultDataRequiredKeysMixin): ...

class RenaultEntity(Entity):
    entity_description: EntityDescription
    vehicle: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, vehicle: RenaultVehicleProxy, description: EntityDescription) -> None: ...
    @property
    def name(self) -> str: ...

class RenaultDataEntity(CoordinatorEntity[Optional[T]], RenaultEntity):
    def __init__(self, vehicle: RenaultVehicleProxy, description: RenaultDataEntityDescription) -> None: ...
    def _get_data_attr(self, key: str) -> StateType: ...
