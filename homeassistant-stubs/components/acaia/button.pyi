from .coordinator import AcaiaConfigEntry as AcaiaConfigEntry
from .entity import AcaiaEntity as AcaiaEntity
from aioacaia.acaiascale import AcaiaScale as AcaiaScale
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class AcaiaButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[AcaiaScale], Coroutine[Any, Any, None]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., press_fn) -> None: ...

BUTTONS: tuple[AcaiaButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AcaiaConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AcaiaButton(AcaiaEntity, ButtonEntity):
    entity_description: AcaiaButtonEntityDescription
    async def async_press(self) -> None: ...
