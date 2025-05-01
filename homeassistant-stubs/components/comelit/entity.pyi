from .coordinator import ComelitSerialBridge as ComelitSerialBridge
from _typeshed import Incomplete
from aiocomelit import ComelitSerialBridgeObject as ComelitSerialBridgeObject
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class ComelitBridgeBaseEntity(CoordinatorEntity[ComelitSerialBridge]):
    _attr_has_entity_name: bool
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ComelitSerialBridge, device: ComelitSerialBridgeObject, config_entry_entry_id: str) -> None: ...
