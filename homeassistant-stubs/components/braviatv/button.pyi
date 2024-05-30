from . import BraviaTVConfigEntry as BraviaTVConfigEntry
from .coordinator import BraviaTVCoordinator as BraviaTVCoordinator
from .entity import BraviaTVEntity as BraviaTVEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class BraviaTVButtonDescription(ButtonEntityDescription):
    press_action: Callable[[BraviaTVCoordinator], Coroutine]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, press_action) -> None: ...

BUTTONS: tuple[BraviaTVButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: BraviaTVConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BraviaTVButton(BraviaTVEntity, ButtonEntity):
    entity_description: BraviaTVButtonDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BraviaTVCoordinator, unique_id: str, model: str, description: BraviaTVButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
