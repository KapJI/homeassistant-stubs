from .renault_coordinator import T as T
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Optional

class RenaultRequiredKeysMixin:
    coordinator: str

class RenaultEntityDescription(EntityDescription, RenaultRequiredKeysMixin): ...

class RenaultDataEntity(CoordinatorEntity[Optional[T]], Entity):
    entity_description: RenaultEntityDescription
    vehicle: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, vehicle: RenaultVehicleProxy, description: RenaultEntityDescription) -> None: ...
    def _get_data_attr(self, key: str) -> StateType: ...
    @property
    def name(self) -> str: ...
