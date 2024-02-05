from . import SimpliSafe as SimpliSafe, SimpliSafeEntity as SimpliSafeEntity
from .const import DOMAIN as DOMAIN
from .typing import SystemType as SystemType
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from simplipy.system import System as System

@dataclass(frozen=True, kw_only=True)
class SimpliSafeButtonDescription(ButtonEntityDescription):
    push_action: Callable[[System], Awaitable]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, push_action) -> None: ...

BUTTON_KIND_CLEAR_NOTIFICATIONS: str

async def _async_clear_notifications(system: System) -> None: ...

BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SimpliSafeButton(SimpliSafeEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    entity_description: SimpliSafeButtonDescription
    def __init__(self, simplisafe: SimpliSafe, system: SystemType, description: SimpliSafeButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
