from .const import DOMAIN as DOMAIN
from .entity import RenaultEntity as RenaultEntity
from .renault_hub import RenaultHub as RenaultHub
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

class RenaultButtonRequiredKeysMixin:
    async_press: Callable[[RenaultButtonEntity], Coroutine[Any, Any, Any]]
    def __init__(self, async_press) -> None: ...

class RenaultButtonEntityDescription(ButtonEntityDescription, RenaultButtonRequiredKeysMixin):
    requires_electricity: bool
    def __init__(self, async_press, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, requires_electricity) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultButtonEntity(RenaultEntity, ButtonEntity):
    entity_description: RenaultButtonEntityDescription
    async def async_press(self) -> None: ...

BUTTON_TYPES: tuple[RenaultButtonEntityDescription, ...]
