from .const import DOMAIN as DOMAIN
from .coordinator import TailwindDataUpdateCoordinator as TailwindDataUpdateCoordinator
from .entity import TailwindEntity as TailwindEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from gotailwind import Tailwind as Tailwind
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class TailwindButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[Tailwind], Awaitable[Any]]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, press_fn) -> None: ...

DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TailwindButtonEntity(TailwindEntity, ButtonEntity):
    entity_description: TailwindButtonEntityDescription
    async def async_press(self) -> None: ...
