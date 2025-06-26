from .const import DOMAIN as DOMAIN
from .coordinator import NextDnsUpdateCoordinator as NextDnsUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from nextdns.model import NextDnsData as NextDnsData

class NextDnsEntity[CoordinatorDataT: NextDnsData](CoordinatorEntity[NextDnsUpdateCoordinator[CoordinatorDataT]]):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: NextDnsUpdateCoordinator[CoordinatorDataT], description: EntityDescription) -> None: ...
