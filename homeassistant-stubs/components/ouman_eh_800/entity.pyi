from .const import OumanDevice as OumanDevice
from .coordinator import OumanEh800Coordinator as OumanEh800Coordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from ouman_eh_800_api import OumanEndpoint as OumanEndpoint

@dataclass(frozen=True, kw_only=True)
class OumanEh800EntityDescription(EntityDescription):
    device: OumanDevice

class OumanEh800Entity(CoordinatorEntity[OumanEh800Coordinator]):
    _attr_has_entity_name: bool
    entity_description: OumanEh800EntityDescription
    _endpoint: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: OumanEh800Coordinator, endpoint: OumanEndpoint, description: OumanEh800EntityDescription) -> None: ...
