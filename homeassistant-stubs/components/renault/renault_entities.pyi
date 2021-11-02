from .renault_coordinator import T as T
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from collections.abc import Mapping
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.dt import as_utc as as_utc, parse_datetime as parse_datetime
from typing import Any, Optional

class RenaultRequiredKeysMixin:
    coordinator: str

class RenaultEntityDescription(EntityDescription, RenaultRequiredKeysMixin): ...

ATTR_LAST_UPDATE: str

class RenaultDataEntity(CoordinatorEntity[Optional[T]], Entity):
    entity_description: RenaultEntityDescription
    vehicle: Any
    _attr_device_info: Any
    _attr_unique_id: Any
    def __init__(self, vehicle: RenaultVehicleProxy, description: RenaultEntityDescription) -> None: ...
    def _get_data_attr(self, key: str) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...

def _convert_to_utc_string(value: str) -> str: ...
