from .const import DOMAIN as DOMAIN
from .coordinator import TedeeApiCoordinator as TedeeApiCoordinator
from _typeshed import Incomplete
from homeassistant.core import callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytedee_async.lock import TedeeLock as TedeeLock

class TedeeEntity(CoordinatorEntity[TedeeApiCoordinator]):
    _attr_has_entity_name: bool
    _lock: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, lock: TedeeLock, coordinator: TedeeApiCoordinator, key: str) -> None: ...
    def _handle_coordinator_update(self) -> None: ...

class TedeeDescriptionEntity(TedeeEntity):
    entity_description: EntityDescription
    def __init__(self, lock: TedeeLock, coordinator: TedeeApiCoordinator, entity_description: EntityDescription) -> None: ...
