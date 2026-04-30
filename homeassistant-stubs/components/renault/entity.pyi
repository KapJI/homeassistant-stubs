from .coordinator import RenaultDataUpdateCoordinator as RenaultDataUpdateCoordinator
from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from renault_api.kamereon.models import KamereonVehicleDataAttributes as KamereonVehicleDataAttributes

@dataclass(frozen=True, kw_only=True)
class RenaultDataEntityDescription(EntityDescription):
    coordinator: str

class RenaultEntity(Entity):
    _attr_has_entity_name: bool
    entity_description: EntityDescription
    vehicle: Incomplete
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, vehicle: RenaultVehicleProxy, description: EntityDescription) -> None: ...

class RenaultDataEntity[T: KamereonVehicleDataAttributes](CoordinatorEntity[RenaultDataUpdateCoordinator[T]], RenaultEntity):
    def __init__(self, vehicle: RenaultVehicleProxy, description: RenaultDataEntityDescription) -> None: ...
    @property
    def assumed_state(self) -> bool: ...
