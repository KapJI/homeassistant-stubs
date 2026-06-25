from .const import DOMAIN as DOMAIN
from .coordinator import AqvifyAggrDataCoordinator as AqvifyAggrDataCoordinator, AqvifyCoordinator as AqvifyCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class AqvifyBaseEntity[_AqvifyCoordinatorT: AqvifyCoordinator | AqvifyAggrDataCoordinator](CoordinatorEntity[_AqvifyCoordinatorT]):
    _attr_has_entity_name: bool
    account_id: Incomplete
    device_key: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: _AqvifyCoordinatorT, device_key: str, description: EntityDescription) -> None: ...

class AqvifyEntity(AqvifyBaseEntity[AqvifyCoordinator]):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: AqvifyCoordinator, device_key: str, description: EntityDescription) -> None: ...

class AqvifyAggrEntity(AqvifyBaseEntity[AqvifyAggrDataCoordinator]): ...
