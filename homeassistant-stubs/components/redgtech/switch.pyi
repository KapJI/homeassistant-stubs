from .const import DOMAIN as DOMAIN, INTEGRATION_NAME as INTEGRATION_NAME
from .coordinator import RedgtechConfigEntry as RedgtechConfigEntry, RedgtechDataUpdateCoordinator as RedgtechDataUpdateCoordinator, RedgtechDevice as RedgtechDevice
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: RedgtechConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RedgtechSwitch(CoordinatorEntity[RedgtechDataUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    coordinator: Incomplete
    device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: RedgtechDataUpdateCoordinator, device: RedgtechDevice) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def _set_state(self, new_state: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
