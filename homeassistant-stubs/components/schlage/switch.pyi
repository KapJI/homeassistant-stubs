from .coordinator import LockData as LockData, SchlageDataUpdateCoordinator as SchlageDataUpdateCoordinator
from .entity import SchlageEntity as SchlageEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyschlage.lock import Lock as Lock
from typing import Any

@dataclass(frozen=True, kw_only=True)
class SchlageSwitchEntityDescription(SwitchEntityDescription):
    on_fn: Callable[[Lock], None]
    off_fn: Callable[[Lock], None]
    value_fn: Callable[[Lock], bool]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., on_fn, off_fn, value_fn) -> None: ...

SWITCHES: tuple[SchlageSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SchlageSwitch(SchlageEntity, SwitchEntity):
    entity_description: SchlageSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SchlageDataUpdateCoordinator, description: SchlageSwitchEntityDescription, device_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
