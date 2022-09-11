from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from aiooncue import OncueDevice as OncueDevice, OncueSensor as OncueSensor
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class OncueEntity(CoordinatorEntity, Entity):
    entity_description: Incomplete
    _device_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, device_id: str, device: OncueDevice, sensor: OncueSensor, description: EntityDescription) -> None: ...
    @property
    def _oncue_value(self) -> str: ...
