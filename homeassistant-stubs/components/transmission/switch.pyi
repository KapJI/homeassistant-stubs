from .const import DOMAIN as DOMAIN, SWITCH_TYPES as SWITCH_TYPES
from .coordinator import TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGING: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TransmissionSwitch(CoordinatorEntity[TransmissionDataUpdateCoordinator], SwitchEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_name: Incomplete
    type: Incomplete
    unsub_update: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, switch_type: str, switch_name: str, coordinator: TransmissionDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
