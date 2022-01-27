from .const import DOMAIN as DOMAIN
from aiooncue import OncueDevice as OncueDevice, OncueSensor as OncueSensor
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class OncueEntity(CoordinatorEntity, Entity):
    entity_description: Any
    _device_id: Any
    _attr_unique_id: Any
    _attr_name: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, device_id: str, device: OncueDevice, sensor: OncueSensor, description: EntityDescription) -> None: ...
    @property
    def _oncue_value(self) -> str: ...
