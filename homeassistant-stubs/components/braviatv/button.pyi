from .const import DOMAIN as DOMAIN
from .coordinator import BraviaTVCoordinator as BraviaTVCoordinator
from .entity import BraviaTVEntity as BraviaTVEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

class BraviaTVButtonDescriptionMixin:
    press_action: Callable[[BraviaTVCoordinator], Coroutine]
    def __init__(self, press_action) -> None: ...

class BraviaTVButtonDescription(ButtonEntityDescription, BraviaTVButtonDescriptionMixin):
    def __init__(self, press_action, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BUTTONS: tuple[BraviaTVButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BraviaTVButton(BraviaTVEntity, ButtonEntity):
    entity_description: BraviaTVButtonDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: BraviaTVCoordinator, unique_id: str, model: str, description: BraviaTVButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
