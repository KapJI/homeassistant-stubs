from . import PlugwiseConfigEntry as PlugwiseConfigEntry
from .coordinator import PlugwiseDataUpdateCoordinator as PlugwiseDataUpdateCoordinator
from .entity import PlugwiseEntity as PlugwiseEntity
from .util import plugwise_command as plugwise_command
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from plugwise.constants import SwitchType as SwitchType
from typing import Any

@dataclass(frozen=True)
class PlugwiseSwitchEntityDescription(SwitchEntityDescription):
    key: SwitchType
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

SWITCHES: tuple[PlugwiseSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PlugwiseConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PlugwiseSwitchEntity(PlugwiseEntity, SwitchEntity):
    entity_description: PlugwiseSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PlugwiseDataUpdateCoordinator, device_id: str, description: PlugwiseSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
