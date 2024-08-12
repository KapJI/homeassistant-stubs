from . import ElgatorConfigEntry as ElgatorConfigEntry
from .coordinator import ElgatoDataUpdateCoordinator as ElgatoDataUpdateCoordinator
from .entity import ElgatoEntity as ElgatoEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from elgato import Elgato as Elgato
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class ElgatoButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Elgato], Awaitable[Any]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., press_fn) -> None: ...

BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ElgatorConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElgatoButtonEntity(ElgatoEntity, ButtonEntity):
    entity_description: ElgatoButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ElgatoDataUpdateCoordinator, description: ElgatoButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
