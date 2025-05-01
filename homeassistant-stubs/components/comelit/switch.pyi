from .coordinator import ComelitConfigEntry as ComelitConfigEntry, ComelitSerialBridge as ComelitSerialBridge
from .entity import ComelitBridgeBaseEntity as ComelitBridgeBaseEntity
from _typeshed import Incomplete
from aiocomelit import ComelitSerialBridgeObject as ComelitSerialBridgeObject
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ComelitConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ComelitSwitchEntity(ComelitBridgeBaseEntity, SwitchEntity):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_class: Incomplete
    def __init__(self, coordinator: ComelitSerialBridge, device: ComelitSerialBridgeObject, config_entry_entry_id: str) -> None: ...
    async def _switch_set_state(self, state: int) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
