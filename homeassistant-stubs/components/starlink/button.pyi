from .const import DOMAIN as DOMAIN
from .coordinator import StarlinkUpdateCoordinator as StarlinkUpdateCoordinator
from .entity import StarlinkEntity as StarlinkEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

@dataclass
class StarlinkButtonEntityDescriptionMixin:
    press_fn: Callable[[StarlinkUpdateCoordinator], Awaitable[None]]
    def __init__(self, press_fn) -> None: ...

@dataclass
class StarlinkButtonEntityDescription(ButtonEntityDescription, StarlinkButtonEntityDescriptionMixin):
    def __init__(self, press_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

class StarlinkButtonEntity(StarlinkEntity, ButtonEntity):
    entity_description: StarlinkButtonEntityDescription
    async def async_press(self) -> None: ...

BUTTONS: Incomplete
