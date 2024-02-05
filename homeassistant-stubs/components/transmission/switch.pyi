from .const import DOMAIN as DOMAIN
from .coordinator import TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

_LOGGING: Incomplete

@dataclass(frozen=True)
class TransmissionSwitchEntityDescriptionMixin:
    is_on_func: Callable[[TransmissionDataUpdateCoordinator], bool | None]
    on_func: Callable[[TransmissionDataUpdateCoordinator], None]
    off_func: Callable[[TransmissionDataUpdateCoordinator], None]
    def __init__(self, is_on_func, on_func, off_func) -> None: ...

@dataclass(frozen=True)
class TransmissionSwitchEntityDescription(SwitchEntityDescription, TransmissionSwitchEntityDescriptionMixin):
    def __init__(self, is_on_func, on_func, off_func, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

SWITCH_TYPES: tuple[TransmissionSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TransmissionSwitch(CoordinatorEntity[TransmissionDataUpdateCoordinator], SwitchEntity):
    entity_description: TransmissionSwitchEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TransmissionDataUpdateCoordinator, entity_description: TransmissionSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
